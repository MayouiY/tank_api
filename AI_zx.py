import Game, Control ,log_zx, random, findway

log = log_zx.log
fangxiang=["up","down","left","right"]

def find_enemy_bullets(tank,dicor,game,str_map):
    return find_enemy(tank, dicor, game, str_map, 1)

def find_enemy(tank,dicor,game,str_map,findzidan=0):
    enemy_num = 0
    enemy_list = []
    if findzidan==1:
        for i in game.find_all_bullets():
            log.log((dicor =="up" and i["direction"]=="down"))
            try:
                if (dicor =="up" and i["direction"]=="down") or (dicor =="down" and i["direction"]=="up") \
                            or (dicor == "down" and  i["direction"] == "up") or (dicor =="left" and  i["direction"]=="right"):
                    enemy_list.append((i['y'], i['x']))
            except Exception as e:
                log.log("bool:")
                log.log(e)
    else:
        for i in game.find_all_enemy():
            enemy_list.append((i['y'],i['x']))
    if dicor == "left":
        for lie in  range(0,tank.coordinate[1]):
            if (tank.coordinate[0],lie) in enemy_list:
                enemy_num = enemy_num + 1
            if str_map[tank.coordinate[0]][lie]=='$':
                enemy_num = 0
            if lie == tank.coordinate[1]:
                return enemy_num
        return enemy_num
    if dicor == "right":
        for lie in range(tank.coordinate[1],game.map_width):
            if (tank.coordinate[0],lie) in enemy_list:
                enemy_num = enemy_num + 1
            if str_map[tank.coordinate[0]][lie] == '$':
                return enemy_num
        return enemy_num
    if dicor=="up":
        for hang in  range(0,tank.coordinate[0]):
            if (hang,tank.coordinate[1]) in enemy_list:
                enemy_num = enemy_num + 1
            if str_map[tank.coordinate[0]][hang]=='$':
                enemy_num = 0
            if hang == tank.coordinate[0]:
                return enemy_num
        return enemy_num
    if dicor=="down":
        for hang in  range(0,tank.coordinate[0]):
            if (hang,tank.coordinate[1]) in enemy_list:
                enemy_num = enemy_num + 1
            if str_map[tank.coordinate[0]][hang]=='$':
                return enemy_num
        return enemy_num


def attack(mytank,game,control,str_map):
    xingdongflag = 1
    if find_enemy(mytank, "up", game, str_map) > 0:
        control.fire(mytank.tank_id, "up", 0)
        mytank.last_fire_where = "up"
    elif find_enemy(mytank, "down", game, str_map) > 0:
        control.fire(mytank.tank_id, "down", 0)
        mytank.last_fire_where = "down"
    elif find_enemy(mytank, "left", game, str_map) > 0:
        control.fire(mytank.tank_id, "left", 0)
        mytank.last_fire_where = "left"
    elif find_enemy(mytank, "right", game, str_map) > 0:
        control.fire(mytank.tank_id, "right", 0)
        mytank.last_fire_where = "right"
    else:
        control.fire(mytank.tank_id, fangxiang[random.randint(0, 3)], 0)
        # control.fire(mytank.tank_id, mytank.last_fire_where, 0)
    return xingdongflag

def protectself(mytank,game,control,str_map):
    xingdongflag = 1
    if find_enemy_bullets(mytank, "up", game, str_map) > 0:
        control.fire(mytank.tank_id, "up", 0)
        mytank.last_fire_where = "up"
    elif find_enemy_bullets(mytank, "down", game, str_map) > 0:
        control.fire(mytank.tank_id, "down", 0)
        mytank.last_fire_where = "down"
    elif find_enemy_bullets(mytank, "left", game, str_map) > 0:
        control.fire(mytank.tank_id, "left", 0)
        mytank.last_fire_where = "left"
    elif find_enemy_bullets(mytank, "right", game, str_map) > 0:
        control.fire(mytank.tank_id, "right", 0)
        mytank.last_fire_where = "right"
    else:
        #control.fire(mytank.tank_id, fangxiang[random.randint(0, 3)], 0)
        # control.fire(mytank.tank_id, mytank.last_fire_where, 0)
        return 0 #no action thistime
    return xingdongflag


def start_zx(game, control):
    str_map = game.get_string_map()
    a_enemy = game.find_all_enemy()[0]
    for mytank in game.get_all_our_tank_zx():
        fangxiang = findway.find_fangxiang(mytank,game,(a_enemy["y"],a_enemy["x"]),str_map);
        if game.maps[fangxiang[1][1]][fangxiang[1][0]].death_trap == False:
            control.move(mytank.tank_id, fangxiang[0])
        if protectself(mytank, game, control, str_map) == 0:  # fire
            attack(mytank, game, control, str_map)


