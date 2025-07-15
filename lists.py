#create a list with the name of five cars and print

cars = ["audi", "honda", "mercedes", "jeep", "volvo"]

print(cars)

print(cars[4])

print(cars[3].title())

print(cars[-3])

message = f"my first car was a {cars[4].title()}"

print(message)

cars[0] = "toyota"
print(cars)

cars.append("audi")

print(cars)

#cars.reverse()

cars.insert(3,"bmw")

print(cars)

cars.remove("audi")

print(cars)

cars.append("Lincoln")

print(cars)

cars.insert(1, "Touareg")

print(cars)