using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace Scheduler.Desktop.Pages
{
    public partial class MoviesPage : UserControl
    {
        public MoviesPage()
        {
            InitializeComponent();
        }

        private void InitializeComponent()
        {
            AvaloniaXamlLoader.Load(this);
        }
    }
}