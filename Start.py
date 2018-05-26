
from Control import *


def start_round(sock, team_id):
    game = Game(sock, team_id)
    game.register()
    with open("log.txt", "a+") as f:
        f.write("success register")
    while True:
        game.receive_msg()
        msg_name = game.get_msg_name()
        if msg_name == "round":
            game.round_start()
            control = Control(team_id, game.our_tank_id, game.maps, game.data)
            # 操作函数
            for tank_id in game.our_tank_id:
                control.move(tank_id, "up")
                control.fire(tank_id, "up", 0)
            control.send_msg(sock)
            game.round_clear()
        elif msg_name == "leg_start":
            game.leg_start()

        elif msg_name == MSG_NAME_LEG_END:
            print(game.data["msg_data"])
            game.leg_clear()
        elif msg_name == MSG_NAME_GAME_OVER:
            print("Game Over ...")
            break
