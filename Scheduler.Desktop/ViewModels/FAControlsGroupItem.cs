using System.Collections.Generic;

namespace Scheduler.Desktop.ViewModels
{
    public class FAControlsGroupItem
    {
        public string Header { get; set; }

        public List<FAControlsItem> Controls { get; init; }
    }
}