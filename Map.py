
class Map(object):
    is_there_tank = False
    is_our_tank = False
    tank_id = 0
    super_bullet_with_tank = False
    coins = 0
    stars = False
    death_trap = False
    is_there_bullet = False
    bullet_direction = None
    bullet_type = 0
    is_our_bullet = False
    is_enemy_bullet = False
    terrain = 0

    def __init__(self, round_id, coordinate):
        self.ROUND_ID = round_id
        self.coordinate = coordinate

    def add_tank_id(self, is_our_tank, tank_id, super_bullet_with_tank):
        self.is_there_tank = True
        self.is_our_tank = is_our_tank
        self.tank_id = tank_id
        self.super_bullet_with_tank = super_bullet_with_tank

    def add_enemy_bullets(self, bullet_direction, bullet_type):
        self.is_enemy_bullet = True
        self.is_there_bullet = True
        self.bullet_type = bullet_type
        self.bullet_direction = bullet_direction

    def add_our_bullets(self, bullet_direction, bullet_type):
        self.is_our_bullet = True
        self.is_there_bullet = True
        self.bullet_type = bullet_type
        self.bullet_direction = bullet_direction

    def change_coins(self, coins):
        self.coins = coins

    def change_stars(self, star):
        self.stars = star

    def change_terrain(self, terrain):
        self.terrain = terrain

    def clear_map(self):
        self.is_there_tank = False
        self.is_our_tank = False
        self.tank_id = 0
        self.super_bullet_with_tank = False
        self.coins = 0
        self.stars = False
        self.death_trap = False
        self.is_there_bullet = False
        self.bullet_direction = None
        self.bullet_type = 0
        self.is_our_bullet = None
        self.is_enemy_bullet = False
        self.terrain = 0

    def get_terrain(self):
        return self.terrain

    def get_coins(self):
        return self.coins

    def get_stars(self):
        return self.stars

    def get_coordinate(self):
        return self.coordinate

    def get_tank_id(self):
        return self.is_there_tank, self.is_our_tank, self.tank_id, self.super_bullet_with_tank

    def get_enemy_bullets(self):
        return self.is_enemy_bullet, self.bullet_direction, self.bullet_type

    def get_our_bullets(self):
        return self.is_our_bullet, self.bullet_direction, self.bullet_type


