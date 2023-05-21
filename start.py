import interface
import wx
import os
import sys
import sshconnect
path_to_my_components = os.path.join(os.path.dirname(__file__), 'handlers')
sys.path.append(path_to_my_components)



ssh = None
frame = None
app = wx.App()
frame = interface.MyFrame(None, "CopyGram")
def stop_ssh(event):
    ssh = sshconnect.ssh
    ssh.close()
    frame.Destroy()

frame.Bind(wx.EVT_CLOSE,stop_ssh)
import auth
auth.tab_init(frame)


app.MainLoop()
