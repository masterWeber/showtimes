using System;
using System.Threading;
using Avalonia;
using Avalonia.Animation;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;
using Avalonia.Media;
using Avalonia.Styling;

namespace Scheduler.Desktop.Pages;

public partial class SettingsPage : UserControl
{
    private const double AdaptiveTriggerWidth = 665;

    private CancellationTokenSource? _cancellationTokenSource;
    private readonly Control? _headerRightContent;
    private bool _isInSmallMode;

    public SettingsPage()
    {
        InitializeComponent();

        _headerRightContent = this.FindControl<Control>("HeaderRightContent");
    }

    private void InitializeComponent()
    {
        AvaloniaXamlLoader.Load(this);
    }

    protected override void OnPropertyChanged(AvaloniaPropertyChangedEventArgs change)
    {
        base.OnPropertyChanged(change);

        if (change.Property == BoundsProperty) HandleAdaptiveWidth(change.GetNewValue<Rect>().Width);
    }

    private void HandleAdaptiveWidth(double width)
    {
        switch (width)
        {
            case < AdaptiveTriggerWidth when !_isInSmallMode:
                _isInSmallMode = true;
                Grid.SetColumn(_headerRightContent ?? throw new InvalidOperationException(), 0);
                Grid.SetRow(_headerRightContent, 1);
                _headerRightContent.Opacity = 0;

                RunConnectedAnimation(300, -75);
                break;
            case > AdaptiveTriggerWidth when _isInSmallMode:
                _isInSmallMode = false;
                Grid.SetColumn(_headerRightContent ?? throw new InvalidOperationException(), 1);
                Grid.SetRow(_headerRightContent, 0);
                _headerRightContent.Opacity = 0;

                RunConnectedAnimation(-175, 45);
                break;
        }
    }

    private async void RunConnectedAnimation(double startX, double startY)
    {
        _cancellationTokenSource?.Cancel();
        _cancellationTokenSource?.Dispose();
        if (_headerRightContent == null) return;
        _headerRightContent.Opacity = 1;
        _cancellationTokenSource = null;

        var ani = new Animation
        {
            Duration = TimeSpan.FromMilliseconds(167),
            FillMode = FillMode.Forward,
            Children =
            {
                new KeyFrame
                {
                    Cue = new Cue(0d),
                    Setters =
                    {
                        new Setter(OpacityProperty, 0d),
                        new Setter(TranslateTransform.XProperty, startX),
                        new Setter(TranslateTransform.YProperty, startY)
                    }
                },
                new KeyFrame
                {
                    Cue = new Cue(1d),
                    Setters =
                    {
                        new Setter(OpacityProperty, 1d),
                        new Setter(TranslateTransform.XProperty, 0d),
                        new Setter(TranslateTransform.YProperty, 0d)
                    },
                    KeySpline = new KeySpline(0, 0, 0, 1)
                }
            }
        };

        _cancellationTokenSource = new CancellationTokenSource();
        await ani.RunAsync(_headerRightContent, null, _cancellationTokenSource.Token);
        _cancellationTokenSource.Dispose();
        _cancellationTokenSource = null;
        _headerRightContent.Opacity = 1;
    }
}