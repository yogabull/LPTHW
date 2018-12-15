#code has operators and

# this is the number of cars available
cars = 100
#The next line is the number of people who can ride in the carself.
space_in_a_car = 4.0
#This is the number of drivers available.
drivers = 30
#below is the number of passengers.
passengers = 90
#below is equation for cars not driven which is the number of cars minus the number of drivers.
cars_not_driven = cars - drivers
#below equates the cars driven by the number of drivers.
cars_driven = drivers
#the number of cars driven multiplied by the space_in_a_car produces the carpool_capacity.
carpool_capacity = cars_driven * space_in_a_car
#the total passengers divided by the number of cars_driven reveals the average_passengers_per_car.
average_passengers_per_car = passengers  / cars_driven

print ("There are ", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
