class Tank(object):
    super_bullets = False
    where_to_go = None
    last_fire_where = "up"
    active = False

    def __init__(self, coordinate=(-1, -1), tank_id=-1):
        self.coordinate = coordinate
        self.tank_id = tank_id

    def set_where_to_go(self, coordinate):
        self.where_to_go = coordinate

    def set_super_bullet(self):
        self.super_bullets = True

    def lose_super_bullet(self):
        self.super_bullets = False

    def change_coordinate(self, coordinate):
        self.coordinate = coordinate

