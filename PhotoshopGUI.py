import wx
   2
   3 class PromptingComboBox(wx.ComboBox) :
   4     def __init__(self, parent, value, choices=[], style=0, **par):
   5         wx.ComboBox.__init__(self, parent, wx.ID_ANY, value, style=style|wx.CB_DROPDOWN, choices=choices, **par)
   6         self.choices = choices
   7         self.Bind(wx.EVT_TEXT, self.EvtText)
   8         self.Bind(wx.EVT_CHAR, self.EvtChar)
   9         self.Bind(wx.EVT_COMBOBOX, self.EvtCombobox)
  10         self.ignoreEvtText = False

  12     def EvtCombobox(self, event):
  13         self.ignoreEvtText = True
  14         event.Skip()
  15
  16     def EvtChar(self, event):
  17         if event.GetKeyCode() == 8:
  18             self.ignoreEvtText = True
  19         event.Skip()
  20
  21     def EvtText(self, event):
  22         if self.ignoreEvtText:
  23             self.ignoreEvtText = False
  24             return
  25         currentText = event.GetString()
  26         found = False
  27         for choice in self.choices :
  28             if choice.startswith(currentText):
  29                 self.ignoreEvtText = True
  30                 self.SetValue(choice)
  31                 self.SetInsertionPoint(len(currentText))
  32                 self.SetMark(len(currentText), len(choice))
  33                 found = True
  34                 break
  35         if not found:
  36             event.Skip()
  37
  38 class TrialPanel(wx.Panel):
  39     def __init__(self, parent):
  40         wx.Panel.__init__(self, parent, wx.ID_ANY)
  41
  42         choices = ['grandmother', 'grandfather', 'cousin', 'aunt', 'uncle', 'grandson', 'granddaughter']
  43         for relative in ['mother', 'father', 'sister', 'brother', 'daughter', 'son']:
  44             choices.extend(self.derivedRelatives(relative))
  45
  46         cb = PromptingComboBox(self, "default value", choices, style=wx.CB_SORT)
  47
  48     def derivedRelatives(self, relative):
  49         return [relative, 'step' + relative, relative + '-in-law']
  50
  51
  52 if __name__ == '__main__':
  53     app = wx.App()
  54     frame = wx.Frame (None, -1, 'Demo PromptingComboBox Control', size=(400, 50))
  55     TrialPanel(frame)
  56     frame.Show()
  57     app.MainLoop()
