import os
import sys

path_to_my_components = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_to_my_components)
import Initializer
import SSH_Explorer
import tarfile
import tracer
import ClientNote
import CronSet
import sshconnect
import shutil
program_name = Initializer.program_name
wx = Initializer.wx
settings = Initializer.server_settings
cli_settings = Initializer.client_settings

frame = None


def tab_init(object):
    global frame
    frame = object
    frame.tab_three.explorer.Bind(wx.EVT_BUTTON, on_set_installer_path_button_click)
    frame.tab_three.UploadOnServer.Bind(wx.EVT_BUTTON, installer)
    frame.tab_three.cron_button.Bind(wx.EVT_BUTTON, on_set_cron_button_click)
    frame.tab_three.tracer.Bind(wx.EVT_BUTTON, on_tracer_button_click)
    frame.tab_three.cron_off.Bind(wx.EVT_BUTTON, on_cron_off_button_click)


def on_tracer_button_click(event):
    if  cli_settings['Main']['path_to_program']:
        tracer.run(frame)
    else:
        ClientNote.addstr(Initializer.language['ServerSet']['ProgramNotFound'], frame)


def on_cron_off_button_click(event):
    if CronSet.delete_cron_task():
        ClientNote.addstr(Initializer.language['ServerSet']['CronDeleteOk'], frame)
    else:
        ClientNote.addstr(Initializer.language['ServerSet']['CronDeleteFall'], frame)


def on_set_cron_button_click(event):

    if cli_settings['Main']['path_to_program']:
        hour = frame.tab_three.time_picker.GetWxDateTime().GetHour()
        minute = frame.tab_three.time_picker.GetWxDateTime().GetMinute()

        if CronSet.delete_cron_task() and CronSet.add_cron_task(hour, minute):
            ClientNote.addstr(Initializer.language['TracerReport']['CronOk'], frame)
        else:
            ClientNote.addstr(Initializer.language['TracerReport']['CronFall'], frame)
    else:
        ClientNote.addstr(Initializer.language['ServerSet']['ProgramNotFound'], frame)


def installer(event):

    archive_name = 'CopyGram'
    ssh = sshconnect.ssh
    local_path = program_name

    remote_path = frame.tab_three.path.GetValue()
    Initializer.server_settings['main']['Location'] = remote_path + f'/{program_name}'
    Initializer.storeparametr()
    try:
        base_path = sys._MEIPASS
        source_path_srv = os.path.join(os.path.expanduser("~"), "AppData\\Local\\CopyGram\\settings.json")
        target_path_srv = os.path.join(base_path, program_name, "settings", "settings.json")
        shutil.copyfile(source_path_srv,target_path_srv)
    except:
        pass


    try:
        with tarfile.open(f"{archive_name}.tar", "w") as tar:
            tar.add(local_path)
    except IOError:
        base_path = sys._MEIPASS
        with tarfile.open(f"{archive_name}.tar", "w") as tar:
            tar.add(os.path.join(base_path,local_path),arcname= program_name )



    try:
        sftp = ssh.open_sftp()
        status = sftp.put(f"{archive_name}.tar", remote_path + f"/{archive_name}.tar")
        sftp.close()

        command = f"tar -xf {remote_path}/{archive_name}.tar -C {remote_path}"
        ssh.exec_command(command)

        command = f"rm {remote_path}/{archive_name}.tar"
        ssh.exec_command(command)
        if os.path.exists(f"{archive_name}.tar"):
            os.remove(f"{archive_name}.tar")
        doexe = remote_path + f'/{program_name}' + '/start.py'
        ssh.exec_command('chmod +x ' + doexe)
        ClientNote.addstr(Initializer.language['TracerReport']['InstallOk'], frame)
    except:

        ClientNote.addstr(Initializer.language['TracerReport']['InstallFall'], frame)

    Initializer.client_settings['Main']['path_to_program'] = remote_path + f'/{program_name}'

    Initializer.store_client_parametr()


def on_set_installer_path_button_click(event):
    obj = frame.tab_three
    value = SSH_Explorer.start(frame)
    obj.path.SetValue(value)
