def fire_ai(game, control, strategy) : #将已经实例化的类传入开火逻辑函数
    game.set_tank_msg() #更新坦克信息
    enemy = game.find_all_enemy() #获取所有敌方坦克信息
    our = game.find_all_our_tank() #获取所有我方坦克信息
    for each in our : #遍历我方所有坦克
        face_enemy = [] #十字轴上的坦克列表
        face_distance = [] #十字轴上的坦克与我方此坦克的距离
        face_flag = []
        for every in enemy : #遍历敌方所有坦克
            if every['x'] == each['x'] : #如果存在敌方坦克与我方此坦克处于同一垂直线 则将flag设为-1
                face_flag.append(-1)
                face_enemy.append(every)
                face_distance.append(abs(every['y'] - each['y']))
            elif every['y'] == each['y'] : #如果存在敌方坦克与我方此坦克处于同一水平线 则将flag设为1
                face_flag.append(1)
                face_enemy.append(every)
                face_distance.append(abs(every['x'] - each['x']))
            # 至此，flag = 0 十字轴上不存在坦克
            # flag = -1 同一垂直线
            # flag = 1 同一水平线

        if len(face_enemy) != 0 :
            over_index = []
            min_dis = face_distance[0]
            min_index = 0
            i = 0


            for count in range(len(face_distance)):
                for i in range(len(face_distance)):
                    if min_dis > face_distance[i] and i not in over_index:
                        min_dis = face_distance[i]
                        min_index = i
                over_index.append(min_index)


                if face_flag[min_index] == -1:
                    if face_enemy[min_index]['y'] > each['y'] :
                        flag = 1
                        for t in range(each['y'],face_enemy[min_index]['y']) :
                            if game.maps[each['x']][t].get_terrain() == 1 or game.maps[each['x']][t].get_terrain() == 2 :
                                flag = 0
                        if flag == 1 :
                            control.fire(each['id'],'down')
                    else :
                        flag = 1
                        for t in range(face_enemy[min_index]['y'],each['y']) :
                            if game.maps[each['x']][t].get_terrain() == 1 or game.maps[each['x']][t].get_terrain() == 2 :
                                flag = 0
                        if flag == 1 :
                            control.fire(each['id'],'up')

                if face_flag[min_index] == 1:
                    if face_enemy[min_index]['x'] > each['x'] :
                        flag = 1
                        for t in range(each['x'],face_enemy[min_index]['x']) :
                            if game.maps[t][each['y']].get_terrain() == 1 or game.maps[t][each['y']].get_terrain() == 2 :
                                flag = 0
                        if flag == 1 :
                            control.fire(each['id'],'right')
                    else :
                        flag = 1
                        for t in range(face_enemy[min_index]['y'],each['y']) :
                            if game.maps[each['x']][t].get_terrain() == 1 or game.maps[each['x']][t].get_terrain() == 2 :
                                flag = 0
                        if flag == 1 :
                            control.fire(each['id'],'left')
        else : control.fire(each['id'], "up", 0)