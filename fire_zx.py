import Tank
tm = [
    '$$#+B++++$A#$$$',
    '$+#++S++$++#++$',
    '$++@@+####+++##',
    '##+$$$$$$$$$#++',
    'A++$+*+$+*+$#+B',
    '$+#$+#2++#+$+++',
    '+$#$A+$@$++$#++',
    '++#$$+@@@+$$#++',
    '++#$++$@$++$#$+',
    '+++$+#+++#+$#+$',
    'A+#$+*+$+4+$++B',
    '++#$$$$$$$$$+##',
    '##+++####+@@++$',
    '$++#++$++++E#+$',
    '$$$#B$++++A+#$$']
map_max_width = 15
map_max_high = 15

enemy_list = ( (0,6),(2,2),(0,8),(0,10),(0,11) )

me = Tank.Tank((0,4),0)
list
#局势判断逻辑 Tank
def panduanjushi(me,tm,enmey_list,map_max_width,map_max_high):

    face_enmey_num = 0
    enemy_flag = 0
    for enemy in enmey_list:
        if enemy[0] == me.coordinate[0]:
            for lie in range(0,map_max_width):
                print("lie:" + str(lie))
                if tm[ enemy[0]] [lie] == '$':
                    if lie > me.coordinate[1]: #列
                        return face_enmey_num + enemy_flag
                    enemy_flag = 0;

                if lie == enemy[1]:
                    enemy_flag = enemy_flag + 1
                    print("en:"+str(lie))

                if lie == me.coordinate[1]:
                    if enemy_flag >= 1:
                        face_enmey_num = face_enmey_num + enemy_flag
                        enemy_flag = 0

    return face_enmey_num+enemy_flag
# 我放tank类 方向（up、down、left、right）
def find_enemy(tank,dicor,game):
    enemy_num = 0
    enemy_list = game.find_all_enemy()

    if dicor=="left":
        for lie in  range(0,tank.coordinate[1]):
            if (tank.coordinate[0],lie) in enemy_list:
                enemy_num = enemy_num + 1
            if game.string_map_info[tank.coordinate[0],lie]=='$':
                enemy_num = 0
            if lie == tank.coordinate[1]:
                return enemy_num

    if dicor == "right":
        for lie in range(tank.coordinate[1],game.width):
            if (tank.coordinate[0],lie) in enemy_list:
                enemy_num = enemy_num + 1
            if game.string_map_info[tank.coordinate[0], lie] == '$':
                return enemy_num
        return enemy_num

    if dicor=="up":
        for hang in  range(0,tank.coordinate[0]):
            if (hang,tank.coordinate[1]) in enemy_list:
                enemy_num = enemy_num + 1
            if game.string_map_info[tank.coordinate[0],hang]=='$':
                enemy_num = 0
            if hang == tank.coordinate[0]:
                return enemy_num

    if dicor=="down":
        for hang in  range(0,tank.coordinate[0]):
            if (hang,tank.coordinate[1]) in enemy_list:
                enemy_num = enemy_num + 1
            if game.string_map_info[tank.coordinate[0],hang]=='$':
                return enemy_num
        return enemy_num





print("result:"+str(panduanjushi(me,tm,enemy_list,map_max_width,map_max_high) ))
