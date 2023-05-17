import Initializer
from datetime import datetime

Files = {}

is_executed = False
Language = Initializer.get_lang('Notificator')
CopyCompleted = Initializer.get_lang('FtpUploader')['CopyCompleted']
path_to_telegram_report = Initializer.telegram_report_path
replist = {"FileList": Files, "Status": "Good", "Note": CopyCompleted, "ReportDate": " "}


def Data_Report_Collector(context='Bad', message='UnknownError', file=None):
    global is_executed
    if not (file is None) and context == 'Good':
        new_value = {file: 'Good'}
        replist['FileList'].update(new_value)
    elif context == 'End':
        Drop_Date_To_Report()
    elif file is None:
        replist['Note'] = message
        replist['Status'] = 'Bad'
    elif not (file is None) and context == 'Bad' and is_executed:
        new_value = {file: 'Bad'}
        replist['FileList'].update(new_value)
    elif not (file is None) and context == 'Bad' and not is_executed:
        replist['Note'] = message
        new_value = {file: 'Bad'}
        replist['FileList'].update(new_value)
        replist['Status'] = 'Bad'
        is_executed = True


def Drop_Date_To_Report():
    date = str(datetime.today().strftime('%Y.%m.%d - %H:%M:%S'))
    replist['ReportDate'] = date


def Report_Maker(Result):
    if Result == 'Messenger':

        Report = ''
        emoji_CheckMarkButtonGreen = u'\U00002705' + '  '
        emoji_CheckBoxWithCheckGrey = u'\U00002611' + ' '
        emoji_InformationGrey = u'\U00002139' + ' '
        emoji_WhiteStarOnOrangeBackground = u'\U00002734' + ' '
        emoji = emoji_WhiteStarOnOrangeBackground
        if replist['FileList']:

            Report += emoji_WhiteStarOnOrangeBackground + Language['FileList'] + '\n'
            for file in replist['FileList']:
                if replist['FileList'][file] == 'Good':
                    Report += emoji_CheckMarkButtonGreen + file + '\n'
                elif replist['FileList'][file] == 'Bad':
                    Report += emoji_CheckBoxWithCheckGrey + file + '\n'
                    emoji = emoji_InformationGrey
            Report += emoji + replist['Note'] + '\n'
            Report += emoji_WhiteStarOnOrangeBackground + Language['ReportDate'] + replist['ReportDate']

        if not replist['FileList']:
            Report += emoji_InformationGrey + replist['Note'] + '\n'
            Report += emoji_WhiteStarOnOrangeBackground + Language['ReportDate'] + replist['ReportDate']
        return Report
    if Result == 'Html':
        pass
    if Result == 'Test':
        Report = ''
        if replist['FileList']:

            Report += Language['FileList'] + '\n'
            for file in replist['FileList']:
                if replist['FileList'][file] == 'Good':
                    Report += file + '\n'
                elif replist['FileList'][file] == 'Bad':
                    Report += file + '\n'
            Report += replist['Note'] + '\n'
            Report += Language['ReportDate'] + replist['ReportDate']

        if not replist['FileList']:
            Report += replist['Note'] + '\n'
            Report += Language['ReportDate'] + replist['ReportDate']
        return Report
