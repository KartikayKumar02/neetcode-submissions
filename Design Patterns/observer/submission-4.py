class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.observer_list = []

    def subscribe(self, observer: Observer) -> None:
        self.observer_list.append(observer)
        

    def unsubscribe(self, observer: Observer) -> None:
        self.observer_list.remove(observer)
        

    def updateStock(self, newStock: int) -> None:
        prev = self.stock
        self.stock = newStock
        if prev == 0 and self.stock > 0:
            for o in self.observer_list:
                o.notify(self.itemName)
        
