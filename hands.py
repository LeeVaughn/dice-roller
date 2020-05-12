from dice import D6

class Hand(list):
    def __init__(self, size = 0, die_class = None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")

        super().__init__()

        # appends dice to list
        for _ in range(size):
            # creates a number of Dice instances based on size
            self.append(die_class())

        # sorts dice
        self.sort()

class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size = 5, die_class = D6, *args, **kwargs)
