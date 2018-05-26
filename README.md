# tank_api
软通的坦克操作api
## Control类
该类分为两个大部分，即`Move`和`Shot`

### Move（移动）
函数原型
```python
def Move(self, player_id, direction):
	return True # 成功
	return False #失败 
```
- `player_id` : 需要移动的坦克的id，需要是int类型。
- `direction` : 移动的方向，是字符串类型，有"up", "down", "right", "left"四个方向。
> 返回失败可能是你撞墙了。
> 每次只行动一格。

调用示例
```python
Control.Move(1,"left") #id为1的坦克向左移动一格。
```

### Fire（射击）
函数原型
```python
def Fire(self, player_id, direction, type = 0):
	pass
```
- `player_id` : 需要移动的坦克的id，需要是int类型。
- `direction` : 移动的方向，是字符串类型，有"up", "down", "right", "left"四个方向。
- `type`: 默认是0，代表是普通子弹，一般不需要传。可以专门设置为1，代表超级子弹。

```
Control.Fire(1,'up') #向上发射一发普通子弹
Control.Fire(1,'up',type = 1) # 向上发射一发超级子弹
```

## Map


首先确定一件事，那就是地图的信息会存在一个Map实例的二维数组里,位置就是坐标
### 属性列表

#### ROUND_ID
记录了回合数
#### death_trap
记录了是否是death_trap（就是在这里下回合一定会死）
### 方法列表
#### get_terrain(void)
`Map.get_terrain()`
返回值是字符串，有几种类型
- `"road"` -> 正常可以前进的路
- `"brick"` —> 砖墙
- `"iron"` -> 铁墙
- `"river"` -> 河流格子

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
### 属性列表
#### TEAM_ID
记录了我方的队伍ID
#### WIDTH
记录了地图的宽度（x坐标）
#### HEIGHT
记录了地图的长度（y坐标）
### 方法列表
#### find_all_coins()
返回一个字典 格式是
```
{"x":3,"y":2, "point":1}
```

#### find_all_stars()
返回一个字典 格式是
```
{"x":3,"y":2}
```

#### find_all_enemy()
返回敌方所有坦克的坐标的list
每一个元素的格式是一个字典
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


#### find_all_road_nearby((x,y))
返回一个复合元组，((x, y)irection)
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

#### set_zx_tank_msg()
设置坦克信息（对象格式）

#### find_all_our_tank()
得到我方所有坦克的信息,list形式，每个元素都是一个字典
```
{"id":0,"team":1001,"x":0,"y":1, "super_bullet":0}
```nate还是二元组的形式，这个会排除掉已经标为危险区域的点
