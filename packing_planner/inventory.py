class Item:
    def __init__(self) -> None:
        pass
    


class Inventory:
    inventory = []
    
    def addItem(self, item):
        self.inventory.append(item)
    
    def loadInventory(self):
        print("Load Inventory")

    def saveInventory(self):
        print("Save Inventory")
        for i in self.inventory:
            print(i)

    def removeItem(self, index):
        print("Remove item at Index" + index)

