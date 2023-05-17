import os
import wx
import sshconnect
import Initializer
Dialog = None
names = Initializer.language



class FileExplorer(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, title="SSH_Explorer", style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.ssh = sshconnect.ssh
        self.sftp = self.ssh.open_sftp()

        self.current_folder_path = '/home'

        self.create_ui()

    def create_ui(self):
        panel = wx.Panel(self)

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.current_folder_text = wx.TextCtrl(panel)
        self.hbox.Add(self.current_folder_text, 1, wx.ALIGN_LEFT | wx.ALL, 5)


        self.button = wx.Button(panel, label=names['FTP_Uploader_Set_button']['Set'])
        self.hbox.Add(self.button, 0, wx.ALIGN_LEFT | wx.ALL, 5)


        self.vbox.Add(self.hbox, flag=wx.EXPAND)


        self.list_box = wx.ListBox(panel)
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        self.list_box.Bind(wx.EVT_LISTBOX_DCLICK, self.on_list_box_dclick)  # Добавляем обработчик событий
        self.update_file_list()

        self.vbox.Add(self.list_box, 1, wx.EXPAND | wx.ALL, 5)



        panel.SetSizer(self.vbox)
        self.ShowModal()


    def on_button_click(self,event):

        try:
            self.sftp.chdir(self.current_folder_text.LabelText)
            self.value = self.current_folder_text.GetValue()  # получает значение из текстового поля
            self.EndModal(0)




        except:
            dlg = wx.MessageDialog(self,"Invalid directory name. Try again.","Oops" ,wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def update_file_list(self):
        self.list_box.Clear()
        self.list_box.Append('..')
        file_list = self.sftp.listdir(self.current_folder_path)
        for file_name in file_list:
            self.list_box.Append(file_name)

    def on_list_box_dclick(self, event):
        selection = self.list_box.GetStringSelection()

        if selection == '..':
            self.current_folder_path = self.current_folder_path.rsplit('/', 1)[0]
        else:
            self.current_folder_path = self.current_folder_path + '/' + selection
        try:
            self.sftp.chdir(self.current_folder_path)
            current_folder_path = self.current_folder_path
            self.update_file_list()
            self.current_folder_text.SetLabel(self.current_folder_path)
        except:
            self.current_folder_text.SetLabel("Invalid directory name. Try again.")



def start(parent):
    global Dialog

    Dialog = FileExplorer(parent)
    Dialog.sftp.close()
    if Dialog.GetReturnCode() == 0:
        value = Dialog.value
        Dialog.Destroy()
        return value
    Dialog.Destroy()
    return ''







