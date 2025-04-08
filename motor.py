class Motor:
    def __init__(self):
        self.speed=0.0

    def set_speed(self, speed):
        speed = max(-1, speed)
        speed = min(1,speed)
        self.speed = speed

    def get_speed(self):
        return self.speed

    def speed_up(self):
        self.speed = 2 * self.speed

    def slow_down(self):
        self.speed = 0.5 * self.speed

    def stop(self):
        self.speed = 0.0

    def reverse(self):
        self.speed=-1*self.speed

