import random


class Die:
    def __init__(self, sides = 2, value = 0):
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")

        self.value = value or random.randint(1, sides)

    # turns an instace of Die into an int
    def __int__(self):
        return self.value

    # magic methods to test equality of dice
    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        # could also be int(self) != other
        return not int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other


# extends Die class
class D6(Die):
    # overrides init
    def __init__(self, value = 0):
        super().__init__(sides = 6, value = value)


# # prints a random number between 1 and 2
# d = Die()
# print(d.value)

# # prints a random number between 1 and 6
# d6 = Die(sides = 6)
# print(d6.value)

# # prints 6
# six = Die(value = 6)
# print(six.value)

# # also prints a random number between 1 and 6
# d6 = D6()
# print(d6.value)
