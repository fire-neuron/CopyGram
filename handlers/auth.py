
import os
import sys
path_to_my_components = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_to_my_components)
import interface
import Initializer
import sshconnect
wx = Initializer.wx
ssh = None

settings = Initializer.server_settings

frame = None


def tab_init(object):
    global frame
    frame = object

    auth.login_button.Bind(wx.EVT_BUTTON, on_login_button)
    auth.Show()
    fill()


def on_login_button(event):
    global frame
    global ssh

    host = auth.host_entry.GetValue()
    username = auth.username_entry.GetValue()
    password = auth.password_entry.GetValue()

    try:
        ssh = sshconnect.open_session(host=host, username=username,
                                          password=password)
        auth.Close()
        frame.Show()



    except:
        dlg = wx.MessageDialog(auth.panel,
                               'Access Denied', 'oops',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


def fill():
    auth.host_entry.SetValue('')
    auth.username_entry.SetValue('')
    auth.password_entry.SetValue('')


auth = interface.Auth(None, interface.names['AuthSet']['Title'])
