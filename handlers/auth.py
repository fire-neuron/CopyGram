
import os
import sys
path_to_my_components = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_to_my_components)
import interface
import Initializer
import sshconnect
import threading
ConnectToSSH = None
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
    global ConnectToSSH
    frame = object
    auth.Bind(wx.EVT_CLOSE,closeme)

    auth.login_button.Bind(wx.EVT_BUTTON, on_login_button)
    Initializer.get_frame(frame)
    auth.Show()
    ConnectToSSH = threading.Thread(target=TryToConnect)

def CheckButtonSet():
    state = Initializer.client_settings['Main']['SetLocal']
    frame.cb.SetValue(state)


def onCheckBox(event):
        Initializer.client_settings['Main']['SetLocal'] = frame.cb.IsChecked()
        Initializer.store_client_parametr()



def cont():
    Initializer.load_settings()
    CheckButtonSet()
    frame.cb.Bind(wx.EVT_CHECKBOX, onCheckBox)
    import tab_one
    tab_one.tab_init(frame)
    import tab_two
    tab_two.tab_init(frame)
    import tab_three
    tab_three.tab_init(frame)
def TryToConnect():
    global ConnectToSSH
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
        cont()
        frame.Show()



    except:
        auth.status.SetLabel(Initializer.language["AuthSet"]["NotConnecting"])
        ConnectToSSH = threading.Thread(target=TryToConnect)





def on_login_button(event):
    global ConnectToSSH

    if not ConnectToSSH.is_alive():
        ConnectToSSH.start()
        auth.status.SetLabel(Initializer.language["AuthSet"]["Connecting"])







auth = interface.Auth(None, interface.names['AuthSet']['Title'])
