cars = 100
space_in_a_care = 4.0
drivers = 30
passengers  = 90
cars_not_driven = cars - drivers
carpool_capacity = car_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars "cars available.")
print("There are only", drivers, "drivers available.")
print("There are only", drivers, "Drivers available.")
print("We can transport", carpool_capacity, "people today.")
print("Wr have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
