# tank_api
软通的坦克操作api
### 使用说明
这套东西的使用是，将自己的操作函数放在Start.py带有注释“操作函数”的位置来调用
之前会帮助实例化Game为game，这个game的maps属性就是一个由Map类数据组成的二维数组，用坐标来寻找
会帮助实例化Control类为control。
可以把这两个当作参数传入函数

每回合开始时由于某些问题，需要自己进行tank信息的更新/设置（见Game的`set_tank_msg()`部分）
使用字符型地图也需要自行进行初始化和更新（见Game的`set_string_map()  & make_string_map()`部分）





## Control类
该类分为两个大部分，即`Move`和`Shot`

### move（移动）
函数原型
```python
def move(self, player_id, direction):
	return True # 成功
	return False #失败 
```
- `player_id` : 需要移动的坦克的id，需要是int类型。
- `direction` : 移动的方向，是字符串类型，有"up", "down", "right", "left"四个方向。
> 返回失败可能是你撞墙了。
> 每次只行动一格。

调用示例
```python
Control.move(1,"left") #id为1的坦克向左移动一格。
```

### fire（射击）
函数原型
```python
def fire(self, player_id, direction, type = 0):
	pass
```
- `player_id` : 需要移动的坦克的id，需要是int类型。
- `direction` : 移动的方向，是字符串类型，有"up", "down", "right", "left"四个方向。
- `type`: 默认是0，代表是普通子弹，一般不需要传。可以专门设置为1，代表超级子弹。

```
Control.fire(1,'up') #向上发射一发普通子弹
Control.fire(1,'up',type = 1) # 向上发射一发超级子弹
```

## Map


首先确定一件事，那就是地图的信息会存在一个Map实例的二维数组里,位置就是坐标
### 属性列表
#### coordinate
记录了本格的坐标
#### ROUND_ID
记录了回合数
#### death_trap
记录了是否是death_trap（就是在这里下回合一定会死）
### 方法列表
#### get_terrain(void)
`Map.get_terrain()`
返回值是int数值，有几种类型
- `0` -> 正常可以前进的路
- `1` —> 砖墙
- `2` -> 铁墙
- `3` -> 河流格子

#### get_coins(void)
`Map.get_coins()`
返回的是一个int类型，代表这个格子的coins数量。

#### get_stars(void)
`Map.get_stars()`
返回一个bool值，True代表有星星，False代表没有星星。

#### get_coordinate(void)
`Map.get_coordinate()`
返回一个格子的坐标，返回一个元组，(x轴坐标,y轴坐标)

#### get_tank_id(void)
`Map.get_tank_id()`
返回一个元组，代表这个格子的tank是友方还是敌方还是没有。
(True/False, Ture/False, tank_id, super_bullet)
(是否存在敌方坦克，是否是友军坦克，id，是否持有超级子弹)
#### get_enemy_bullets()
`Map.get_tank_id()`
返回一个三元组
(True/False, direction:"up", Type:0/1)

#### get_our_bullets()
返回一个三元组
(True/False, direction:"up", Type:0/1)


## Game类
这个类会返回一些比较实用的东西
这个类里包含了一个Map类型的二维数组，表现为maps
### 属性列表
#### maps
一个Map型二维数组，包含了地图信息
#### team_id
记录了我方的队伍ID
#### map_width
记录了地图的宽度（x坐标）
#### map_height
记录了地图的长度（y坐标）
#### string_map_info
记录了字符串形式的地图，需要通过`set_string_map()`设置，每回合通过`make_string_map()`更新
#### our_tank_id
一个list，每局比赛更新，内容是我方坦克的id
#### enemy_tank_id
一个list，每局比赛更新，内容是对方坦克的id
#### data
每回合收到的信息，，如果想要自己解析可以参考通信协议去找这个值

### 方法列表
#### find_all_coins()
返回一个字典组成的list 每个元素的格式是
```
{"x":3,"y":2, "point":1}
```

#### find_all_stars()
返回一个字典组成的list 每个元素的格式是
```
{"x":3,"y":2}
```

#### find_all_enemy()
返回敌方所有坦克的坐标的list
每一个元素的格式是一个字典，其中`"super_bullet":0` 代表其没有持有超级子弹，为1代表有
示例
```python
{
"id":0,"team":1001,"x":0,"y":1, "super_bullet":0
}
```
#### find_all_bullets()
返回敌方所有子弹的坐标的list
每一个元素的格式是一个字典
示例
```python
{"type":0,"team":1001,"x":0,"y":0, "direction":"down"},	 
```

#### find_all_super_bullets()
找到所有敌方已经发射的超级子弹，返回值是一个list，每一个元素都是一个字典,例如其中一个元素为
`{"type":1,"team":1001,"x":0,"y":0, "direction":"down"}`


#### find_all_road_nearby((x,y))
找到这个坐标附近可以走的点
返回一个复合元组，((x, y), direction)
示例
```python
for coordinate, direction in Game.find_all_road_nearby((1,2)).iteritems():
	pass
```
> 其中coordinate还是二元组的形式，这个会排除掉已经标为危险区域的点

#### set_string_map()
初始化一个字符格式的地图

#### make_string_map()
制作/更新一个字符格式的地图

#### set_tank_msg()
设置坦克信息（正常版）
特别注意，一定要在每回合开始调用

#### set_zx_tank_msg()
设置坦克信息（对象格式）
特别注意，一定要在每回合开始调用
#### find_all_our_tank()
得到我方所有坦克的信息,list形式，每个元素都是一个字典
```
{"id":0,"team":1001,"x":0,"y":1, "super_bullet":0}
```

## Strategy类
这个类是一个纯粹的方法类，每回合开始在Game类之后实例化

### 方法列表
####