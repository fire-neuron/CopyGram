
import os
import sys
path_to_my_components = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_to_my_components)
import interface
import Initializer
import sshconnect
wx = Initializer.wx
ssh = None
<<<<<<< HEAD
=======
turn = True
>>>>>>> 05e8314 (Initial commit)

settings = Initializer.server_settings

frame = None

<<<<<<< HEAD
=======
def closeme(event):
    auth.Destroy()
    if turn:
        frame.Destroy()
>>>>>>> 05e8314 (Initial commit)

def tab_init(object):
    global frame
    frame = object
<<<<<<< HEAD

    auth.login_button.Bind(wx.EVT_BUTTON, on_login_button)
    auth.Show()
    fill()
=======
    auth.Bind(wx.EVT_CLOSE,closeme)

    auth.login_button.Bind(wx.EVT_BUTTON, on_login_button)
    auth.Show()
    # fill()
>>>>>>> 05e8314 (Initial commit)


def on_login_button(event):
    global frame
    global ssh
<<<<<<< HEAD
=======
    global turn
>>>>>>> 05e8314 (Initial commit)

    host = auth.host_entry.GetValue()
    username = auth.username_entry.GetValue()
    password = auth.password_entry.GetValue()

    try:
        ssh = sshconnect.open_session(host=host, username=username,
<<<<<<< HEAD
                                          password=password)
=======
                                        password=password)
        turn = False
>>>>>>> 05e8314 (Initial commit)
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
