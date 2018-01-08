import wx
import wx.adv

class SystemTray:
    """ Manage the system tray """
    def __init__(self):
        self.tooltip_text = "Stand Now!"
        self.icon_file = "img/icon.png"

        self.systray = wx.adv.TaskBarIcon()
        self.systray_icon = wx.Icon(self.icon_file)

        self.systray.SetIcon(self.systray_icon, tooltip=self.tooltip_text)

    def update_tooltip(self):
        """ Update the system tray tooltip text """
        pass

def main():
    """ Insert docstring here """
    app = wx.App()

    systray = SystemTray()

    app.MainLoop()

main()
