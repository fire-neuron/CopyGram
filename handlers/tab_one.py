
import os
import sys
path_to_my_components = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_to_my_components)
import Initializer
import SSH_Explorer


wx = Initializer.wx
settings = Initializer.server_settings

frame = None


def tab_init(object):
    global frame
    frame = object




    # frame.tab_one.show_pass_btn.Bind(wx.EVT_BUTTON, on_show_pass_btn_click)
    frame.tab_one.explorer.Bind(wx.EVT_BUTTON, on_set_scan_folder_click)
    frame.tab_one.write_button.Bind(wx.EVT_BUTTON, on_write_ftp_param_button_click)
    frame.tab_one.read_button.Bind(wx.EVT_BUTTON, on_read_button_click)

# def on_show_pass_btn_click(event):
#     text = frame.tab_one.ftp_pass
#     if text.GetWindowStyleFlag() == 2048:
#         text.SetWindowStyleFlag(0)
#     else:
#         text.SetWindowStyleFlag(wx.TE_PASSWORD)
#     text.Refresh()

def on_read_button_click(event):
    obj = frame.tab_one
    obj.ftp_host.SetValue(settings['FtpUploader']['host'])
    obj.ftp_login.SetValue(settings['FtpUploader']['ftp_user'])
    obj.ftp_pass.SetValue(settings['FtpUploader']['ftp_password'])
    obj.ftp_port.SetValue(settings['FtpUploader']['ftp_port'])
    obj.ftp_start_folder.SetValue(settings['FtpUploader']['start_dir'])
    obj.local_path_scan.SetValue(settings['FtpUploader']['folder_for_scan'])






def on_set_scan_folder_click(event):
    obj = frame.tab_one
    value = SSH_Explorer.start(frame)
    obj.local_path_scan.SetValue(value)






def on_write_ftp_param_button_click(event):
    obj = frame.tab_one

    settings['FtpUploader']['host'] = obj.ftp_host.GetValue()

    settings['FtpUploader']['ftp_user'] = obj.ftp_login.GetValue()

    settings['FtpUploader']['ftp_password'] = obj.ftp_pass.GetValue()

    settings['FtpUploader']['ftp_port'] = obj.ftp_port.GetValue()

    settings['FtpUploader']['start_dir'] = obj.ftp_start_folder.GetValue()
    settings['FtpUploader']['folder_for_scan'] = obj.local_path_scan.GetValue()

    Initializer.storeparametr()
