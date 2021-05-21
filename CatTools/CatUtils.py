from CatTools.CatActions import CatActions
from CatTools.CatSettings import CatSettings
from telebot import types
from Tools import Tools


class CatUtils(CatActions):
    def __init__(self, images):
        CatActions.__init__(self, images)

    def get_my_cat(self):
        return "😸Имя вашего котика: " + self.name + "\n" + \
               "⭐️Уровень вашего котика: " + str(self.level) + "\n" + \
               "🐟Сытость: " + str(self.hunger) + "/" + str(self.max_hunger) + "\n" + \
               "🔮Мурмана: " + str(self.murmana) + "/" + str(self.max_mana_value) + "\n" + \
               "🐁Мышки: " + str(self.mice) + "\n\n" + \
               "🌚Настроение: " + str(self.mood) + "(" + self.mood_desc() + ")" + "\n\n" + \
               "💪Количество побед: " + str(self.win) + "\n" + \
               "👎Количество поражений: " + str(self.lose) + "\n"

    def get_cat_info(self):
        timeE = Tools.get_time_to_string((self.eat_time_left()))
        timeT = Tools.get_time_to_string((self.training_time_left()))
        timeW = Tools.get_time_to_string((self.work_time_left()))
        if timeT > timeW:
            time = timeT
        else:
            time = timeW
        return "🐟Котика можно покормить " + timeE + "\n" + \
               "💼Котика можно отправить на работу " + time + "\n" \
               "🧚🏼‍♀️Котика можно отправить на тренировку " + time + "\n" \
               "⚔️Можно учавствовать в поединке\n" \
               "🎉Можно пойти на тусу\n" \
               "💝Котик не в браке"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        if not self.is_cat_eat:
            eat = types.InlineKeyboardButton(text="Покормить котика",
                                             switch_inline_query_current_chat="Покормить котика")
            keyboard.add(eat)
        if self.is_cat_home:
            train = types.InlineKeyboardButton(text="Отправить котика на тренировку",
                                               switch_inline_query_current_chat="на трешу")
            keyboard.add(train)
        if self.is_cat_home:
            work = types.InlineKeyboardButton(text="Отправить котика на работу",
                                              switch_inline_query_current_chat="на работу")
            keyboard.add(work)

        if self.is_cat_train and self.training_time_left() == "00:00:00":
            home = types.InlineKeyboardButton(text="Забрать котика с тренировки",
                                              switch_inline_query_current_chat="с треши")
            keyboard.add(home)

        if self.is_cat_work and self.work_time_left() == "00:00:00":
            home = types.InlineKeyboardButton(text="Забрать котика с работы",
                                              switch_inline_query_current_chat="с работы")
            keyboard.add(home)
        return keyboard
