import sm
class Delay2Machine(sm.SM):
    def __init__(self, val0, val1):
        self.startState = (val0, val1)
        pass
    def getNextValues(self, state, inp):
        (previousPreviousInput, previousInput) = state
        return ((previousInput, inp), previousPreviousInput)


if __name__ == "__main__":
    sm = Delay2Machine(100, 10)
    print(sm.transduce([1, 2, 10, 20, 30, 35]))
