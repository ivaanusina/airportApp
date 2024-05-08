from airport import Airport
from controllerairport import ControllerAirport
import apiairport

airport_controller = ControllerAirport()
AirportObject = Airport()

while True:
    print("AIRPORT DATABASE")
    print("----------------------------")
    print("1.- Import an airport")
    print("2.- Delete an airport")
    print("3.- Add a flight operator to an airport")
    print("4.- Delete a flight operator from an airport")
    print("5.- List airports by operators")
    print("6.- List number of planes by operator – (by airport / all)")
    print("7.- Exit")
    option = int(input("Choose option:"))

    if option == 1:
        iata = str(input("Enter IATA:"))
        AirportObject = apiairport.getInfoAirport(iata)
        if airport_controller.addAirport(iata, AirportObject):
            print("Import airport with Iata " + iata + " successfully!")
        else:
            print("This airport is already imported")

    elif option == 2:
        iata = str(input("Enter IATA:"))
        if airport_controller.deleteAirport(iata):
            print("Delete airport with Iata " + iata + " successfully!")
        else:
            print("This airport is not imported")

    elif option == 3:
        iata = str(input("Which Iata airport do you want to add the flight operator to?"))
        if airport_controller.checkIata(iata):
            name = str(input("Enter name the flight operator:"))
            planes = str(input("How many plans does this flight operator have?"))
            airport_controller.addFlightOperator(iata, name, planes)
            print("Flight operator has been added successfully!")
        else:
            print("This airport is not imported")

    elif option == 4:
        iata = str(input("Which Iata airport do you want to remove the flight operator from?"))
        if airport_controller.checkIata(iata):
            name = str(input("Enter the name of the flight operator you want to delete:"))
            airport_controller.deleteFlightOperator(iata, name)
            print("Flight operator has been deleted successfully!")
        else:
            print("This airport is not imported")

    elif option == 5:
        operator = input("Enter the name of the flight operator: ")
        print(airport_controller.listAirportsByOperators(operator))
        print("hola")

    elif option == 6:
        iata = str(input("Enter IATA of the airport (or 'all' for all airports): "))
        operator = str(input("Enter the name of the flight operator: "))
        print(airport_controller.listPlanesByOperator(iata, operator))

    elif option == 7:
        print("Bye!!")
        break

    else:
        print("Choose one coreect option [1-7]")


