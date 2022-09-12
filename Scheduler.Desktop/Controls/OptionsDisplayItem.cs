using System;
using System.Windows.Input;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Primitives;
using Avalonia.Input;
using Avalonia.Interactivity;
using FluentAvalonia.UI.Controls;

namespace Scheduler.Desktop.Controls;

public class OptionsDisplayItem : TemplatedControl
{
    public static readonly StyledProperty<string> HeaderProperty =
        AvaloniaProperty.Register<OptionsDisplayItem, string>(nameof(Header));

    public static readonly StyledProperty<string> DescriptionProperty =
        AvaloniaProperty.Register<OptionsDisplayItem, string>(nameof(Description));

    public static readonly StyledProperty<FAIconElement> IconProperty =
        AvaloniaProperty.Register<OptionsDisplayItem, FAIconElement>(nameof(Icon));

    public static readonly StyledProperty<bool> NavigatesProperty =
        AvaloniaProperty.Register<OptionsDisplayItem, bool>(nameof(Navigates));

    public static readonly StyledProperty<IControl> ActionButtonProperty =
        AvaloniaProperty.Register<OptionsDisplayItem, IControl>(nameof(ActionButton));

    public static readonly StyledProperty<bool> ExpandsProperty =
        AvaloniaProperty.Register<OptionsDisplayItem, bool>(nameof(Expands));

    public static readonly StyledProperty<object?> ContentProperty =
        ContentControl.ContentProperty.AddOwner<OptionsDisplayItem>();

    public static readonly DirectProperty<OptionsDisplayItem, bool> IsExpandedProperty =
        Expander.IsExpandedProperty.AddOwner<OptionsDisplayItem>(x => x.IsExpanded, (x, v) => x.IsExpanded = v);

    private static readonly StyledProperty<ICommand> NavigationCommandProperty =
        AvaloniaProperty.Register<OptionsDisplayItem, ICommand>(nameof(NavigationCommand));

    private static readonly RoutedEvent<RoutedEventArgs> NavigationRequestedEvent =
        RoutedEvent.Register<OptionsDisplayItem, RoutedEventArgs>(nameof(NavigationRequested),
            RoutingStrategies.Bubble);

    private bool _isExpanded;
    private bool _isPressed;
    private Border? _layoutRoot;

    public string Header
    {
        get => GetValue(HeaderProperty);
        set => SetValue(HeaderProperty, value);
    }

    public string Description
    {
        get => GetValue(DescriptionProperty);
        set => SetValue(DescriptionProperty, value);
    }

    public FAIconElement Icon
    {
        get => GetValue(IconProperty);
        set => SetValue(IconProperty, value);
    }

    public bool Navigates
    {
        get => GetValue(NavigatesProperty);
        set => SetValue(NavigatesProperty, value);
    }

    public IControl ActionButton
    {
        get => GetValue(ActionButtonProperty);
        set => SetValue(ActionButtonProperty, value);
    }

    public bool Expands
    {
        get => GetValue(ExpandsProperty);
        set => SetValue(ExpandsProperty, value);
    }

    public object? Content
    {
        get => GetValue(ContentProperty);
        set => SetValue(ContentProperty, value);
    }

    public bool IsExpanded
    {
        get => _isExpanded;
        set => SetAndRaise(IsExpandedProperty, ref _isExpanded, value);
    }

    public ICommand NavigationCommand
    {
        get => GetValue(NavigationCommandProperty);
        set => SetValue(NavigationCommandProperty, value);
    }

    public event EventHandler<RoutedEventArgs> NavigationRequested
    {
        add => AddHandler(NavigationRequestedEvent, value);
        remove => RemoveHandler(NavigationRequestedEvent, value);
    }

    protected override void OnPropertyChanged(AvaloniaPropertyChangedEventArgs change)
    {
        base.OnPropertyChanged(change);

        if (change.Property == NavigatesProperty)
        {
            if (Expands)
                throw new InvalidOperationException("Control cannot both Navigate and Expand");

            PseudoClasses.Set(":navigates", change.GetNewValue<bool>());
        }
        else if (change.Property == ExpandsProperty)
        {
            if (Navigates)
                throw new InvalidOperationException("Control cannot both Navigate and Expand");

            PseudoClasses.Set(":expands", change.GetNewValue<bool>());
        }
        else if (change.Property == IsExpandedProperty)
        {
            PseudoClasses.Set(":expanded", change.GetNewValue<bool>());
        }
        else if (change.Property == IconProperty)
        {
            PseudoClasses.Set(":icon", change.NewValue != null);
        }
    }

    protected override void OnApplyTemplate(TemplateAppliedEventArgs e)
    {
        base.OnApplyTemplate(e);

        _layoutRoot = e.NameScope.Find<Border>("LayoutRoot");
        if (_layoutRoot == null) return;

        _layoutRoot.PointerPressed += OnLayoutRootPointerPressed;
        _layoutRoot.PointerReleased += OnLayoutRootPointerReleased;
        _layoutRoot.PointerCaptureLost += OnLayoutRootPointerCaptureLost;
    }

    private void OnLayoutRootPointerPressed(object? sender, PointerPressedEventArgs e)
    {
        if (e.GetCurrentPoint(this).Properties.PointerUpdateKind != PointerUpdateKind.LeftButtonPressed) return;

        _isPressed = true;
        PseudoClasses.Set(":pressed", true);
    }

    private void OnLayoutRootPointerReleased(object? sender, PointerReleasedEventArgs e)
    {
        var pt = e.GetCurrentPoint(this);
        if (!_isPressed || pt.Properties.PointerUpdateKind != PointerUpdateKind.LeftButtonReleased) return;

        _isPressed = false;

        PseudoClasses.Set(":pressed", false);

        if (Expands)
            IsExpanded = !IsExpanded;

        if (!Navigates) return;

        RaiseEvent(new RoutedEventArgs(NavigationRequestedEvent, this));
        NavigationCommand.Execute(null);
    }

    private void OnLayoutRootPointerCaptureLost(object? sender, PointerCaptureLostEventArgs e)
    {
        _isPressed = false;
        PseudoClasses.Set(":pressed", false);
    }
}