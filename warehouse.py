from shop import shop
class item(shop):

    def __init__(self, name, buyprice, sellprice, quantity):
        self.name = name
        self.buyprice = buyprice
        self.sellprice = sellprices
        self.quantity = quantity
        self.allmoneyincrease = (sellprice-buyprice)*quantity

