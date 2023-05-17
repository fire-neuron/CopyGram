# -*- coding: utf-8 -*-
import json
import os

settings = {}

parent_folder = os.path.dirname(__file__)
telegram_report_path = os.path.join(parent_folder, "report", "Telegram_Report.txt")
path_to_advanced_report = os.path.join(parent_folder, "report", "advanced_log.txt")
path_to_settings = os.path.join(parent_folder, "settings", "settings.json")

with open(path_to_settings, "r") as read_file_s:
    settings = json.load(read_file_s)


def get_lang(context, path=False):
    language = {}

    if path:
        path_to_localization = path
    else:
        lang = settings["main"]["Language"]
        path_to_localization = os.path.join(parent_folder, "settings", "localization", lang)

    with open(path_to_localization, "rb") as read_file_l:
        if context == 'get_path_localizations':
            return os.path.join(parent_folder, "settings", "localization")
        elif context == 'get_all_localization':
            language = json.load(read_file_l)
            return language
        else:
            language = json.load(read_file_l)[context]
            return language

def storeparametr():
    with open(path_to_settings, 'w') as write_file:
        json.dump(settings, write_file, indent=2)
