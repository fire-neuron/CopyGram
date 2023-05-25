# -*- coding: utf-8 -*-
import ftplib
import os
import socket
import Initializer
import RepGen

settings = Initializer.settings
Language = Initializer.get_lang('FtpUploader')

UnknownError = Language['UnknownError']
FailedConnect = Language['FailedConnect']
InvalidAuthorization = Language['InvalidAuthorization']
DirNotSet = Language['DirNotSet']
CopyError = Language['CopyError']
CopyCompleted = Language['CopyCompleted']
TimeOut = Language['TimeOut']
FtpStartFolderError = Language['FtpStartFolderError']
ConRefuse = Language['ConRefuse']

host = settings['FtpUploader']['host']
ftp_user = settings['FtpUploader']['ftp_user']
ftp_password = settings['FtpUploader']['ftp_password']
if settings['FtpUploader']['ftp_port']:
    ftp_port = int(settings['FtpUploader']['ftp_port'])
else:
    ftp_port = 21
start_dir = settings['FtpUploader']['start_dir']
report_path = Initializer.telegram_report_path
path_to_advanced_report = Initializer.path_to_advanced_report
myPath = None





file_status = ''

# sys.stdout = open(path_to_advanced_report, 'w')

# sys.stderr = open(path_to_advanced_report, 'w')


myFTP = ftplib.FTP()
myFTP.set_debuglevel(1)


def start():
    global myPath
    myPath = settings['FtpUploader']['folder_for_scan']

    if settings['FtpUploader']['Test_Folder_For_Scan']:
        myPath = settings['FtpUploader']['Test_Folder_For_Scan']


    try:
        myFTP.connect(host, ftp_port, 30)
        myFTP.login(ftp_user, ftp_password)
        if start_dir:  # Пустая строка работает как значение - Ложь
            myFTP.cwd(start_dir)
        UploadThis(myPath)
    except ConnectionRefusedError:
        RepGen.Data_Report_Collector('Bad', ConRefuse)
    except socket.error:
        RepGen.Data_Report_Collector('Bad', TimeOut)
    except ftplib.error_perm as e:
        if e.args[0][:3] == '530':
            RepGen.Data_Report_Collector('Bad', InvalidAuthorization)
        if e.args[0][:3] == '550':
            RepGen.Data_Report_Collector('Bad', str.replace(FtpStartFolderError, '*', start_dir))
    except:
        RepGen.Data_Report_Collector('Bad', FailedConnect)

    RepGen.Data_Report_Collector('End')


def get_last_object(path):
    files = os.listdir(path)
    if path == myPath:
        files = [os.path.join(path, file) for file in files]
        lastobj = max(files, key=os.path.getctime)
        files.clear()
        files.append(os.path.basename(lastobj))
        return files
    else:
        return files


def UploadThis(path):
    files = get_last_object(path)
    os.chdir(path)

    for f in files:
        if os.path.isfile(f):
            fh = open(f, 'rb')
            try:
                myFTP.storbinary('STOR %s' % f, fh)
            except:
                RepGen.Data_Report_Collector('Bad', CopyError, f)
                continue
            RepGen.Data_Report_Collector('Good', '', f)
            fh.close()
        elif os.path.isdir(f):
            try:
                myFTP.mkd(f)
            except:
                RepGen.Data_Report_Collector('Bad', DirNotSet)
                break
            myFTP.cwd(f)
            UploadThis(f)
    myFTP.cwd('..')
    os.chdir('..')


if __name__ == "__main__":
    start()
