class Airport:
    def __init__(self):
        self.__iata = ""
        self.__name = ""
        self.__location = ""
        self.__city = ""
        self.__country = ""
        self.__website = ""
        self.__phone = ""
        self.__flightOperators = {}

    def getIata(self):
        return self.__iata

    def setIata(self, iata):
        self.__iata = iata

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getLocation(self):
        return self.__location

    def setLocation(self, location):
        self.__location = location

    def getCity(self):
        return self.__city

    def setCity(self, city):
        self.__city = city

    def getCountry(self):
        return self.__country

    def setCountry(self, country):
        self.__country = country

    def getWebsite(self):
        return self.__website

    def setWebsite(self, website):
        self.__website = website

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    def getFlightOperators(self):
        return self.__flightOperators

    def setFlightOperators(self, flightOperators):
        self.__flightOperators = flightOperators
    
    def addFlightOperator(self, name, planes):
        self.__flightOperators[name] = planes

    def deleteFlightOperator(self, name):
        if name in self.__flightOperators:
            del self.__flightOperators[name]
            return True
        return False

