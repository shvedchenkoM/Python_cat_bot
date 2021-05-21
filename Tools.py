class Tools:
    @staticmethod
    def get_id_from_message(message):
        return message.from_user.username

    @staticmethod
    def is_text_correct(text, real, bot_username):
        return text == real or text == (bot_username + " " + real)

    @staticmethod
    def time_from_seconds(time):
        hours = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        return str(hours // 10) + str(hours % 10) + ":" + str(minutes // 10) + str(minutes % 10) + ":" + str(
            time // 10) + str(time % 10)

    @staticmethod
    def get_time_to_string(time):
        if time == "00:00:00":
            return ""
        else:
            return str("через " + time)
