﻿using System;
using Scheduler.Desktop.Services;
using Scheduler.Desktop.Utilities;

namespace Scheduler.Desktop.ViewModels
{
    public class FAControlsItem
    {
        public FAControlsItem()
        {
            InvokeCommand = new FACommand(OnInvokeCommandExecute);
        }

        public string Header { get; set; }

        public string Description { get; set; }

        public string PreviewImageSource { get; set; }

        public string PageType { get; init; }

        public FACommand InvokeCommand { get; }

        private void OnInvokeCommandExecute(object parameter)
        {
            var type = Type.GetType($"FluentAvaloniaSamples.Pages.{PageType}");
            NavigationService.Instance.Navigate(type);
        }
    }
}