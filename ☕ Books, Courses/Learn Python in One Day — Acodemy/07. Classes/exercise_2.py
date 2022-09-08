class Smartphone():

    def __init__(self, price, band, screensize):
        self.price = price
        self.band = band
        self.screensize = screensize

    def getBand(self):
        return self.band

    def getPrice(self):
        return self.price

    def getScreensize(self):
        return self.screensize

    def phone_info(self):
        print(self.getPrice())
        print(self.getBand())
        print(self.getScreensize())


smartphone = Smartphone(15000, 'Nokia', 5.6)
smartphone.phone_info()
