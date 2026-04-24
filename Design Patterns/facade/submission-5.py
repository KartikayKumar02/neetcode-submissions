class Order:
    def __init__(self, contents: str, takeOut: bool):
        self.contents = contents
        self.takeOut = takeOut

    def getOrder(self) -> str:
        return self.contents

    def isTakeOut(self) -> bool:
        return self.takeOut

class Cashier:
    def takeOrder(self, contents: str, takeOut: bool) -> Order:
        return Order(contents, takeOut)

class Food:
    def __init__(self, order: str):
        self.contents = order

    def getFood(self) -> str:
        return self.contents

class Chef:
    def prepareFood(self, order: Order) -> Food:
        return Food(order.getOrder())

class PackagedFood(Food):
    def __init__(self, food: Food):
        super().__init__(food.getFood() + " in a bag")

class KitchenStaff:
    def packageOrder(self, food: Food) -> PackagedFood:
        return PackagedFood(food)

class DriveThruFacade:
    def __init__(self):
        self.cashier = Cashier()
        self.chef = Chef()
        self.kitchenStaff = KitchenStaff()
        self.new_order = None
        self.new_food = None

    def takeOrder(self, orderContents: str, takeOut: bool) -> Food:
        self.new_order = Order(orderContents, takeOut)
        self.new_food = self.chef.prepareFood(self.new_order)
        if self.new_order.isTakeOut():
            return self.kitchenStaff.packageOrder(self.new_food)
        return self.new_food


