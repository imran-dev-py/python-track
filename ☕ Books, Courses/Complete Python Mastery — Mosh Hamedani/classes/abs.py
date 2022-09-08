# Abstract Base Class

from abc import ABC, abstractmethod


class Stream(ABC):
    def open(self):
        pass

    def close(self):
        pass

    @abstractmethod
    def read(self):
        pass


class fileStream(Stream):
    def read(self):
        print('Reading data from file stream')


class networkStream(Stream):
    def read(self):
        print('Reading data from network stream')

class memoryStream(Stream):
    def read(self): # no Error in console
        print('Writting')


stream = memoryStream()  # TypeError
stream.close()

"""
* A is an abstract concept and we shouldn't call directly instance of that class
always instance subclass
* so solve this problem we need to import abc[ABC, abstractmethod]
and define commnad interface in abstract class
* if want to create new class[subclass] and if it has no method called read it throws error and
treat as abstract class until it has read method
"""
