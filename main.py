class computer:
    def __init__(self):
        self.maxprize = 900

    def sell(self):
        print(f"selling prize is {self.maxprize}")

    def set_max_prize(self,abc):
        self.maxprize = abc


obj = computer()
obj.sell()
print(obj.maxprize)
