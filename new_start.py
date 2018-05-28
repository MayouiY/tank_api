import log_zx

# y

def find_to_go(game):
    stars = game.find_all_stars()
    if stars != []:
        return (stars[0]["x"],stars[0]["y"])

    coins = game.find_all_coins()
    if coins != [] :
        return (coins[0]["x"],coins[0]["y"])

    enemys = game.find_all_enemy()
    if enemys != []:
        for enemy in enemys:
            if enemy["super_bullet"] == 0:
                return enemy["x"], enemy["y"]
        return enemys[0]["x"], enemys[0]["y"]
    return -1


log = log_zx.log


def start_5_28(game, control, strategy):
    log.log(find_to_go(game))


