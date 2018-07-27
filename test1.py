import wx

class Example(wx.Frame):
    def apply_filter(image,filter):
        pixels = [filter(p) for p in image.getdata()]
        nim = Image.new('RGB', image.size)
        nim.putdata(pixels)
        return nim

    def open_image(filename):
        image = Image.open(filename)
        if image == None:
            print ("Specified Input file " + filename + "cannot be opened")
            return Image.new('RBG', image.size)

        else:
            print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
            return image.convert("RGB")


    def invert(pixel):

        r,g,b = pixel
        return (255-r, 255-g, 255-b)

    def darken(pixel):

        r,g,b = pixel
        return (int(.5 * r), int(.5 * g), int(.5 * b))

    def brighten(pixel):
        r,g,b = pixel
        return (int(1.5 * r), int(1.5 * g), int(1.5 * b))

    def gray_scale(pixel):
        r,g,b = pixel
        x = (r + g + b) / 3
        return (int(x),int(x),int(x))

    def posterize(pixel):
        r,g,b = pixel
        if r >= 0 and r<= 63:
            r = 50
        elif r >= 64 and r<= 127:
            r = 100
        elif r >= 128 and r<= 191:
            r = 150
        elif r >= 192 and r<=255:
            r = 200

        if g >= 0 and g <= 63:
            g = 50
        elif g >= 64 and g <= 127:
            g = 100
        elif g >= 128 and g <= 191:
            g = 150
        elif g >= 192 and g <=255:
            g = 200

        if b >= 0 and b <= 63:
            b = 50
        elif b >= 64 and b <= 127:
            b = 100
        elif b >= 128 and b <= 191:
            b = 150
        elif b >= 192 and b <=255:
            b = 200
        return (r,g,b)

    def solarize(pixel):

        r,g,b = pixel
        if r < 128:
            r = 255 - r
        if g < 128:
            g = 255 - g
        if b < 128:
            b = 255 - b
        return(r,g,b)

    def crop(image,coordinates):
        crop = image.crop(coordinates)
        image.show()
        crop.show()
        crop.save("processedImage.jpg")
        return (crop)

    def blur(image,radius):
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
        image.show()
        blurred_image.show()
        blurred_image.save("processedImage.jpg")

    def sharpen(image):
        inpt_radius = eval(input("What radius would you like?(Choose number 1 - 3): "))
        inpt_percent = eval(input("What percentage would you like?(Choose a number 100 - 300): "))
        inpt_threshold = eval(input("What threshold would you like?(Choose a number from 3 - 5): "))
        sharpened_image = image.filter(ImageFilter.UnsharpMask(radius = int(inpt_radius), percent = int(inpt_percent), threshold = int(inpt_threshold)))
        image.show()
        sharpened_image.show()
        sharpened_image.save("processedImage.jpg")





    def load_and_go (fname,filterfunc):
        image = open_image(fname)
        nimage = apply_filter(image,filterfunc)
        image.show()
        nimage.show()
        nimage.save("processedImage.jpg")




    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size = (1050,700))

        self.InitUI()
        self.Centre()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)

        font.SetPointSize(9)


        #btn_invert = (wx.Button(self,label = "Invert"))
        #btn_gray_scale = (wx.Button(self,label = "Black And White"))
        #btn_posterize = (wx.Button(self, label = "Posterize"))
        # btn_solarize = (wx.Button(self, label = 'Solarize' ))
        # btn_darken = (wx.Button(self, label = 'Darken'))
        # btn_brighten = (wx.Button(self, label = 'Brigten'))
        # btn_crop = (wx.Button(self, label = 'Crop'))
        # btn_blur = (wx.Button(self, label = 'Blur'))
        # btn_sharpen = (wx.Button(self, label = 'Darken'))

        # self.Bind(wx.EVT_BUTTON,self.OnButtonInvert, btn_invert)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonGrayScale, btn_gray_scale)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonPosterize, btn_posterize)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonSolarize, btn_solarize)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonDarken, btn_darken)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonBrighten, btn_brighten)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonCrop, btn_crop)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonBlur, btn_blur)
        # self.Bind(wx.EVT_BUTTON,self.OnButtonSharpen, btn_sharpen)



        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        open_btn = wx.Button(panel, label='Open', size=(70, 24))
        hbox1.Add(open_btn)
        tc = wx.TextCtrl(panel)
        hbox1.Add(tc, proportion=1000000)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=20)

        vbox.Add((-1, 15))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)
        tc21 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox3.Add(tc21, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
            border=10)

        vbox.Add((-1, 25))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='Original Image', style=wx.ALIGN_CENTER)
        st2.SetFont(font)
        hbox2.Add(st2, wx.EXPAND)

        st22 = wx.StaticText(panel, label='Filtered Image', style=wx.ALIGN_CENTER)
        st22.SetFont(font)
        hbox2.Add(st22, wx.EXPAND)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.EXPAND)

        vbox.Add((-1, 10))


        vbox.Add((-1, 10))



        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        menubar_2 = wx.MenuBar()
        Menu = wx.Menu()
        item = fileMenu.Append(wx.EVT_HANDLER, 'Invert', 'Darken')
        item = fileMenu.Append(wx.EVT_HANDLER, 'Darken', 'Darken')
        item = fileMenu.Append(wx.ID_EXIT, 'Brighten', 'Darken')
        item = fileMenu.Append(wx.ID_EXIT, 'Black and White', 'Darken')
        item = fileMenu.Append(wx.ID_EXIT, 'Posterize', 'Darken')
        item = fileMenu.Append(wx.ID_EXIT, 'Solarize', 'Darken')
        item = fileMenu.Append(wx.ID_EXIT, 'Blur', 'Darken')
        item = fileMenu.Append(wx.ID_EXIT, 'Sharpen', 'Darken')
        item = fileMenu.Append(wx.ID_EXIT, 'Crop', 'Darken')

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnButtonInvert, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonGrayScale, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonPosterize, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonSolarize, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonPosterize, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonDarken, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonBrighten, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonCrop, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonBlur, fileItem)
        self.Bind(wx.EVT_MENU, self.OnButtonSharpen, fileItem)



        panel.SetSizer(vbox)

    def OnQuit(self, e):
        self.Close()

    def OnButtonInvert(self,event):
        self.load_and_go(input_filename,invert)
        self.invert(pixel)

    def OnButtonGrayScale(self,event):
        self.load_and_go(input_filename,gray_scale)
        self.gray_scale(pixel)

    def OnButtonPosterize(self,event):
        self.load_and_go(input_filename,posterize)
        self.posterize(pixel)

    def OnButtonSolarize(self,event):
        self.load_and_go(input_filename,solarize)
        self.solarize(pixel)

    def OnButtonDarken(self,event):
        self.load_and_go(input_filename,darken)
        self.darken(pixel)

    def OnButtonBrighten(self,event):
        self.load_and_go(input_filename,brighten)
        self.brighten(pixel)

    def OnButtonCrop(self,event):
        self.crop(image)

    def OnButtonBlur(self,event):
        self.load_and_go(input_filename,invert)
        self.blur(image)

    def OnButtonSharpen(self,event):
        self.sharpen(image)

def main():

    app = wx.App()
    ex = Example(None, title='Photoshop')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
