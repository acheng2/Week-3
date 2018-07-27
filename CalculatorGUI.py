import wx


class Calculator(wx.Frame):

    i = ""
    def Operations(self, list1):
        def BinaryToOctal(x):
            b = str(x)
            count = 0
            t = 0
            answer1 = 0
            while 3*count < len(b):
                z = x % 1000
                r = z % 8
                answer1 = r * 10 ** t + answer1
                t = t + 1
                count = count + 1
                x = int(x / 1000)
            self.display.WriteText(str(answer1))

        def BinaryToDecimal(x):
            count = 0
            answer1 = 0
            b = str(x)
            r = 0
            while count <= len(b):
                r = x % 2
                answer1 = r * 2 ** count + answer1
                x = int(x / 10)
                count = count + 1
            self.display.WriteText(str(answer1))

        def BinaryToHexal(x):
            x = str(x)
            [num_bef_dec, num_after_dec] = x.split(".")
            print (num_bef_dec)
            print (num_after_dec)
            output = ""
            output_1 = ""
            count = 0
            side_a = len(num_bef_dec)
            print (side_a)
            side_b = len(num_after_dec)
            print (side_b)

            if side_a % 4 == 1:
                num_bef_dec = num_bef_dec[::-1] + "000"
                num_bef_dec = num_bef_dec[::-1]
                print (num_bef_dec)
            elif side_a % 4 == 2:
                num_bef_dec = num_bef_dec[::-1] + "00"
                num_bef_dec = num_bef_dec[::-1]
            elif side_a % 4 == 3:
                num_bef_dec = num_bef_dec[::-1] + "0"
                num_bef_dec = num_bef_dec[::-1]

            if side_b % 4 == 1:
                num_after_dec = num_after_dec + "000"

            elif side_b % 4 == 2:
                num_after_dec = num_after_dec + "00"

            elif side_b % 4 == 3:
                num_after_dec = num_after_dec + "0"


            for index in range(0, side_a, 4):
                cur_group = num_bef_dec[index:index+4]

                if cur_group == "0000":
                    output = output + "0"
                elif cur_group == "0001":
                    output = output + "1"
                elif cur_group == "0010":
                    output = output + "2"
                elif cur_group == "0011":
                    output = output + "3"
                elif cur_group == "0100":
                    output = output + "4"
                elif cur_group == "0101":
                    output = output + "5"
                elif cur_group == "0110":
                    output = output + "6"
                elif cur_group == "0111":
                    output = output + "7"
                elif cur_group == "1000":
                    output =output + "8"
                elif cur_group == "1001":
                    output = ouput + "9"
                elif cur_group == "1010":
                    output = output + "A"
                elif cur_group == "1011":
                    output = output + "B"
                elif cur_group == "1100":
                    output = output + "C"
                elif cur_group == "1101":
                    output = output + "D"
                elif cur_group == "1110":
                    output = output + "E"
                elif cur_group == "1111":
                    output = output + 'F'

            for index in range(0, side_b, 4):
                cur_group = num_after_dec[index:index+4]

                if cur_group == "0000":
                    output_1 = output_1 + "0"
                elif cur_group == "0001":
                    output_1 = output_1 + "1"
                elif cur_group == "0010":
                    output_1 = output_1 + "2"
                elif cur_group == "0011":
                    output_1 = output_1 + "3"
                elif cur_group == "0100":
                    output_1 = output_1 + "4"
                elif cur_group == "0101":
                    output_1 = output_1 + "5"
                elif cur_group == "0110":
                    output_1 = output_1 + "6"
                elif cur_group == "0111":
                    output_1 = output_1 + "7"
                elif cur_group == "1000":
                    output_1 =output_1 + "8"
                elif cur_group == "1001":
                    output_1 = output_1 + "9"
                elif cur_group == "1010":
                    output_1 = output_1 + "A"
                elif cur_group == "1011":
                    output_1 = output_1 + "B"
                elif cur_group == "1100":
                    output_1 = output_1 + "C"
                elif cur_group == "1101":
                    output_1 = output_1 + "D"
                elif cur_group == "1110":
                    output_1 = output_1 + "E"
                elif cur_group == "1111":
                    output_1 = output_1 + 'F'
            total = output + '.' + output_1
            self.display.WriteText(total)

        def divide(x,y):
            answer1 = x / y
            self.display.WriteText(str(answer1))


        def multiply(x,y):
            answer1 = x * y
            self.display.WriteText(str(answer1))

        def add(x,y):
            answer1 = x + y
            self.display.WriteText(str(answer1))

        def subtract(x,y):
            answer1 = x - y
            self.display.WriteText(str(answer1))

        def Power(x,y):
            answer1 = x ** y
            self.display.WriteText(str(answer1))

        if "+" in list1:
            list1 = list1.split("+")
            add(float(list1[0]), float(list1[-1]))

        if "-" in list1:
            list1 = list1.split("-")
            subtract(float(list1[0]), float(list1[-1]))

        if "/" in list1:
            list1 = list1.split("/")
            divide(float(list1[0]), float(list1[-1]))

        if "*" in list1:
            list1 = list1.split("*")
            multiply(float(list1[0]), float(list1[-1]))

        if "BinToDec" in list1:
            list1 = list1.replace("BinToDec", '')
            BinaryToDecimal(float(list1))

        if "BinToOct" in list1:
            list1 = list1.replace("BinToOct", '')
            BinaryToOctal(float(list1))

        if "BinToHex" in list1:
            list1 = list1.replace("BinToHex", '')
            BinaryToHexal(float(list1))


        if "^" in list1:
            list1 = list1.split("^")
            Power(float(list1[0]), float(list1[-1]))


    def __init__(self, parent, title):
        super(Calculator, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.btn2 = wx.Button(self, label='CC')
        self.btn4 = wx.Button(self, label='^')
        self.btn5 = wx.Button(self, label='Bin to Dec')
        self.btn6 = wx.Button(self, label='7')
        self.btn7 = wx.Button(self, label='8')
        self.btn8 = wx.Button(self, label='9')
        self.btn9 = wx.Button(self, label='/')
        self.btn10 = wx.Button(self, label='Bin to Oct')
        self.btn11 = wx.Button(self, label='4')
        self.btn12 = wx.Button(self, label='5')
        self.btn13 = wx.Button(self, label='6')
        self.btn14 = wx.Button(self, label='*')
        self.btn15 = wx.Button(self, label='Bin to Hex')
        self.btn16 = wx.Button(self, label='1')
        self.btn17 = wx.Button(self, label='2')
        self.btn18 = wx.Button(self, label='3')
        self.btn19 = wx.Button(self, label='-')
        self.btn20 = wx.Button(self, label='0')
        self.btn21 = wx.Button(self, label='.')
        self.btn22 = wx.Button(self, label='=')
        self.btn23 = wx.Button(self, label='+')

        self.btn2.Bind(wx.EVT_BUTTON,self.OnClicked2)
        self.btn4.Bind(wx.EVT_BUTTON,self.OnClicked4)
        self.btn5.Bind(wx.EVT_BUTTON,self.OnClicked5)
        self.btn6.Bind(wx.EVT_BUTTON,self.OnClicked6)
        self.btn7.Bind(wx.EVT_BUTTON,self.OnClicked7)
        self.btn8.Bind(wx.EVT_BUTTON,self.OnClicked8)
        self.btn9.Bind(wx.EVT_BUTTON,self.OnClicked9)
        self.btn10.Bind(wx.EVT_BUTTON,self.OnClicked10)
        self.btn11.Bind(wx.EVT_BUTTON,self.OnClicked11)
        self.btn12.Bind(wx.EVT_BUTTON,self.OnClicked12)
        self.btn13.Bind(wx.EVT_BUTTON,self.OnClicked13)
        self.btn14.Bind(wx.EVT_BUTTON,self.OnClicked14)
        self.btn15.Bind(wx.EVT_BUTTON,self.OnClicked15)
        self.btn16.Bind(wx.EVT_BUTTON,self.OnClicked16)
        self.btn17.Bind(wx.EVT_BUTTON,self.OnClicked17)
        self.btn18.Bind(wx.EVT_BUTTON,self.OnClicked18)
        self.btn19.Bind(wx.EVT_BUTTON,self.OnClicked19)
        self.btn20.Bind(wx.EVT_BUTTON,self.OnClicked20)
        self.btn21.Bind(wx.EVT_BUTTON,self.OnClicked21)
        self.btn22.Bind(wx.EVT_BUTTON,self.OnClicked22)
        self.btn23.Bind(wx.EVT_BUTTON,self.OnClicked23)


        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        gs = wx.GridSizer(5, 5, 5, 5)

        gs.AddMany( [(self.btn2, 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (self.btn6, 0, wx.EXPAND),
            (self.btn7, 0, wx.EXPAND),
            (self.btn8, 0, wx.EXPAND),
            (self.btn9, 0, wx.EXPAND),
            (self.btn4, 0, wx.EXPAND),
            (self.btn11, 0, wx.EXPAND),
            (self.btn12, 0, wx.EXPAND),
            (self.btn13, 0, wx.EXPAND),
            (self.btn14, 0, wx.EXPAND),
            (self.btn5, 0, wx.EXPAND),
            (self.btn16, 0, wx.EXPAND),
            (self.btn17, 0, wx.EXPAND),
            (self.btn18, 0, wx.EXPAND),
            (self.btn19, 0, wx.EXPAND),
            (self.btn10, 0, wx.EXPAND),
            (self.btn20, 0, wx.EXPAND),
            (self.btn21, 0, wx.EXPAND),
            (self.btn22, 0, wx.EXPAND),
            (self.btn23, 0, wx.EXPAND),
            (self.btn15, 0, wx.EXPAND) ])

        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)


    def OnQuit(self, e):
        self.Close()

    def OnClicked2(self, event):
        self.display.Clear()
        c = "CC"
        self.i = ''
    def OnClicked4(self, event):
        self.display.WriteText("^")
        b = "^"
        self.i+=("^")
    def OnClicked5(self, event):
        self.display.WriteText("BinToDec")
        self.i+=("BinToDec")
        d = "Bin to Dec"
    def OnClicked6(self, event):
        self.display.WriteText("7")
        a = 7
        self.i+=("7")
    def OnClicked7(self, event):
        self.display.WriteText("8")
        a = 8
        self.i+=("8")
    def OnClicked8(self, event):
        self.display.WriteText("9")
        a = 9
        self.i+=("9")
    def OnClicked9(self, event):
        self.display.WriteText("/")
        b = "/"
        self.i+=("/")
    def OnClicked10(self, event):
        self.display.WriteText("BinToOct")
        self.i+=("BinToOct")
        d = "Bin to Oct"
    def OnClicked11(self, event):
        self.display.WriteText("4")
        a = 4
        self.i+=("4")
    def OnClicked12(self, event):
        self.display.WriteText("5")
        a = 5
        self.i+=("5")
    def OnClicked13(self, event):
        self.display.WriteText("6")
        a = 6
        self.i+=("6")
    def OnClicked14(self, event):
        self.display.WriteText("*")
        b = "*"
        self.i+=("*")
    def OnClicked15(self, event):
        self.display.WriteText("BinToHex")
        d = "Bin to Hex"
        self.i+=("BinToHex")
    def OnClicked16(self, event):
        self.display.WriteText("1")
        a = 1
        self.i+=("1")
    def OnClicked17(self, event):
        self.display.WriteText("2")
        a = 2
        self.i+=("2")
    def OnClicked18(self, event):
        self.display.WriteText("3")
        a = 3
        self.i+=("3")
    def OnClicked19(self, event):
        self.display.WriteText("-")
        b = "-"
        self.i+=("-")
    def OnClicked20(self, event):
        self.display.WriteText("0")
        a = 0
        self.i+=("0")
    def OnClicked21(self, event):
        self.display.WriteText(".")
        e = "."
        self.i+=("-")
    def OnClicked22(self, event):
        self.display.WriteText("=")
        f = "="
        self.Operations(self.i)
    def OnClicked23(self, event):
        b = "+"
        self.display.WriteText("+")
        self.i+=("+")

def main():

    app = wx.App()
    ex = Calculator(None, title="Angela's Calculator")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
