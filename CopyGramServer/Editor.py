# -*- coding: utf-8 -*-
import json
import os
import Initializer
from getpass import getpass

settings = Initializer.settings
Language = Initializer.get_lang('Editor')


def writeparametr(where=None, what=None, promt=None, mode='write'):
    if mode != 'pass':
        txt2 = input(promt)
    else:
        password = getpass(promt)
        settings[where][what] = str(password)
        print(Language['Complete'])

    if mode == "write":
        settings[where][what] = str(txt2)
        print(Language['Value'] + what + " = " + settings[where][what])
    elif mode == "delete":
        settings[where][what].remove(int(txt2))
        print(Language['Value'] + what + " = " + txt2 + Language['Deleted'])
    elif mode == "add":
        settings[where][what].append(int(txt2))
        print(Language['Value'] + what + " = " + txt2 + Language['Added'])
    storeparametr()
    if where == "telegram":
        SetNotificator()
    if where == "FtpUploader":
        SetUploader()


def storeparametr():
    with open(Initializer.path_to_settings, 'w') as write_file:
        json.dump(settings, write_file, indent=2)


def SetNotificator():
    answers = {
        "1": {"what": "token", "where": "telegram", "promt": Language['TokenPrompt'], 'context': 'pass'},
        "2": {"what": "recipients", "where": "telegram", "promt": Language['EnterUserIdPrompt'], 'context': 'add'},
        "3": {"what": "recipients", "where": "telegram", "promt": Language['EnterUserIdPrompt'], 'context': 'delete'}}
    promt = f'''
    0 - {Language['Back']}
    1 - {Language['SetToken']}
    2 - {Language['AddUser']}
    3 - {Language['DeleteUser']}
    '''
    print(promt)
    txt = input(Language['SetVariant'])
    if answers.get(txt, 0):
        writeparametr(answers[txt]["where"], answers[txt]["what"], answers[txt]["promt"], answers[txt]['context'])
    else:
        print(Language['Incorrect'])
        start()


def SetUploader():
    answers = {
        "1": {"what": "host", "where": "FtpUploader", "promt": Language['FtpUrlPrompt']},
        "2": {"what": "ftp_password", "where": "FtpUploader", "promt": Language['PassPrompt'], "mode": "pass"},
        "3": {"what": "ftp_user", "where": "FtpUploader", "promt": Language['LoginPrompt']},
        "4": {"what": "ftp_port", "where": "FtpUploader", "promt": Language['PortPrompt']},
        "5": {"what": "folder_for_scan", "where": "FtpUploader", "promt": Language['ScanFolderPrompt']},
        "6": {"what": "start_dir", "where": "FtpUploader", "promt": Language['FtpStartFolderPrompt']}
    }
    promt = f'''
    0 - {Language['Back']}
    1 - {Language['SetFtpUrl']}
    2 - {Language['SetFtpPass']}
    3 - {Language['SetFtpLogin']}
    4 - {Language['SetFtpPort']}
    5 - {Language['SetScanFolder']}
    6 - {Language['SetFtpStartFolder']}
    '''
    print(promt)
    txt = input(Language['SetVariant'])
    if answers.get(txt, 0):
        # TODO заменить награмождение параметров снизу на один словарь с параметрами
        writeparametr(answers[txt]["where"], answers[txt]["what"], answers[txt]["promt"],
                      answers[txt].get('mode', 'write'))
    else:
        print(Language['Incorrect'])
        start()


def external_cron():
    os.system("crontab -e")
    start()


def show_settings():
    set = Initializer.settings
    for level_1 in set:
        print(level_1 + ':')
        for level_2 in set[level_1]:
            print('\t' + f'{level_2} - {set[level_1][level_2]}')

    input('\n' + Language["PressEnter"])
    start()


def finish():
    print('bye bye')
    return


def get_and_print_lang_list():
    lang_directory = Initializer.get_lang('get_path_localizations')
    list_localizations = {}
    tmp = ''
    count = 0
    with os.scandir(lang_directory) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                count += 1
                tmp = {str(count): entry.name}
                list_localizations.update(tmp)
                print(f'    {count} - {entry.name}')

    return list_localizations


def convert_text_to_ascii():
    languages = get_and_print_lang_list()
    txt = input(Language['SetLanguage'])

    if languages.get(txt, False):
        path = Initializer.get_lang('get_path_localizations')
        path_to_localization = os.path.join(path, languages[txt])
        lang = Initializer.get_lang('get_all_localization', path_to_localization)

        with open(path_to_localization,
                  'w') as write_file:  # Данный механизм неявно сохраняет файл в закодированных UTF-8 кодах
            json.dump(lang, write_file, indent=2)

        print(Language['Complete'])
        start()
    else:
        print(Language['Incorrect'])
        start()


def utilities():
    promt = f'''
    0 - {Language['Back']}
    1 - {Language['FixText']}
    2 - {Language['ShowSet']}
    '''
    print(promt)
    functions = {"1": convert_text_to_ascii,
                 "2": show_settings,
                 "0": start}
    txt = input(Language['SetVariant'])
    if functions.get(txt, False):
        functions[str(txt)]()
    else:
        print(Language['Incorrect'])
        start()


def start():
    promt = f'''
    1 - {Language['SetUploader']}
    2 - {Language['SetNotificator']}
    3 - {Language['SetLanguage']}
    4 - {Language['OpenCronTab']}
    5 - {Language['Utilities']}
    0 - {Language['Back']}
    '''
    functions = {"1": SetUploader,
                 "2": SetNotificator,
                 "3": SelectLanguage,
                 "4": external_cron,
                 "5": utilities,
                 "0": finish
                 }
    print(promt)
    txt = input(Language['SetVariant'])
    if functions.get(txt, False):
        functions[str(txt)]()
    else:
        print(Language['Incorrect'])


def SelectLanguage():
    global Language

    languages = get_and_print_lang_list()
    txt = input(Language['ChooseLanguage'])
    if languages.get(txt, False):
        settings['main']['Language'] = languages[txt]
        storeparametr()
        Language = Initializer.get_lang('Editor')
        start()
    else:
        print(Language['Incorrect'])
        return


if __name__ == "__main__":
    start()
