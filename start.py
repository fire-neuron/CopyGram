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
def clear(event):
    stop_ssh(event)
    clear_set()
    frame.Destroy()


def clear_set():

    if not frame.cb.IsChecked():
        import Initializer
        data = Initializer.server_settings
        for key in data.keys():
            for key2 in data[key].keys():
                # Получаем тип значения по ключу
                value_type = type(data[key][key2])
                # Если значение - строка, то присваиваем пустую строку
                if value_type == str:
                    data[key][key2] = ""
                # Если значение - массив, то присваиваем пустой массив
                elif value_type == list:
                    data[key][key2] = []

        Initializer.server_settings['main']['Language'] = 'RU.JSON' #TODO replace this
        Initializer.storeparametr()
def stop_ssh(event):
    ssh = sshconnect.ssh
    ssh.close()


frame.Bind(wx.EVT_CLOSE,clear)
import auth
auth.tab_init(frame)


app.MainLoop()

