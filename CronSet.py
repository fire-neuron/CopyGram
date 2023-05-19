import sshconnect
import Initializer
import time

client_settings = Initializer.client_settings



def delete_cron_task():
    ssh = sshconnect.ssh
    stdin, stdout, stderr = ssh.exec_command('crontab -l | grep -v "start.py" | crontab -')
    if stderr.read().decode('utf-8'):
        return False
    else:
        return True


def add_cron_task(hour='*', minute='*'):
    ssh = sshconnect.ssh
    path = Initializer.client_settings['Main']['path_to_program'] + '/start.py'

    if hour == '*' and minute == '*':
        test_mode = " -a t"
    else:
        test_mode = ''
    try:
        stdin, stdout, stderr = ssh.exec_command('crontab -l')
        curent_cron = stdout.read().decode('utf-8')
        cron_task = curent_cron + f"{hour} {minute} * * * /usr/bin/python3 {path}{test_mode}\n"
        stdin, stdout, stderr = ssh.exec_command('crontab -')
        stdin.write(cron_task)
        stdin.flush()
        return True
    except:
        return False

def delete_back():
    ssh = sshconnect.ssh
    n = 10
    path = Initializer.client_settings['Main']['path_to_program'] + '/CronBack'
    print(path)
    sftp = ssh.open_sftp()
    files = sftp.listdir(path)
    file_count = len(files)
    if file_count >= n:
        files = sftp.listdir_attr(path)
        files.sort(key = lambda f: f.st_mtime)
        earliest = files[0]
        command = f"rm {path}/{earliest.filename}"
        ssh.exec_command(command)



def BackupCron():
    ssh = sshconnect.ssh
    delete_back()
    timepin = str(time.time()).replace('.', 'S')
    path = Initializer.client_settings['Main']['path_to_program'] + '/CronBack'
    backup_file = f'{path}/crontab{timepin}.bak'
    stdin, stdout, stderr = ssh.exec_command(f'crontab -l > {backup_file}')

    if stderr.read().decode('utf-8'):
        return False
    else:
        return True
