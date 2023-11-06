import requests
from airport import Airport

def getInfoAirport(iata):
    url = "https://airport-info.p.rapidapi.com/airport"

    querystring = {"iata":str(iata)}

    headers = {
        "X-RapidAPI-Key": "4eab2a45ccmsh7b37f676aa9044fp1d7006jsn2f75b4254563",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    AirportObject = Airport()
    AirportObject.setIata(data['iata'])
    AirportObject.setName(data['name'])
    AirportObject.setLocation(data['location'])
    AirportObject.setCity(data['city'])
    AirportObject.setCountry(data['country'])
    AirportObject.setWebsite(data['website'])
    AirportObject.setPhone(data['phone'])
    
    return AirportObject


    

