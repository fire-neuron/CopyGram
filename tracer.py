import sshconnect
import Initializer
import time
import threading

names = Initializer.language
server_settings = Initializer.server_settings
client_settings = Initializer.client_settings

frame = None
ssh = None


def run(fr):

    global frame, ssh
    frame = fr
    ssh = sshconnect.ssh
    try:
        ssh.exec_command('ls', timeout=3)
    except:
        addstr(Initializer.language['errors']['ConnectionFailed'])
        return
    python_check()
    availability_check()
    check_net_thread = threading.Thread(target=check_network)
    check_net_thread.start()


def cronStart():
    import CronSet

    if CronSet.BackupCron():
        if CronSet.add_cron_task():
            addstr(Initializer.language['TracerReport']['CronOk'])


        else:
            addstr(Initializer.language['TracerReport']['CronFall'])

    else:
        addstr(Initializer.language['TracerReport']['CronBackFall'])


def addstr(line):
    frame.tab_three.report.InsertItem(frame.tab_three.report.GetItemCount(), line)


def check_network():
    path = client_settings["Main"]["path_to_program"] + '/NetWorkTest.py'
    stdin, stdout, stderr = ssh.exec_command('python3 ' + path)
    output = stdout.read().decode('utf-8').strip()
    if output:
        if output == 'NotConnect':
            addstr(Initializer.language['TracerReport']['TelegramNetFall'])
        if output == 'Unauthorized':
            addstr(Initializer.language['TracerReport']['TelegramUnAuth'])
        if output == 'True':
            addstr(Initializer.language['TracerReport']['TelegramCheckOk'])
            cronStart()
            check_file_thread = threading.Thread(target=get_remote_report)
            check_file_thread.start()




def check_script_location():
    ssh = sshconnect.ssh
    path = client_settings["Main"]["path_to_program"] + '/start.py'
    report = frame.tab_three.report

    # Выполнение команды ls и получение вывода
    stdin, stdout, stderr = ssh.exec_command('ls ' + path)

    # Проверка наличия папки в выводе
    output = stdout.read().decode('utf-8').strip()

    addstr(names['TracerReport']['AvailabilityCheck'])

    if 'start.py' in output:
        addstr(names['TracerReport']['AvailabilityOK'])
        addstr(f"{names['TracerReport']['AvailabilityAdress']}{path}")
        return True
    else:
        addstr(f"{names['TracerReport']['AvailabilityFall']}")
        addstr(f"{names['TracerReport']['AvailabilityAdress']}{path}")
        return False


def get_remote_report():
    content = ''
    sftp = ssh.open_sftp()
    path = client_settings["Main"]["path_to_program"] + '/report/TestReport.txt'
    addstr(names['TracerReport']['GetReportPromt'])
    timer = 1
    files = sftp.listdir(client_settings["Main"]["path_to_program"] + '/report/')
    if 'TestReport.txt' in files:
        remote_file_path = path
        sftp.remove(remote_file_path)

    while True:
        files = sftp.listdir(client_settings["Main"]["path_to_program"] + '/report/')
        if timer > 59:
            addstr(names['TracerReport']['GetReportFall'])
            break
        if 'TestReport.txt' not in files:
            time.sleep(1)
            timer += 1
            continue

        with sftp.open(path, 'r') as f:
            content = f.read().decode('utf-8')

        decoded_text = content.encode('utf-8').decode('unicode-escape')
        addstr(names['TracerReport']['GetReportOK'])
        decoded_text = decoded_text.splitlines()
        for line in decoded_text:
            addstr(line.strip('"').strip())
        remote_file_path = path
        sftp.remove(remote_file_path)
        break
    sftp.close()


def python_check():
    stdin, stdout, stderr = ssh.exec_command('python3 -c "print(\'OK\')"')
    output = stdout.read().decode()
    error = stderr.read().decode()
    addstr(names['TracerReport']['SeekPython'])
    if not error:
        stdin, stdout, stderr = ssh.exec_command('python3 --version')
        output = stdout.read().decode()

        addstr(f"{names['TracerReport']['PythonDetected']}{output}")

    else:
        addstr(f"{names['TracerReport']['PythonFall']}{error}")
        raise


def availability_check():
    if not check_script_location():
        raise
    path = client_settings["Main"]["path_to_program"] + '/TestFolder'
    stdin, stdout, stderr = ssh.exec_command('ls ' + path)
    output = stdout.read().decode('utf-8').strip()
    addstr(names['TracerReport']['ContentFind'])

    if 'Must_Send.test' in output:
        output = output.splitlines()
        for line in output:
            addstr(line.strip())
        addstr(names['TracerReport']['ContentFindOK'])
    else:
        addstr(names['TracerReport']['ContentFindFall'])
        raise


def start_test_mode():
    pass


def finish_test_mode():
    pass
