# Define the class that we'll be using for our inventory
class DealerVehicle:
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return (f'Make: {self.make}\n'
                f' Model: {self.model}\n'
                f' Color: {self.color}\n'
                f' Year: {self.year}\n'
                f' Miles: {self.mileage}')


# Defining the method, so we can add vehicles to the list
def add_vehicle(make, model, color, year, mileage):
    inventory.append(DealerVehicle(make, model, color, year, mileage))


# Define method to remove a vehicle from the list
def remove_vehicle(index):
    inventory.pop(index)


inventory = []

menu = input('What would you like to do?\n'
             '  1: View Vehicles\n'
             '  2: Add Vehicle\n'
             '  3: Remove a vehicle\n'
             '  Input menu option: ')

# Menu option to view inventory
while menu != 'quit':
    if menu == '1':
        if len(inventory) > 0:
            for i, vehicle in enumerate(inventory):
                print(i, "\n", inventory[i])
                print()
        else:
            print('Inventory is empty, add a vehicle(s)\n')

    # Menu option to add a vehicle
    elif menu == '2':
        make = str(input('What is the Make of the vehicle?\n'))
        model = str(input('What is the Model of the vehicle?\n'))
        color = str(input('What is the Color of the vehicle?\n'))
        year = int(input('What is the Year of the vehicle?\n'))
        mileage = int(input('What is the Mileage of the vehicle?\n'))
        add_vehicle(make, model, color, year, mileage)
        print('Vehicle Added!')

    # Menu option to remove a vehicle
    elif menu == '3':
        if len(inventory) > 0:
            what_to_pop = int(input('What vehicle to remove:\n'))
            remove_vehicle(what_to_pop)
        else:
            print('no vehicles to remove')

    menu = input('What would you like to do?\n'
                 '  1: View Vehicles\n'
                 '  2: Add Vehicle\n'
                 '  3: Remove a vehicle\n'
                 '  Input menu option: ')
