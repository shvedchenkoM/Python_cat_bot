import telebot
from Chat import Chat


class BotSettings:
    def __init__(self, commands_bot: list):
        self.bot_username = "@kitty_battle_bot"
        self.commands = commands_bot.copy()
        for i in commands_bot:
            self.commands.append(self.bot_username + " " + i)
        TokenFile = open("/home/mariia/PycharmProjects/ggvp/Token")
        Token = TokenFile.read()
        self.bot = telebot.TeleBot(Token, parse_mode=None)

    def is_related_message(self, message):
        return message in self.commands

    def send_message(self, chat, message):
        return self.bot.send_message(chat.id, message)
