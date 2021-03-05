WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Food:
    def __init__(self, time, temp, pressure, desired_state):
        self.time = time
        self.temp = temp
        self.pressure = pressure
        self.desired_state = desired_state

    def is_cooking_criteria_satisfied(self):
        return self.is_well_done() or self.is_medium()

    def is_well_done(self):
        return self.desired_state == 'well-done' and  \
            self.get_cooking_progress() >= WELL_DONE

    def is_medium(self):
        return self.desired_state == 'medium' and  \
            self.get_cooking_progress() >= MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temp * self.pressure * COOKED_CONSTANT

food = Food(30, 103, 20, 'well-done')

if food.is_cookeding_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')