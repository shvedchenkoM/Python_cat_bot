import random

from Tools import Tools
import time
import telebot
from CatTools.CatSettings import CatSettings


class CatActions(CatSettings):

    def __init__(self, images):
        CatSettings.__init__(self, images)
        self.work_end_time = 0
        self.training_end_time = 0
        self.eat_end_time = 0
        self.is_cat_work = False
        self.is_cat_eat = False
        self.is_cat_train = False
        self.is_cat_home = True

    def put_cat_to_training(self):
        # train for 4 hours minutes for now
        if self.is_cat_home:
            self.training_end_time = round(time.time()) + 1 * 6  # * 3600
            self.is_cat_train = True
            self.is_cat_home = False
            return ""
        else:
            if self.is_cat_work:
                # send message
                # bot.send_message(chat_id, "Sorry, " + cat_name + " , next time.\n"
                #                                                  "Left time: " + self.work_time_left())
                return "Sorry, " + self.name + ", next time. Left time: " + self.work_time_left()
            elif self.is_cat_train:
                # bot.send_message(chat_id, "Sorry, " + cat_name + " , next time.\n"
                #                                                  "Left time: " + self.training_time_left())
                return "Sorry, " + self.name + ", next time. Left time: " + self.training_time_left()

    def pick_up_from_training(self):
        # print("ddd")
        if self.training_time_left() != "00:00:00":
            return "НЕ отвлекать КоТиКа во время тренировки! Омуропасно для муржизни)"
        self.is_cat_train = False
        self.murmana += self.mana_level_increase
        self.health -= self.level_increase // 10
        self.mood //= 2
        self.hunger -= 1
        self.is_cat_home = True
        if self.murmana > self.max_mana_value:
            self.update_level()
        return ""

    def pick_up_from_work(self):
        # print("ddd")
        if self.training_time_left() != "00:00:00":
            return "НЕ отвлекать КоТиКа во время тренировки! Омуропасно для муржизни)"
        self.is_cat_work = False

        self.mood //= 2
        self.hunger -= 1
        self.mice += random.randint(0, self.mice_level_increase)
        self.is_cat_home = True
        return ""

    def put_cat_to_work(self):
        # work for 8 hoursminutes for now
        if self.is_cat_home:
            self.work_end_time = round(time.time()) + 8 * 60  # * 3600
            self.is_cat_work = True
            self.is_cat_home = False
            return ""
        else:
            if self.is_cat_work:
                # send message
                # bot.send_message(chat_id, "Sorry, " + cat_name + " , next time.\n"
                #                                                  "Left time: " + self.work_time_left())
                return ("Sorry, " + self.name + ", next time. Left time: " + self.work_time_left())
            elif self.is_cat_train:
                # bot.send_message(chat_id, "Sorry, " + cat_name + " , next time.\n"
                #                                                  "Left time: " + self.training_time_left())
                return ("Sorry, " + self.name + ", next time. Left time: " + self.training_time_left())

    def feed_cat(self):
        # eat for 6 hours minutes for now
        if not self.is_cat_eat:
            self.hunger += 1
            self.eat_end_time = round(time.time()) + 6 * 60
            self.is_cat_eat = True
            return ""
        else:
            # send message
            # bot.send_message(chat_id, "Sorry, " + cat_settings.name + " , next time.\n"
            # "Left time: " + self.eat_time_left())
            return ("Sorry, " + self.name + ", next time. Left time: " + self.eat_time_left())

    def work_time_left(self):
        cur_time = round(time.time())
        if not self.is_cat_work or (self.work_end_time - cur_time) <= 0:
            self.is_cat_work = False
            return "00:00:00"
        return Tools.time_from_seconds(self.work_end_time - cur_time)

    def training_time_left(self):
        cur_time = round(time.time())
        if not self.is_cat_train or (self.training_end_time - cur_time) <= 0:
            # self.is_cat_train = False
            return "00:00:00"
        return Tools.time_from_seconds(self.training_end_time - cur_time)

    def eat_time_left(self):
        cur_time = round(time.time())
        print(self.is_cat_eat)
        if not self.is_cat_eat or (self.eat_end_time - cur_time) <= 0:
            # print("why", self.eat_end_time, cur_time)
            self.is_cat_eat = False
            return "00:00:00"

        return Tools.time_from_seconds(self.eat_end_time - cur_time)
