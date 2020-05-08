import random


class Die:
    def __init__(self, sides = 2, value = 0):
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")

        self.value = value or random.randint(1, sides)

# prints a random number between 1 and 2
d = Die()
print(d.value)

# prints a random number between 1 and 20
d20 = Die(sides = 20)
print(d20.value)

# prints 6
six = Die(value = 6)
print(six.value)
