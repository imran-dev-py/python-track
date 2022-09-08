class Phone():

    def __init__(self, price, band):
        self.price = price
        self.band = band

    def getPrice(self):
        return self.price

    def getBand(self):
        return self.band


phone = Phone(band='Samsung', price=15000)
print(phone.getBand())
print(phone.getPrice())
