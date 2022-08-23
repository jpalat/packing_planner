import pickle
import os.path

class Item:
    def __init__(self) -> None:
        pass
    


class Inventory:
    inventory = []

    def __init__(self) -> None:
        self.filename = '.pplan_inv.pkl'
        if os.stat(self.filename).st_size == 0:
            print('File is empty')
        else:
            self.loadInventory()
                
    
    def addItem(self, item):
        self.inventory.append(item)
    
    def loadInventory(self):
        print("Load Inventory")
        inputFile = open(self.filename, 'rb')
        self.inventory = pickle.load(inputFile)        
        inputFile.close()

    def saveInventory(self):
        print("Save Inventory")
        pp = []
        for i in self.inventory:
            print(i)
            pp.append(i)
        outputFile = open(self.filename, 'wb')
        pickle.dump(pp, outputFile)
        outputFile.close()

    def printInventory(self):
        print("Print Inventory")
        for i in self.inventory:
            print(i)


    def removeItem(self, index):
        print("Remove item at Index" + index)

