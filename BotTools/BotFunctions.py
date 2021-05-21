from BotTools.BotSettings import BotSettings
from Tools import Tools
from telebot import types
from Battle.battle import battle
from Chat import Chat


class BotFunctions(BotSettings):
    def __init__(self, commands, chats):
        BotSettings.__init__(self, commands)
        self.chats = chats

    def my_cat(self, message):
        # print(users.users)
        id = Tools.get_id_from_message(message)
        markup = types.InlineKeyboardMarkup(row_width=2)
        info = types.InlineKeyboardButton(text="Котик Инфо", switch_inline_query_current_chat="Котик Инфо")
        inventory = types.InlineKeyboardButton(text="Мой инвентарь", switch_inline_query_current_chat="Мой Инвентарь")
        markup.add(info, inventory)
        img_file = open(self.chats.get_chat(message.chat.id).users[id].cat.image_path, "rb")
        self.bot.send_photo(message.chat.id, img_file,
                            caption=self.chats.get_chat(message.chat.id).users[id].cat.get_my_cat(),
                            reply_markup=markup)
        img_file.close()

    def cat_info(self, message):
        id = Tools.get_id_from_message(message)
        self.bot.send_message(message.chat.id,
                              self.chats.get_chat(message.chat.id).users[id].cat.get_cat_info(),
                              reply_markup=self.chats.get_chat(message.chat.id).users[id].cat.get_keyboard())

    def cat_eat(self, message):
        id = Tools.get_id_from_message(message)
        chat = self.chats.get_chat(message.chat.id)
        answer = chat.users[id].cat.feed_cat()
        if answer != "":
            self.send_message(chat, answer)

    def cat_train(self, message):
        id = Tools.get_id_from_message(message)
        chat = self.chats.get_chat(message.chat.id)
        answer = chat.users[id].cat.put_cat_to_training()
        if answer != "":
            self.send_message(chat, answer)

    def cat_work(self, message):
        id = Tools.get_id_from_message(message)
        chat = self.chats.get_chat(message.chat.id)
        answer = chat.users[id].cat.put_cat_to_work()
        if answer != "":
            self.send_message(chat, answer)

    def cat_from_train(self, message):
        id = Tools.get_id_from_message(message)
        chat = self.chats.get_chat(message.chat.id)
        answer = chat.users[id].cat.pick_up_from_training()
        if answer != "":
            self.send_message(chat, answer)

    def cat_from_work(self, message):
        id = Tools.get_id_from_message(message)
        chat = self.chats.get_chat(message.chat.id)
        answer = chat.users[id].cat.pick_up_from_work()
        if answer != "":
            self.send_message(chat, answer)

    def send_battle(self, message: types.Message, chat):
        kb = types.InlineKeyboardMarkup()
        accepted = types.InlineKeyboardButton(text="Дуэль принять", switch_inline_query_current_chat="Дуэль принять")
        deny = types.InlineKeyboardButton(text="Дуэль отклонить", switch_inline_query_current_chat="Дуэль отклонить")
        kb.add(accepted)
        kb.add(deny)
        id1 = message.reply_to_message.from_user.username
        id2 = message.from_user.username
        chat.battle = battle(self.chats.get_chat(message.chat.id).users[id1].cat,
                             self.chats.get_chat(message.chat.id).users[id2].cat)
        self.bot.send_message(message.chat.id, "Вы бросили вызов котику " +
                              message.reply_to_message.from_user.first_name, reply_markup=kb)

    def duel_deny(self, message, chat):
        chat.battle = None
        id = Tools.get_id_from_message(message)
        img_file = open("Images/duel_deny_cat.png", "rb")
        self.bot.send_photo(message.chat.id, img_file, caption="отлично, не стоит царапаться, лучше:",
                            reply_markup=self.chats.get_chat(message.chat.id).users[id].cat.get_keyboard())
        img_file.close()

    def duel_accepted(self, message, chat):
        id = Tools.get_id_from_message(message)
        img_file = open("Images/cat_battle_winner.jpg", "rb")
        self.bot.send_photo(message.chat.id, img_file, caption="Победил котик участника " + chat.battle.battle(),
                            reply_markup=self.chats.get_chat(message.chat.id).users[id].cat.get_keyboard())
        chat.battle = None
        img_file.close()
