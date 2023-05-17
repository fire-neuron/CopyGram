import wx
import Initializer

names = Initializer.language


class TabOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.ftp_host = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), 0)
        bSizer3.Add(self.ftp_host, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.ftp_login = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), 0)
        bSizer3.Add(self.ftp_login, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.ftp_pass = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), wx.TE_PASSWORD)
        bSizer4.Add(self.ftp_pass, 0, wx.ALL, 5)

        # self.show_pass_btn = wx.Button(self, wx.ID_ANY, u"👁️‍🗨️", wx.DefaultPosition, wx.Size(30, -1), 0)
        # bSizer4.Add(self.show_pass_btn, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer11.Add(bSizer3, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        self.ftp_port = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), 0)
        bSizer31.Add(self.ftp_port, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.ftp_start_folder = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(230, -1), 0)
        bSizer31.Add(self.ftp_start_folder, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer41 = wx.BoxSizer(wx.HORIZONTAL)

        self.local_path_scan = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(190, -1), 0)
        bSizer41.Add(self.local_path_scan, 0, wx.ALL, 5)

        self.explorer = wx.Button(self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size(30, -1), 0)
        bSizer41.Add(self.explorer, 0, wx.ALL, 5)

        bSizer31.Add(bSizer41, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer11.Add(bSizer31, 1, wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer1.Add(bSizer11, 1, wx.ALIGN_CENTER, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.read_button = wx.Button(self, wx.ID_ANY, names['FTP_Uploader_Set_button']['read'], wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.read_button, 0, wx.ALL, 5)

        self.write_button = wx.Button(self, wx.ID_ANY, names['FTP_Uploader_Set_button']['write'], wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.write_button, 0, wx.ALL, 5)

        bSizer1.Add(bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP | wx.RIGHT | wx.LEFT, 5)

        self.ftp_host.SetHint(names['FTP_Hints']['ftp_server_adress'])
        self.ftp_pass.SetHint(names['FTP_Hints']['ftp_server_pass'])
        self.ftp_login.SetHint(names['FTP_Hints']['ftp_server_login'])
        self.ftp_port.SetHint(names['FTP_Hints']['ftp_server_port'])
        self.ftp_start_folder.SetHint(names['FTP_Hints']['ftp_server_start_folder'])
        self.local_path_scan.SetHint(names['FTP_Hints']['ftp_folder_for_scan'])


        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
# class TabOne(wx.Panel):
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent)
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         hbox = wx.BoxSizer(wx.HORIZONTAL)
#         hbox2 = wx.BoxSizer(wx.HORIZONTAL)
#         drops = [names['FTP_Uploader_Set']['ftp_server_adress'], names['FTP_Uploader_Set']['ftp_server_login'],
#                  names['FTP_Uploader_Set']['ftp_server_pass'], names['FTP_Uploader_Set']['ftp_server_port'],
#                  names['FTP_Uploader_Set']['ftp_target_folder']]
#
#         self.paths = wx.TextCtrl(self)
#
#         self.paths.SetHint(names['FTP_Uploader_Set']['ftp_listbox_paths_hint'])
#         self.auth_on_ftp = wx.TextCtrl(self)
#
#         hbox.Add(self.auth_on_ftp, flag=wx.ALIGN_LEFT | wx.TOP, border=5, proportion=1)
#         self.FTP_param_comboBox = wx.ComboBox(self, choices=drops, style=wx.CB_DROPDOWN)
#         hbox.Add(self.FTP_param_comboBox, flag=wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
#         self.FTP_param_comboBox.SetHint(names['FTP_Uploader_Set']['ftp_listbox_hint'])
#         self.write_button = wx.Button(self, label=names['FTP_Uploader_Set_button']['write'])
#         self.auth_on_ftp.SetHint(names['FTP_Uploader_Set']['ftp_hint'])
#         hbox.Add(self.write_button, flag=wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
#         vbox.Add(hbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=8)
#
#         hbox2.Add(self.paths, flag=wx.ALIGN_LEFT | wx.RIGHT | wx.TOP, border=5, proportion=1)
#         self.open_explorer_button = wx.Button(self, size=(30, 22), label='...')
#
#         self.set_path_button = wx.Button(self, label=names['FTP_Uploader_Set_button']['write'])
#         self.auth_on_ftp.SetHint(names['FTP_Uploader_Set']['ftp_hint'])
#         hbox2.Add(self.open_explorer_button, flag=wx.ALIGN_LEFT | wx.TOP, border=5)
#         hbox2.Add(self.set_path_button, flag=wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
#         vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=8)
#
#         self.SetSizer(vbox)
#

class TabTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
        vertical_sizer = wx.BoxSizer(wx.VERTICAL)
        self.telegram_set_comboBox = wx.ComboBox(self, choices=[names['TelegramSet']['CbxAdd'],
                                                                names['TelegramSet']['CbxDelete'],
                                                                names['TelegramSet']['Token']], style=wx.CB_DROPDOWN)

        self.telegram_set_comboBox.SetHint(names['TelegramSet']['CxHint'])

        self.telegram_text_ctrl = wx.TextCtrl(self)
        self.telegram_text_ctrl.SetHint(names['TelegramSet']['SetIdHint'])
        horizontal_sizer.Add(self.telegram_text_ctrl, flag=wx.ALIGN_LEFT | wx.TOP, border=5, proportion=1)
        self.set_tg_param_button = wx.Button(self, label=names['TelegramSet']['Btn'])
        self.set_tg_param_button.Enable(False)

        horizontal_sizer.Add(self.telegram_set_comboBox, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM, border=5)
        horizontal_sizer.Add(self.set_tg_param_button, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM, border=5)
        vertical_sizer.Add(horizontal_sizer, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

        exp = wx.StaticText(self, label=names["TelegramSet"]["TelegramListBox"])
        vertical_sizer.Add(exp, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

        self.tg_user_list_ctrl = MyListCtrl(self)

        vertical_sizer.Add(self.tg_user_list_ctrl, 1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

        self.SetSizer(vertical_sizer)


class TabThree(wx.Panel):
    def __init__(self, parent):
        import wx.lib.masked as masked

        wx.Panel.__init__(self, parent)

        self.time_picker = masked.TimeCtrl(self, fmt24hr=True, format='24HHMM', style=wx.TE_LEFT)

        self.explorer = wx.Button(self, size=(30, 22), label="...")
        self.cron_off = wx.Button(self, size=(75, 22), label=names["ServerSet"]["CronOff"])
        self.tracer = wx.Button(self, size=(75, 22), label=names["ServerSet"]["Tracer"])
        self.UploadOnServer = wx.Button(self, label=Initializer.language['ServerSet']['UploadOnServer'])
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        self.path = wx.TextCtrl(self)
        self.path.SetHint(Initializer.language['ServerSet']['UploadOnServerHint'])
        hbox.Add(self.path, 1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)
        hbox.Add(self.explorer, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM, border=5)
        hbox.Add(self.UploadOnServer, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM, border=5)
        vbox.Add(hbox, 0, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)
        line = wx.StaticLine(self)
        vbox.Add(line, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.report = wx.ListCtrl(self, style=wx.LC_LIST)
        self.report.InsertColumn(0, 'report')
        self.report.SetColumnWidth(0, 600)

        # создаём текстовое поле
        exp = wx.StaticText(self, label=names["ServerSet"]["CronSet"])
        self.cron_button = wx.Button(self, label=Initializer.language['ServerSet']['Set'])

        hbox2.Add(exp, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.RIGHT, border=8)
        hbox2.Add(self.time_picker, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM, border=(5))
        hbox2.Add(self.cron_button, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM | wx.LEFT, border=5)
        hbox2.Add(self.cron_off, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM | wx.LEFT, border=5)

        hbox2.AddStretchSpacer()
        hbox2.Add(self.tracer, 0, flag=wx.ALIGN_LEFT | wx.TOP | wx.BOTTOM | wx.LEFT, border=5)

        vbox.Add(hbox2, 0, flag=wx.EXPAND, border=5)

        line2 = wx.StaticLine(self)
        vbox.Add(line2, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        vbox.Add(self.report, 1, flag=wx.EXPAND, border=5)

        self.SetSizer(vbox)


class Auth(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.panel = wx.Panel(self)
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.host_label = wx.StaticText(self.panel, label=Initializer.language['AuthSet']['Address'])
        self.host_entry = wx.TextCtrl(self.panel)
        self.username_label = wx.StaticText(self.panel, label=Initializer.language['AuthSet']['Login'])
        self.username_entry = wx.TextCtrl(self.panel)
        self.password_label = wx.StaticText(self.panel, label=Initializer.language['AuthSet']['Pass'])
        self.password_entry = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
        self.login_button = wx.Button(self.panel, label=Initializer.language['AuthSet']['Auth'])

    def layout_widgets(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.host_label, 0, wx.ALL, 5)
        sizer.Add(self.host_entry, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.username_label, 0, wx.ALL, 5)
        sizer.Add(self.username_entry, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.password_label, 0, wx.ALL, 5)
        sizer.Add(self.password_entry, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.login_button, 0, wx.ALL | wx.CENTER, 5)
        self.panel.SetSizer(sizer)


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 330))
        self.notebook = wx.Notebook(self)

        self.tab_one = TabOne(self.notebook)
        self.tab_two = TabTwo(self.notebook)
        self.tab_three = TabThree(self.notebook)
        # self.tab_one = TabROne(self.notebook)

        self.notebook.AddPage(self.tab_one, names['TabsName']['OneTab'])
        self.notebook.AddPage(self.tab_two, names['TabsName']['TwoTab'])
        self.notebook.AddPage(self.tab_three, names['TabsName']['ThreeTab'])
        # self.notebook.AddPage(self.tab_help, 'test')
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)

        self.SetSizer(sizer)


class MyListCtrl(wx.ListCtrl):
    def __init__(self, parent):
        super().__init__(parent, style=wx.LC_REPORT)
        self.InsertColumn(0, names['TelegramSet']['Id'])
        self.SetColumnWidth(0, 200)
        self.popup_menu = wx.Menu()
