# -*- coding: utf-8 -*-
import wx
import json
import os
import sys
import shutil



target = None
text_field_target = None
settings = {}
language = {}
server_settings = {}
client_settings = {}
program_name = 'CopyGramServer'
def set_prep():
    folder_path = os.path.join(os.path.expanduser("~"), "AppData\\Local\\CopyGram")

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        base_path = sys._MEIPASS
        source_path_cli = os.path.join(base_path, "settings", "set.json")
        source_path_srv = os.path.join(base_path,program_name, "settings", "settings.json")

        target_cli = os.path.join(folder_path,"set.json")
        target_svr = os.path.join(folder_path,"settings.json")
        shutil.copyfile(source_path_cli, target_cli)
        shutil.copyfile(source_path_srv, target_svr)
    return folder_path

try:
    base_path =''
    base_path2 =''
    setpath_client = os.path.join("settings", "set.json")
    setpath = os.path.join("settings", "set.json")
    setpath_server = os.path.join(program_name, "settings", "settings.json")
    with open(setpath_client,'r'):
        pass
except IOError:
    base_path = set_prep()
    base_path2 = sys._MEIPASS
    setpath_client = os.path.join(base_path,"set.json")
    setpath_server = os.path.join(base_path,"settings.json")


with open(setpath_client, "rb") as settings_file:
    settings = json.load(settings_file)
    lang = settings['Main']['language']

langpath = os.path.join(base_path2, "localization", lang)







with open(langpath, "rb") as localization:
    language = json.load(localization)


with open(setpath_server, "rb") as settings_file:
    server_settings = json.load(settings_file)

with open(setpath_client, "rb") as settings_file2:
    client_settings = json.load(settings_file2)




def storeparametr():
    with open(setpath_server, 'w') as write_file:
        json.dump(server_settings, write_file, indent=2)
def store_client_parametr():
    with open(setpath_client, 'w') as write_file:
        json.dump(client_settings, write_file, indent=2)


