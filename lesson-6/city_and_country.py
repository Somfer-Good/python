from math import sqrt, pow

class Coordinates:
    def __init__(self,latitude, longitude):
        self.x = latitude
        self.y = longitude
    
    def distance(self, other) -> float:
        return sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))

class City:
    def __init__(self, name, population, coords):
        self._name = name
        self._population = population
        self._coords = coords

    def distanceBetweenCities(self, other) -> float:
        return self._coords.distance(other._coords)

    def printCoords(self):
        print('(', self._coords.x, ':', self._coords.y, ')')

class Country:
    def __init__(self, name, capital, cities):
        self._name = name
        self._capital = capital
        self._cities = cities
        self._population = 0
        if len(cities) != 0:
            for city in cities:
                self._population += city._population

    def addCity(self, city):
        self._cities.append(city)
        self._population += city._population

    def print(self):
        print(self._name, self._capital._name, self._population)

    def findMinimumDistanceBetweenCities(self):
        if len(self._cities) < 2:
            print("Нельзя определить наименьшее расстояние. В стране только один город")
            return
        distance = self._cities[0].distanceBetweenCities(self._cities[1])
        for i in range(2, len(self._cities)):
            tmpDist = self._cities[0].distanceBetweenCities(self._cities[i])
            distance = min(distance, tmpDist)
        for i in range(1, len(self._cities)):
            for j in range(i + 1, len(self._cities)):
                tmpDist = self._cities[i].distanceBetweenCities(self._cities[j])
                distance = min(distance, tmpDist)
        print("Наименьшее расстояние между городами:", distance)

    def findDistanceBetweenCities(self, name):
        if len(self._cities) < 2:
            print("Нельзя определить наименьшее расстояние. В стране только один город")
            return
        tmpCity = City("", 0, Coordinates(0,0))
        for city in self._cities:
            if city._name == name:
                tmpCity = city
                break
        if tmpCity._name == "":
            print("Нельзя определить наименьшее расстояние. В стране нет такого города")
            return
        idx = 0 if self._cities[0]._name != tmpCity._name else 1
        distance = self._cities[idx].distanceBetweenCities(tmpCity)
        otherCity = self._cities[idx]
        for city in self._cities:
            if city._name != name:
                if distance > city.distanceBetweenCities(tmpCity):
                    otherCity = city
                    distance = city.distanceBetweenCities(tmpCity)
        print("Самый близжайший город к", tmpCity._name,":", otherCity._name, ". Расстояние равняется", distance)  
        print("Координаты", otherCity._name, ":")
        otherCity.printCoords()
        print("Координаты", tmpCity._name,":")
        tmpCity.printCoords()