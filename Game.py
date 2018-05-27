from Map import Map
from Tank import *
import os
import sys
import socket
import json
import time
MAX_RECV_BYTES = 1024*10
MSG_NAME_REGISTRATION = "registration"
MSG_NAME_LEG_START = "leg_start"
MSG_NAME_ROUND = "round"
MSG_NAME_ACTION = "action"
MSG_NAME_LEG_END = "leg_end"
MSG_NAME_GAME_OVER = "game_over"


def recv(sock):
    while True:
        msg = sock.recv(MAX_RECV_BYTES)
        if len(msg) != 0:
            break
    print("<<<", msg)
    return str(msg, encoding="utf-8")


def send(sock, data):
    msg_data = json.dumps(data)
    msg_len = "%05d" % len(msg_data)
    msg = msg_len + msg_data
    print(">>>", msg)
    sock.send(bytes(msg, encoding="utf8"))


def registration(sock, team_id):
    reg_data = {
        "msg_name": "registration",
        "msg_data": {
            "team_id": team_id,
            "team_name": "test",
        }}
    send(sock, reg_data)






class Game(object):

    data = None
    map_width = 0
    map_height = 0
    our_tank_id = []
    enemy_tank_id = []
    maps = None
    enemy_tank = []
    star_list = []
    coin_list = []
    enemy_bullet_list = []
    enemy_super_bullet = []
    string_map_info = []
    our_tank = []

    def __init__(self, sock, team_id):
        self.sock = sock
        self.team_id = team_id

    def register(self):
        registration(self.sock, self.team_id)

    def receive_msg(self):
        msg = recv(self.sock)
        msg_len = int(msg[0:5])
        msg_data = msg[5:]
        if msg_len != len(msg_data):
            raise Exception("parse message failed")
        self.data = json.loads(msg_data)

    def get_msg_name(self):
        if self.data is None:
            raise Exception("we have not receive any data")
        else:
            msg_name = self.data.get("msg_name", None)
        return msg_name

    def leg_start(self):
        if self.get_msg_name() == MSG_NAME_LEG_START:
            self.map_width = self.data["msg_data"]["map"]["width"]
            self.map_height = self.data["msg_data"]["map"]["height"]
            teams = self.data["msg_data"]["teams"]
            for team in teams:
                if team["id"] == self.team_id:
                    self.our_tank_id = team["players"]
                else:
                    self.enemy_tank_id = team["players"]

    def round_start(self):
        self.get_msg_name()
        if self.get_msg_name() == MSG_NAME_ROUND:
            msg_data = self.data["msg_data"]

            if self.maps is None:
                self.maps = [[Map(msg_data["round_id"], (width, height)) for height in range(self.map_height)]for width in range(self.map_width)]
                #for width in range(self.map_width):
                #    for height in range(self.map_height):
                #        self.maps[width][height] = Map(msg_data["round_id"], (width, height))

            for brick_walls in msg_data["brick_walls"]:
                self.maps[brick_walls["x"]][brick_walls["y"]].change_terrain(1)

            for iron_walls in msg_data["iron_walls"]:
                self.maps[iron_walls["x"]][iron_walls["y"]].change_terrain(2)

            for river in msg_data["river"]:
                self.maps[river["x"]][river["y"]].change_terrain(3)

            for coin in msg_data["coins"]:
                self.maps[coin["x"]][coin["y"]].change_coins(coin["point"])
                self.coin_list.append(coin)
            for star in msg_data["stars"]:
                self.maps[star["x"]][star["y"]].change_stars(1)
                self.star_list.append(star)
            for bullet in msg_data["bullets"]:
                if bullet["team"] == self.team_id:
                    self.maps[bullet["x"]][bullet["y"]].add_our_bullets(bullet["direction"], bullet["type"])

                else:
                    self.maps[bullet["x"]][bullet["y"]].add_enemy_bullets(bullet["direction"], bullet["type"])
                    self.enemy_bullet_list.append(bullet)
                    direction = bullet["direction"]
                    for i in range(1, 2):
                        try:
                            if direction is "up":
                                self.maps[bullet["x"]][bullet["y"] + i].death_trap = True
                            elif direction is "down":
                                self.maps[bullet["x"]][bullet["y"] - i].death_trap = True
                            elif direction is "left":
                                self.maps[bullet["x"] - i][bullet["y"]].death_trap = True
                            elif direction is "right":
                                self.maps[bullet["x"] + i][bullet["y"]].death_trap = True
                        except IndexError:
                            break
                        except Exception as ex:
                            print("%s, retry ..." % ex)

    def set_tank_msg(self):  # 请在使用我方tank信息前调用
        msg_data = self.data["msg_data"]
        for tank_msg in msg_data["players"]:
            if tank_msg["team"] == self.team_id:
                self.maps[tank_msg["x"]][tank_msg["y"]].add_tank_id(True, tank_msg["id"], tank_msg["super_bullet"])
                self.our_tank.append(tank_msg)
            else:
                self.maps[tank_msg["x"]][tank_msg["y"]].add_tank_id(False, tank_msg["id"], tank_msg["super_bullet"])
                self.enemy_tank.append(tank_msg)

    def set_zx_tank_msg(self):
        msg_data = self.data["msg_data"]
        tanks = []
        for tank_msg in msg_data["players"]:
            if tank_msg["team"] == self.team_id:
                new_tank = Tank((tank_msg["x"], tank_msg["y"]), tank_msg["id"])
                if tank_msg["super_bullet"] == 1:
                    new_tank.set_super_bullet()
                tanks.append(new_tank)
        return tanks

    def find_all_enemy(self):
        return self.enemy_tank

    def find_all_our_tank(self):  # 得到我方所有坦克的信息（字典形式{"id":0,"team":1001,"x":0,"y":1, "super_bullet":0}）
        return self.our_tank

    def find_all_star(self):
        return self.star_list

    def find_all_coins(self):
        return self.coin_list

    def find_all_bullets(self):
        return self.enemy_bullet_list

    def find_all_super_bullets(self):
        super_bullets_list = []
        for bullet in self.enemy_bullet_list:
            if bullet["type"] == 1:
                super_bullets_list.append(bullet)
        return super_bullets_list


    def round_clear(self):
        self.data = None

        self.maps = None
        self.enemy_tank = []
        self.star_list = []
        self.coin_list = []
        self.enemy_bullet_list = []
        self.enemy_super_bullet = []
        self.our_tank = []

    def leg_clear(self):
        self.round_clear()
        self.our_tank_id = []
        self.enemy_tank_id = []

    def find_all_road_nearby(self, coordinate):
        rounds = [((coordinate[0]+1, coordinate[1]), "right"), ((coordinate[0]-1, coordinate[1]), "left"),
                 ((coordinate[0], coordinate[1]+1), "up"), ((coordinate[0], coordinate[1] - 1), "down")]
        round_could = []
        for point in rounds:
            if self.maps[point[0]][point[1]].get_terrain() is 0 and self.maps[point[0]][point[1]].death_trap is False:
                round_could.append(point)
        return round_could

    def set_string_map(self):
        self.string_map_info = [["+" for y in range(self.map_height)] for x in range(self.map_width)]

    def make_string_map(self):
        msg_data = self.data["msg_data"]
        for brick_walls in msg_data["brick_walls"]:
            self.string_map_info[brick_walls["x"]][brick_walls["y"]] = "$"

        for iron_walls in msg_data["iron_walls"]:
            self.string_map_info[iron_walls["x"]][iron_walls["y"]] = "#"

        for river in msg_data["river"]:
            self.string_map_info[river["x"]][river["y"]] = "@"

        for coin in msg_data["coin"]:
            self.string_map_info[coin["x"]][coin["y"]] = str(coin["point"])
       
        for star in msg_data["stars"]:
            self.string_map_info[star["x"]][star["y"]] = "*"
        







