using System;
using Avalonia;
using Avalonia.Animation;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;
using Avalonia.Styling;
using FluentAvalonia.Core;
using FluentAvalonia.UI.Controls;
using FluentAvalonia.UI.Navigation;
using Microsoft.Extensions.Configuration;
using Scheduler.Desktop.Pages;
using Scheduler.Desktop.Services;
using Scheduler.Desktop.ViewModels;

namespace Scheduler.Desktop.Views;

public partial class MainView : UserControl
{
    private Frame? _frameView;
    private NavigationView? _navView;

    public MainView()
    {
        InitializeComponent();
        IConfiguration config = new ConfigurationBuilder()
            .AddJsonFile("appsettings.json")
            .AddEnvironmentVariables()
            .Build();

        DataContext = new MainViewViewModel(config);
    }

    private void InitializeComponent()
    {
        AvaloniaXamlLoader.Load(this);
    }

    protected override void OnAttachedToVisualTree(VisualTreeAttachmentEventArgs e)
    {
        base.OnAttachedToVisualTree(e);

        _frameView = this.FindControl<Frame>("FrameView");
        _frameView.Navigated += OnFrameViewNavigated;

        _navView = this.FindControl<NavigationView>("NavView");
        _navView.BackRequested += OnNavigationViewBackRequested;
        _navView.SelectionChanged += OnNavigationViewSelectionChanged;

        _frameView.Navigate(typeof(MoviesPage));

        NavigationService.Instance.SetFrame(_frameView);
    }

    private void OnFrameViewNavigated(object sender, NavigationEventArgs e)
    {
        var found = false;

        foreach (NavigationViewItem navViewSelectedItem in _navView.MenuItems)
            if (navViewSelectedItem.Tag is Type tag && tag == e.SourcePageType)
            {
                found = true;
                _navView.SelectedItem = navViewSelectedItem;
                break;
            }

        if (!found)
            _navView.SelectedItem = e.SourcePageType == typeof(SettingsPage)
                ? _navView.FooterMenuItems.ElementAt(0)
                : _navView.MenuItems.ElementAt(1);

        switch (_frameView.BackStackDepth)
        {
            case > 0 when !_navView.IsBackButtonVisible:
                AnimateContentForBackButton(true);
                break;
            case 0 when _navView.IsBackButtonVisible:
                AnimateContentForBackButton(false);
                break;
        }
    }

    private async void AnimateContentForBackButton(bool show)
    {
        if (show)
        {
            var animation = new Animation
            {
                Duration = TimeSpan.FromMilliseconds(250),
                FillMode = FillMode.Forward,
                Children =
                {
                    new KeyFrame
                    {
                        Cue = new Cue(0d),
                        Setters =
                        {
                            new Setter(MarginProperty, new Thickness(12, 4, 12, 4))
                        }
                    },
                    new KeyFrame
                    {
                        Cue = new Cue(1d),
                        KeySpline = new KeySpline(0, 0, 0, 1),
                        Setters =
                        {
                            new Setter(MarginProperty, new Thickness(48, 4, 12, 4))
                        }
                    }
                }
            };

            _navView.IsBackButtonVisible = true;
        }
        else
        {
            _navView.IsBackButtonVisible = false;

            var animation = new Animation
            {
                Duration = TimeSpan.FromMilliseconds(250),
                FillMode = FillMode.Forward,
                Children =
                {
                    new KeyFrame
                    {
                        Cue = new Cue(0d),
                        Setters =
                        {
                            new Setter(MarginProperty, new Thickness(48, 4, 12, 4))
                        }
                    },
                    new KeyFrame
                    {
                        Cue = new Cue(1d),
                        KeySpline = new KeySpline(0, 0, 0, 1),
                        Setters =
                        {
                            new Setter(MarginProperty, new Thickness(12, 4, 12, 4))
                        }
                    }
                }
            };
        }
    }

    private void OnNavigationViewSelectionChanged(object? sender, NavigationViewSelectionChangedEventArgs e)
    {
        if (e.SelectedItemContainer is NavigationViewItem { Tag: Type pageType })
            _frameView.Navigate(pageType, null, e.RecommendedNavigationTransitionInfo);
    }

    private void OnNavigationViewBackRequested(object? sender, NavigationViewBackRequestedEventArgs e)
    {
        _frameView.GoBack();
    }
}