import os
import sys
path_to_my_components = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path_to_my_components)
import Initializer
wx = Initializer.wx
settings = Initializer.server_settings
names = Initializer.language
frame = None
def tab_init(object):
    global frame
    frame = object
    frame.tab_two.telegram_set_comboBox.Bind(wx.EVT_TEXT, on_tg_set_combobox_select)
    frame.tab_two.set_tg_param_button.Bind(wx.EVT_BUTTON, set_tg_param_button)
    frame.tab_two.tg_user_list_ctrl.Bind(wx.EVT_CONTEXT_MENU, Tg_on_show_popup_menu)
    delete_item = frame.tab_two.tg_user_list_ctrl.popup_menu.Append(wx.ID_ANY, 'Удалить')
    frame.tab_two.tg_user_list_ctrl.Bind(wx.EVT_MENU, on_tg_usr_delete_item, delete_item)
    T2_сomplete_the_user_list()


def on_tg_usr_delete_item(event):
    textbox = frame.tab_two.tg_user_list_ctrl
    selection = textbox.GetFirstSelected()
    id = textbox.GetItemText(selection, 0)
    Initializer.server_settings['telegram']['recipients'].remove(id)
    while selection != -1:
        textbox.DeleteItem(selection)
        selection = textbox.GetFirstSelected()
    Initializer.storeparametr()
def on_tg_set_combobox_select(event):
    object = frame.tab_two
    items = object.telegram_set_comboBox.GetItems()
    selection = object.telegram_set_comboBox.GetValue()

    if selection in items:
        object.set_tg_param_button.Enable(True)
    else:
        object.set_tg_param_button.Enable(False)


def Tg_on_show_popup_menu(event):
    textbox = frame.tab_two.tg_user_list_ctrl
    textbox.PopupMenu(textbox.popup_menu)

def T2_сomplete_the_user_list():
    T2 = frame.tab_two
    T2.tg_user_list_ctrl.DeleteAllItems()
    i = -1
    recipients = settings['telegram']['recipients']
    for user in recipients:
        i += 1
        T2.tg_user_list_ctrl.InsertItem(i, str(user))

def set_tg_param_button(event):
    T2 = frame.tab_two
    users = Initializer.server_settings['telegram']['recipients']
    item_index = T2.telegram_set_comboBox.GetSelection()
    value = T2.telegram_tf.GetValue()
    if item_index == 0:
        users.append(value)
        T2_сomplete_the_user_list()
    elif (item_index == 1) and (value in users):
        users.remove(value)
        T2_сomplete_the_user_list()

    elif item_index == 2:
        Initializer.server_settings['telegram']['token'] = value
        dlg = wx.MessageDialog(T2, names["TelegramSet"]["TokenYour"] + value,
                               names["TelegramSet"]["TokenMsg"],
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
    Initializer.storeparametr()