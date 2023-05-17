import sys
import os
import argparse
import json

path_to_my_components = os.path.join(os.path.dirname(__file__))
sys.path.append(path_to_my_components)

import Uploader
import Notificator
import Editor
import Initializer

parser = argparse.ArgumentParser(description="type_of_start")
parser.add_argument('-a', dest="mode", default="simple", type=str)
args = parser.parse_args()


def delete_cron_task():
    import subprocess

    new_lines = ''

    path = Initializer.settings['main']['Location'] + '/start.py'

    command_to_remove = f"* * * * * /usr/bin/python3 {path} -a t\n"

    with open("temp.cron", "w") as f:
        subprocess.run(["crontab", "-l"], stdout=f)

    with open("temp.cron", "r") as f:
        lines = f.readlines()

    for line in lines:
        new_lines = new_lines + line.replace(command_to_remove, '')

    with open("temp.cron", "w") as f:
        f.writelines(new_lines)

    subprocess.run(["crontab", "temp.cron"])

    os.remove("temp.cron")


def run():
    try:
        Uploader.start()
        Notificator.horn()
    except:
        Notificator.horn()



def test():
    delete_cron_task()
    report = ''
    Initializer.settings["FtpUploader"]['Test_Folder_For_Scan'] = os.path.join(Initializer.settings["main"]['Location'],
                                                                               'TestFolder')
    Initializer.storeparametr()

    run()
    Initializer.settings["FtpUploader"]['Test_Folder_For_Scan'] = ''
    Initializer.storeparametr()

    report = Notificator.RepGen.Report_Maker('Test')
    with open(os.path.join(path_to_my_components,'report','TestReport.txt'), 'w') as write_file:
        json.dump(report, write_file, indent=2)


if args.mode == "s":
    Editor.start()
elif args.mode == "t":
    test()
else:
    run()
