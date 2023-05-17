
import os
import sys
path_to_my_components = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_to_my_components)
import interface
import Initializer
import sshconnect
wx = Initializer.wx
ssh = None
turn = True

settings = Initializer.server_settings

frame = None

def closeme(event):
    auth.Destroy()
    if turn:
        frame.Destroy()

def tab_init(object):
    global frame
    frame = object
    auth.Bind(wx.EVT_CLOSE,closeme)

    auth.login_button.Bind(wx.EVT_BUTTON, on_login_button)
    auth.Show()
    # fill()


def on_login_button(event):
    global frame
    global ssh
    global turn

    host = auth.host_entry.GetValue()
    username = auth.username_entry.GetValue()
    password = auth.password_entry.GetValue()

    try:
        ssh = sshconnect.open_session(host=host, username=username,
                                        password=password)
        turn = False
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
