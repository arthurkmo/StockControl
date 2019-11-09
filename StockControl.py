## Advanced Programming, coursework 1: Object Orientation
##
## The stock control system classes are unfinished.
## Work through the 14 steps of the coursework to
## implement and extend the methods and classes.
##
##

# No. 0

"""
Group members:
    Name:Opio Arthur Moses
    Reg:2018/HD05/3913U
    StudentNo:1800743685

    Name:Beinomugisha Edwin 
    Reg:2018/HD05/1948U
    StudentNo:1800737351

"""
from datetime import date

"""A stock control system"""



class StockControlSystemError(Exception):
    """Base class for exceptions in this module."""
    pass

class SoldOutOfStockError(StockControlSystemError):
    """Raised when an item is sold that isn't in stock
    Attributes:
    item -- item being sold
    """
    def __init__(self, item):
        self.item = item

class ItemNotFoundError(StockControlSystemError):
    """Raised when an item is sold that isn't in the stock list
    Attributes:
    barcode -- barcode of item being sold
    """
    def __init__(self, barcode):
        self.barcode = barcode


class StockItem(object):
    """Provides the basic stock item class for the stock control system. This keeps track of the particulars of the items in the stock"""

    def __init__(self, name, barcode, quantity):
        """Provides the basic stock item class for the stock control system
        name     -- name of product (string)
        barcode  -- barcode of product item (string)
        quantity -- number of items in stock (integer)
        """
        self.name = name;
        self.barcode = barcode;
        self.quantity = quantity;

    def toString(self):
        """Returns a string describing the stock item, its barcode and the quantity remaining"""
        #TODO complete this method
        description = "Stock Name: " + self.name + "\tBarcode: " + self.barcode + \
            "\tQty remaining: " + str(self.quantity)

        return description

    def needRestock(self):
        """Returns true if this item needs restocking (i.e. the quantity<a threshold)"""
        #TODO check if the quantity<threshold and return true if it is
        #we'll set for now the threshold at *five* items
        #so we need to check if self.quantity is less than five.
        threshold = 5
        if self.quantity < threshold:
            return True
        else:
            return False


    def sell(self):
        """Process the sale of an item, generates an exception if an item is sold when its stock is zero"""
        #TODO
        #hint: use the raise method to create an exception.
        if self.quantity < 1:
            raise SoldOutOfStockError(self.name)
        else:
            return 1
        # item getters
    def getName(self):
        return self.name

    def getBarcode(self):
        return self.barcode

    def getQuantity(self):
        return self.quantity

    # item setters
    def setName(self, name):
        self.name = name

    def setBarcode(self, barcode):
        self.barcode = barcode

    def setQuantity(self, quantity):
        self.quantity = quantity

        # No. 9
    def restockQuantity(self, quantity):
        self.quantity = self.quantity + quantity


class StockControl(object):
    """ The stock control system """

    def __init__(self):
        """The stock control system"""
        # note: We could have implemented the list as a dictionary, with
        # the barcode as the key, however if the barcode for the item
        # changes we might have problems.
        self.stocklist = []  # a list of stock items

    def listRestock(self):
        """Return a string listing items that need restocking"""
        # TODO return a list of items that need restocking
        # hint: Need to loop through the stocklist
        # No. 3
        flag = 0
        mystr = ""
        for item in self.stocklist:
            if StockItem.needRestock(item):
                mystr = mystr + StockItem.getName(item) + '\n'
                flag = flag + 1  # item that needs restocking found

        # No. 4
        if flag == 0:
            return "All items stocked"
        else:
            return mystr

    def addStockType(self, item):
        """Add an item to the stock list"""
        # TODO
        # hint: Add an item to this.stocklist
        # No. 6
        self.stocklist.append(item)

    def sellStock(self, barcode):
        """Process the sale of one item"""
        # TODO
        # hint: Look through the list of items
        # and call the 'sell' method of the relevant item
        # return an error if the product isn't found
        # No. 7
        invalid_barcode = 0
        for item in self.stocklist:
            if barcode == StockItem.getBarcode(item):
                invalid_barcode = 1
                if StockItem.sell(item) == 1:
                    # StockItem.setQuantity(StockItem, 0) find away of reducing the stock quantity
                    newQty = StockItem.getQuantity(item) - 1  # We reduce stock by one per item solid
                    StockItem.setQuantity(item, newQty)
                    print("Sold: Successfully: Qty remaining: ", StockItem.getQuantity(item))
                else:
                    raise SoldOutOfStockError()
        if invalid_barcode == 0:
            raise ItemNotFoundError(barcode)

    # No. 9
    def restock(self, barcode, quantity):
        invalid_barcode = 0
        for item in self.stocklist:
            if barcode == StockItem.getBarcode(item):
                invalid_barcode = 1
                StockItem.restockQuantity(item, quantity) # We set new quantity (current + new)
                print("Item Restocked Successfully: New Qty: ", StockItem.getQuantity(item))
        if invalid_barcode == 0:
            raise ItemNotFoundError(barcode)

# No. 10 & No. 11
class PerishableStockItem(StockItem):
    def __init__(self, name, barcode, quantity, sellbydate):
        super(PerishableStockItem, self).__init__(name, barcode, quantity)
        self.sellbydate = sellbydate
        self.name = name
        self.barcode = barcode
        self.quantity = quantity

    # No. 12
    def pastSellByDate(self):
        if date.today() > self.sellbydate:
            return True

    # No. 13
    # Override needRestock
    def needRestock(self):
        """Returns true if this item needs restocking (i.e. the quantity<a threshold)"""
        # TODO check if the quantity<threshold and return true if it is
        # we'll set for now the threshold at *five* items
        # so we need to check if self.quantity is less than five.

        threshold = 5
        if self.quantity < threshold or PerishableStockItem.pastSellByDate(self):
            return True
        else:
            return False

    # No. 14
    # Qverride the toString to display sellbydate.
    def toString(self):
        """Returns a string describing the stock item, its barcode and the quantity remaining"""
        # TODO complete this method
        # No. 1
        description = "Stock Name: " + self.name + "\tBarcode: " + self.barcode + \
            "\tQty remaining: " + str(self.quantity) + "\tSell by: " + str(self.sellbydate)

        return description

# Below is some code to test the classes. Feel free
# to alter this test-code to test your submission
# more thoroughly.
# Populate the stock control system
stockctrl = StockControl()

stockctrl.addStockType(StockItem('Museli', '0191', 5))  # 2
stockctrl.addStockType(StockItem('Flour (1kg)', '1191', 24))
stockctrl.addStockType(StockItem('Bag of Coffee', '1234', 2))  # 23
stockctrl.addStockType(StockItem('Salt and Vinegar Crisps', '4434', 5))  # 3
# uncomment to test the PerishableStockItem class for milk
# stockctrl.addStockType(PerishableStockItem('Milk (500ml)', '1191', 24, date(2013, 10, 10)))
stockctrl.addStockType(StockItem('Cookies', '2312', 6))
stockctrl.addStockType(StockItem('Bags of grapes', '1111', 6))  # 0

# Find out what needs restocking
print("Items that need restocking:\n")
print(stockctrl.listRestock())


# Sell some items
print("\n")
print("Testing sales:")
for barcode in ['1234', '2312', '1112', '1111', '2312', '1191', '0191', '2312']:
    try:
        stockctrl.sellStock(barcode)
    except SoldOutOfStockError as e:
        print("Stock sold which isn't in stock: " + e.item)
    except ItemNotFoundError as e:
        print("Item not found:" + e.barcode)

print("\nItems that need restocking:\n")
print(stockctrl.listRestock())

# Uncomment this section to test the restock method
print("\nRestocking...\n")
for barcode in ['1111', '0191', '2312', '4434', '2312', '9999']:
    try:
        stockctrl.restock(barcode, 10)
    except ItemNotFoundError as e:
        print("Item not found:" + e.barcode)

# print("\nItems that need restocking:\n")
# print(stockctrl.listRestock())

# p1 = PerishableStockItem('Milk (500ml)', '1191', 10, date(2019, 10, 2))
# print(p1.toString())
