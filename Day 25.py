country = ("India", "America", "Russia", "China","Germany","france")
# Convert the tuple to a list
country = list(country)
print(type(country))
print(country)
country.append("japan")
print(country)
country.pop(3)
print(country)
country.remove("America")
print(country)
country.insert(3,"japan")
print(country)
a=country.count("japan")
print(a)
# Convert the list back to a tuple
country = tuple(country)
print(country)
print(type(country))