from Game import *


class Control(object):
    actions = []

    def __init__(self, team_id, player_id_list, map_info, data):
        self.actions = []
        self.team_id = team_id
        self.player_id_list = player_id_list
        self.map_info = map_info
        self.data = data

        for player_id in player_id_list:
            action = {
                "team": self.team_id, "player_id": player_id,
                "move": [],  # 移动方向，不动为空[]
                "fire": [],  # 开火方向, 不开火为空[]
                "bullet_type": 0,  # 子弹类型,0普通子弹, 1超级子弹
            }
            self.actions.append(action)

    def move(self, player_id, direction):
        for action in self.actions:
            if action["player_id"] == player_id:
                action["move"] = [direction]
                break
        return True

    def fire(self, player_id, direction, bullet_type):
        for action in self.actions:
            if action["player_id"] == player_id:
                action["fire"] = [direction]
                action["bullet_type"] = bullet_type
                break
        return True

    def send_msg(self, sock):
        if self.actions is None or len(self.actions):
            print("There are no available actions")
        action_data = {
            "msg_name": "action",  # 动作请求消息名
            "msg_data": {
                "round_id": self.data["msg_data"]["round_id"],  # 回合标识，回填
                "actions": self.actions
            }
        }
        print(self.player_id_list)
        send(sock, action_data)
        return True
