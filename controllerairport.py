from airport import Airport

class ControllerAirport:
    def __init__(self):
        self.__airports = {}

    def addAirport(self, iata, AirportObject):
        if iata not in self.__airports:
            self.__airports[iata] = AirportObject
            return True
        else:
            return False
        
    def deleteAirport(self, iata):
        if iata in self.__airports:
            self.__airports.pop(iata)
            return True
        else:
            return False
        
    def checkIata(self, iata):
        if iata in self.__airports:
            return True
        else:
            return False
        
    def addFlightOperator(self, iata, name, planes):
        if iata in self.__airports:
            airport = self.__airports[iata]
            airport.addFlightOperator(name, planes)
            return True
        return False

    def deleteFlightOperator(self, iata, name):
        if iata in self.__airports:
            airport = self.__airports[iata]
            return airport.deleteFlightOperator(name)
        return False

    def listAirportsByOperators(self, operator):
        result = "Airports working with the specified operator:\n"
        for iata, airport in self.__airports.items():
            operators = airport.getFlightOperators()
            if operator in operators:
                result += f"{iata}\n"
                result += f"\t{airport.getName()}\n"
                result += f"\t{airport.getLocation()}\n"
                result += f"\t{airport.getCity()}\n"
                result += f"\t{airport.getCountry()}\n"
                result += f"\t{airport.getWebsite()}\n"
                result += f"\t{airport.getPhone()}\n"
                result += "\tFlight Operators:\n"
                for operator, planes in operators.items():
                        result += f"\t\t{operator}: {planes} planes\n"
        return result

    def listPlanesByOperator(self, iata, operator):
        if iata == 'all':
            result = ""
            for iata, airport in self.__airports.items():
                planes = airport.getFlightOperators()
                if operator in planes:
                    result += f"{iata} - {airport.getName()} - {planes[operator]} planes\n"
            return result
        elif iata in self.__airports:
            airport = self.__airports[iata]
            planes = airport.getFlightOperators()
            if operator in planes:
                return f"{iata} - {airport.getName()} - {planes[operator]} planes"
        else:
            return "This airport is not imported"
    