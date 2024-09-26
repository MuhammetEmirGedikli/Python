class Squares():

    def __init__(self, max):
        self.max = max
        self.power = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.power <= self.max:
            result = self.power ** 2
            self.power += 1
            return result

        else:
            self.power = 0
            raise StopIteration


a = int(input("Enter a number: "))
square = Squares(a)
iterator = iter(square)

for i in range(1, a + 1):
    print(f"The square of {i} is =", next(iterator))
