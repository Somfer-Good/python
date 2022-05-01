import random
from city_and_country import Coordinates, City, Country

def printCountries(countries, sort):
    """Вывод стран с определённой сортировкой: alphabet или population"""
    if sort == "alphabet":
        list = sorted(countries, key=lambda x: x._name)
        for country in list:
            country.print()
    elif sort == "population":
        list = sorted(countries, key=lambda x: x._population, reverse=True)
        for country in list:
            country.print()
    else:
        return

def randfloat():
    return random.random() * 90

print("Страна 1", end='\n\n')

City1 = City("Город1", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City2 = City("Город2", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City3 = City("Город3", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City4 = City("Город4", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City5 = City("Город5", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))

Country1 = Country("Страна 1", City1, [City1, City2])

print("Добавление новых городов.", end='\n\n')
Country1.addCity(City3)
Country1.addCity(City4)
Country1.addCity(City5)

Country1.print()
print()

print("Страна 2", end='\n\n')

City6 = City("Город6", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City7 = City("Город7", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City8 = City("Город8", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City9 = City("Город9", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City10 = City("Город10", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))

Country2 = Country("Страна 2", City6, [City6, City7, City8, City9, City10])

Country2.print()
Country2.findMinimumDistanceBetweenCities()
print()

print("Страна 3", end='\n\n')

City11 = City("Город11", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City12 = City("Город12", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City13 = City("Город13", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City14 = City("Город14", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City15 = City("Город15", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))

Country3 = Country("Страна 3", City11, [City11, City12, City13, City14, City15])
Country3.print()

Country3.findDistanceBetweenCities("Город13")

print()

City16 = City("Город16", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City17 = City("Город17", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City18 = City("Город18", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City19 = City("Город19", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))
City20 = City("Город20", random.randint(100_000, 5_000_000), Coordinates(randfloat(),randfloat()))

Country4 = Country("Страна 4", City16, [City16, City17, City18, City19, City20])
Country4.print()

print("Печать стран отсортированных по населению", end='\n\n')
printCountries([Country1, Country2, Country3, Country4], "population")
print()

print("Печать стран отсортированных по алфавиту", end='\n\n')
printCountries([Country1, Country2, Country3, Country4], "alphabet")
print()