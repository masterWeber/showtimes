using System;
using Avalonia.Controls;
using FluentAvalonia.UI.Controls;

namespace Scheduler.Desktop.Services;

public class NavigationService
{
    private Frame? _frame;
    private Panel? _overlayHost;

    public static NavigationService Instance { get; } = new();

    public void SetFrame(Frame f)
    {
        _frame = f;
    }

    public void SetOverlayHost(Panel p)
    {
        _overlayHost = p;
    }

    public void Navigate(Type t)
    {
        _frame?.Navigate(t);
    }

    public void ClearOverlay()
    {
        _overlayHost?.Children.Clear();
    }
}