from Chats import Chats
from Tools import Tools
from Bot import Bot
from telebot import types

chats = Chats()
commands = ["завести котика", "мой котик", "котик инфо", "покормить котика", "на трешу", "на работу", "с треши",
            "с работы", "дуэль принять", "дуэль отклонить", "дуэль"]
Bot = Bot(commands, chats)


@Bot.bot.message_handler(func=lambda message: True)
def echo_all(message: types.Message):
    id = Tools.get_id_from_message(message)
    text = message.text.lower()
    chat = chats.get_chat(message.chat.id)
    if not Bot.is_related_message(text):
        return
    if message.reply_to_message is not None:
        if not chats.get_chat(message.chat.id).is_user_log_in(id):
            Bot.send_message(chat, "Для начала заведите себе котика. Мурмяю\nВведите: Завести котика ᓚᘏᗢ")
            return
        if Tools.is_text_correct(text, "дуэль", Bot.bot_username):
            Bot.send_battle(message, chat)
            return
    if Tools.is_text_correct(text, "завести котика", Bot.bot_username):
        start_login(message)
        return 
    if not chats.get_chat(message.chat.id).is_user_log_in(id):
        Bot.send_message(chat, "Для начала заведите себе котика. Мурмяю\nВведите: Завести котика ᓚᘏᗢ")
    if Tools.is_text_correct(text, "мой котик", Bot.bot_username):
        Bot.my_cat(message)
    elif Tools.is_text_correct(text, "котик инфо", Bot.bot_username):
        Bot.cat_info(message)
    elif Tools.is_text_correct(text, "покормить котика", Bot.bot_username):
        Bot.cat_eat(message)
    elif Tools.is_text_correct(text, "на трешу", Bot.bot_username):
        Bot.cat_train(message)
    elif Tools.is_text_correct(text, "на работу", Bot.bot_username):
        Bot.cat_work(message)
    elif Tools.is_text_correct(text, "с треши", Bot.bot_username):
        Bot.cat_from_train(message)
    elif Tools.is_text_correct(text, "с работы", Bot.bot_username):
        Bot.cat_from_work(message)
    elif Tools.is_text_correct(text, "дуэль принять", Bot.bot_username):
        Bot.duel_accepted(message, chat)
    elif Tools.is_text_correct(text, "дуэль отклонить", Bot.bot_username):
        Bot.duel_deny(message, chat)


def start_login(message):
    id = Tools.get_id_from_message(message)
    chat = chats.get_chat(message.chat.id)
    if chats.get_chat(message.chat.id).is_user_log_in(id):
        return
    msg = Bot.bot.send_message(chat.id, "Выбери имя для своего котика!")
    Bot.bot.register_next_step_handler(msg, set_name, message.from_user.id)
    return


@Bot.bot.message_handler(func=start_login)
def set_name(message, user_id):
    if message.from_user.id != user_id:
        Bot.bot.register_next_step_handler(message, set_name, user_id)
        return

    id = Tools.get_id_from_message(message)
    chats.get_chat(message.chat.id).set_cat_name(id, cat_name=message.text, name=message.from_user.username)
    Bot.bot.send_photo(message.chat.id,
                       open(chats.get_chat(message.chat.id).users[id].cat.image_path, "rb"),
                       caption="Муур, " +
                               chats.get_chat(message.chat.id).users[id].name + " теперь у тебя есть котикᓚᘏᗢ " +
                               chats.get_chat(message.chat.id).users[
                                   id].cat.name + "!\nВселенский рандом определил как " +
                               "выглядит твой котик и передает тебе заботу о нем! \nМюр!🐈")

    return


Bot.bot.polling()
