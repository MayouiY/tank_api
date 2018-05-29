class Strategy(object):

    def __init__(self, game):
        self.game = game

    def find_bullets_down(self, coordinate):
        bullets = []
        for bullet in self.game.find_all_bullets():
            if bullet["x"] == coordinate[0] and bullet["y"] > coordinate[1] and bullet["direction"] is "up":
                if self.game.find_blocks_with_y(coordinate[1], bullet["y"], coordinate[0]) == {}:
                    cp_bullet = bullet.copy()
                    cp_bullet["distance"] = bullet["y"] - coordinate[1]
                    bullets.append(cp_bullet)

        return bullets

    def find_bullets_up(self, coordinate):
        bullets = []
        for bullet in self.game.find_all_bullets():

            if bullet["x"] == coordinate[0] and bullet["y"] < coordinate[1] and bullet["direction"] is "down":
                if self.game.find_blocks_with_y(coordinate[1], bullet["y"], coordinate[0]) == {}:
                    cp_bullet = bullet.copy()
                    cp_bullet["distance"] = coordinate[1] - bullet["y"]
                    bullets.append(cp_bullet)

        return bullets

    def find_bullets_left(self, coordinate):
        bullets = []
        for bullet in self.game.find_all_bullets():
            if bullet["y"] == coordinate[1] and bullet["x"] < coordinate[0] and bullet["direction"] is "right":
                if self.game.find_blocks_with_x(coordinate[0], bullet["x"], coordinate[1]) == {}:
                    cp_bullet = bullet.copy()
                    cp_bullet["distance"] = coordinate[1] - bullet["y"]
                    bullets.append(cp_bullet)

        return bullets

    def find_bullets_right(self, coordinate):
        bullets = []
        for bullet in self.game.find_all_bullets():
            if bullet["y"] == coordinate[1] and bullet["x"] > coordinate[0] and bullet["direction"] is "left":
                if self.game.find_blocks_with_x(coordinate[0], bullet["x"], coordinate[1]) == {}:
                    cp_bullet = bullet.copy()
                    cp_bullet["distance"] = bullet["y"] - coordinate[1]
                    bullets.append(cp_bullet)

        return bullets

    def find_bullets_dangers(self, tank, direction):
        coordinate = tank.coordinate
        bullets = []
        if direction == "up":
            bullets = self.find_bullets_up(coordinate)
        elif direction == "down":
            bullets = self.find_bullets_down(coordinate)
        elif direction == "left":
            bullets = self.find_bullets_left(coordinate)
        elif direction == "right":
            bullets = self.find_bullets_right(coordinate)

        return bullets

    def find_all_bullets_dangers(self, coordinate):
        all_bullet_danger = {}
        all_bullet_danger["left"] = self.find_bullets_left(coordinate)
        all_bullet_danger["right"] = self.find_bullets_right(coordinate)
        all_bullet_danger["up"] = self.find_bullets_up(coordinate)
        all_bullet_danger["down"] = self.find_bullets_down(coordinate)
        return all_bullet_danger


