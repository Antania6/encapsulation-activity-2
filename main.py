class computer:
    def __init__(self):
        self.__maxprize = 900

    def sell(self):
        print(f"selling prize is {self.__maxprize}")

    def set_max_prize(self,abc):
        self.__maxprize = abc


obj = computer()
obj.sell()
obj.__maxprize = 1500
obj.sell()

obj.set_max_prize(1000)
obj.sell()