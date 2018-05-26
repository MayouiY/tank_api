import random


class Scheduler(object):
    def __init__(self, team_id, map_info, player_id_list, round_data):
        self.map_info = map_info
        self.team_id = team_id
        self.player_id_list = player_id_list
        self.round_data = round_data

    def schedule(self):
        actions = []
        for player_id in self.player_id_list:
            action = {
                         "team": self.team_id, "player_id": player_id,
                         "move": [random.choice(["up", "down", "right", "left"])],  # 移动方向，不动为空[]
                         "fire": [random.choice(["up", "down", "right", "left"])],  # 开火方向, 不开火为空[]
                         "bullet_type": 0,  # 子弹类型,0普通子弹, 1超级子弹
                     },
            actions.extend(action)
        return actions
