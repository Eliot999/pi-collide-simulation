from numba import njit

HEIGHT = 20


class Block:
    def __init__(self, HEIGHT, x, w, v, m):
        self.x = x
        self.y = HEIGHT - w
        self.w = w
        self.v = v
        self.m = m

    def collide(self, block):
        return self.x + self.w >= block.x or (self.x > block.x + block.w)

    def bounce(self, block):
        sum_M = self.m + block.m
        new_V = (self.m - block.m) / sum_M * self.v
        new_V += (2 * block.m / sum_M) * block.v
        return new_V

    def hit_wall(self):
        if self.x <= 0:
            return True
        return False

    def reverse(self):
        self.v *= -1

    def update(self):
        self.x += self.v

    def prep_show(self):
        return self.x, self.y, self.w, self.w
