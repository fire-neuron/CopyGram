
import os
import sys

import sshconnect

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





    frame.tab_one.explorer.Bind(wx.EVT_BUTTON, on_set_scan_folder_click)
    frame.tab_one.write_button.Bind(wx.EVT_BUTTON, on_write_ftp_param_button_click)
    frame.tab_one.read_button.Bind(wx.EVT_BUTTON, on_read_button_click)



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
    lang = Initializer.language

    try:
        obj = frame.tab_one

        sftp = sshconnect.ssh.open_sftp()
        sftp.chdir(obj.local_path_scan.GetValue())
        sftp.close()


        settings['FtpUploader']['host'] = obj.ftp_host.GetValue()

        settings['FtpUploader']['ftp_user'] = obj.ftp_login.GetValue()

        settings['FtpUploader']['ftp_password'] = obj.ftp_pass.GetValue()
        if not obj.ftp_port.GetValue():
            settings['FtpUploader']['ftp_port'] = 21
        else:
            settings['FtpUploader']['ftp_port'] = obj.ftp_port.GetValue()

        settings['FtpUploader']['start_dir'] = obj.ftp_start_folder.GetValue()
        settings['FtpUploader']['folder_for_scan'] = obj.local_path_scan.GetValue()

        Initializer.storeparametr()

        dlg = wx.MessageDialog(frame.tab_one,
                               lang['FTP_Uploader_Set']['WriteOk'], 'OK',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    except IOError:
        dlg = wx.MessageDialog(frame.tab_one,
                               lang['errors']['FailedToScanFolder'], 'Oops',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        sftp.close()
    except:
        dlg = wx.MessageDialog(frame.tab_one,
                               lang['FTP_Uploader_Set']['WriteFall'], 'Oops',
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
