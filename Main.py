import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        # hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        # menubar_2 = wx.MenuBar()
        # menu = wx.Menu()
        # items = menu.Append('Invert')
        # menubar_2.Append(menu, '&File')
        # self.SetMenuBar(menubar_2)
        # self.Bind(items)
        # vbox.Add(hbox5, flag=wx.ALIGN_CENTER|wx.EXPAND, border=500)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Invert', 'Darken')
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Darken', 'Darken')
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Solaruze', 'Darken')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
