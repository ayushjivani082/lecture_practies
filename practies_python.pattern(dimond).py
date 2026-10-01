
# pattern

rows = int(input("Enter number of rows:"))
for i in range(1 , rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(rows-1,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()





'''



class Vehicle:
    def __init__(self, vehicle_id="", brand="", model="",
                 rental_price_per_day=0, availability_status="Available"):

        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.__rental_price_per_day = rental_price_per_day
        self.__availability_status = availability_status
        self.__renter_id = None

        # New payment and rental details
        self.__rental_days = 0
        self.__total_rent = 0
        self.__payment_received = 0

    def get_rental_price(self):
        return self.__rental_price_per_day

    def set_rental_price(self, price):
        self.__rental_price_per_day = price

    def get_availability_status(self):
        return self.__availability_status

    def set_availability_status(self, status):
        self.__availability_status = status

    def get_renter_id(self):
        return self.__renter_id

    def set_renter_id(self, renter_id):
        self.__renter_id = renter_id

    # New method for rental days
    def set_rental_days(self, days):
        self.__rental_days = days
        self.__total_rent = self.__rental_price_per_day * days

    def get_rental_days(self):
        return self.__rental_days

    def get_total_rent(self):
        return self.__total_rent

    # New payment method
    def add_payment(self, amount):
        self.__payment_received += amount

    def get_payment_received(self):
        return self.__payment_received

    def get_remaining_payment(self):
        return self.__total_rent - self.__payment_received

    def display_payment(self):
        print("Rental Days:", self.__rental_days)
        print("Total Rent:", self.__total_rent)
        print("Payment Received:", self.__payment_received)
        print("Remaining Payment:", self.get_remaining_payment())

    def display(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rental Price per day:", self.get_rental_price())
        print("Availability:", self.get_availability_status())
        print("Renter ID:", self.get_renter_id())
        print("Rental Days:", self.get_rental_days())
        print("Total Rent:", self.get_total_rent())
        print("Payment Received:", self.get_payment_received())
        print("Remaining Payment:", self.get_remaining_payment())

    def rent(self, renter_id, days):
        if self.get_availability_status() == "Available":

            self.set_availability_status("Rented")
            self.set_renter_id(renter_id)
            self.set_rental_days(days)

            return True

        return False

    def return_vehicle(self):
        if self.get_availability_status() == "Rented":

            self.set_availability_status("Available")
            self.set_renter_id(None)

            return True

        return False


class Car(Vehicle):

    def __init__(self, vehicle_id, brand, model,
                 rental_price_per_day, number_of_seats, fuel_type):

        super().__init__(
            vehicle_id,
            brand,
            model,
            rental_price_per_day
        )

        self.number_of_seats = number_of_seats
        self.fuel_type = fuel_type

    def display(self):
        print("Car Details")
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rental Price per day:", self.get_rental_price())
        print("Seats:", self.number_of_seats)
        print("Fuel Type:", self.fuel_type)
        print("Availability:", self.get_availability_status())
        print("Renter ID:", self.get_renter_id())
        print("Rental Days:", self.get_rental_days())
        print("Total Rent:", self.get_total_rent())
        print("Payment Received:", self.get_payment_received())
        print("Remaining Payment:", self.get_remaining_payment())


class Bike(Vehicle):

    def __init__(self, vehicle_id, brand, model,
                 rental_price_per_day, bike_type):

        super().__init__(
            vehicle_id,
            brand,
            model,
            rental_price_per_day
        )

        self.bike_type = bike_type

    def display(self):
        print("Bike Details")
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rental Price per day:", self.get_rental_price())
        print("Bike Type:", self.bike_type)
        print("Availability:", self.get_availability_status())
        print("Renter ID:", self.get_renter_id())
        print("Rental Days:", self.get_rental_days())
        print("Total Rent:", self.get_total_rent())
        print("Payment Received:", self.get_payment_received())
        print("Remaining Payment:", self.get_remaining_payment())


vehicles = []


def find_vehicle(vehicle_id):

    for vehicle in vehicles:

        if vehicle.vehicle_id == vehicle_id:
            return vehicle

    return None


while True:

    print("\n--- Python OOP Project: Vehicle Rental Management System ---")
    print("--- Choose an operation ---")

    print("1. Add a Car")
    print("2. Add a Bike")
    print("3. Rent a Vehicle")
    print("4. Return a Vehicle")
    print("5. Show Vehicle Details")
    print("6. Make Payment")
    print("7. Check Payment Balance")
    print("8. Exit")

    choice = input("Enter your choice: ")


    # ADD CAR
    if choice == "1":

        brand = input("Enter Brand: ")
        model = input("Enter Model: ")
        vehicle_id = input("Enter Vehicle ID: ")
        price = float(input("Enter Rental Price per day: "))
        seats = int(input("Enter Number of Seats: "))
        fuel = input("Enter Fuel Type: ")

        if find_vehicle(vehicle_id) is not None:

            print("Vehicle ID already exists.")

        else:

            car = Car(
                vehicle_id,
                brand,
                model,
                price,
                seats,
                fuel
            )

            vehicles.append(car)

            print(
                f"Car created with brand: {brand}, "
                f"model: {model}, "
                f"ID: {vehicle_id}, "
                f"price: {price}, "
                f"seats: {seats}, "
                f"fuel: {fuel}."
            )


    # ADD BIKE
    elif choice == "2":

        brand = input("Enter Brand: ")
        model = input("Enter Model: ")
        vehicle_id = input("Enter Vehicle ID: ")
        price = float(input("Enter Rental Price per day: "))
        bike_type = input("Enter Bike Type: ")

        if find_vehicle(vehicle_id) is not None:

            print("Vehicle ID already exists.")

        else:

            bike = Bike(
                vehicle_id,
                brand,
                model,
                price,
                bike_type
            )

            vehicles.append(bike)

            print(
                f"Bike created with brand: {brand}, "
                f"model: {model}, "
                f"ID: {vehicle_id}, "
                f"price: {price}, "
                f"type: {bike_type}."
            )


    # RENT VEHICLE
    elif choice == "3":

        vehicle_id = input("Enter Vehicle ID to rent: ")

        vehicle = find_vehicle(vehicle_id)

        if isinstance(vehicle, Vehicle):

            renter_id = input("Enter Renter ID: ")

            # New option for number of days
            days = int(input("Enter Number of Days to rent: "))

            if days <= 0:

                print("Number of days must be greater than 0.")

            else:

                if vehicle.rent(renter_id, days):

                    print("Vehicle rented successfully.")
                    print("Rental Days:", days)
                    print("Rental Price per day:",
                          vehicle.get_rental_price())
                    print("Total Rent:", vehicle.get_total_rent())

                else:

                    print("Vehicle is already rented.")

        else:

            print("Vehicle not found.")


    # RETURN VEHICLE
    elif choice == "4":

        vehicle_id = input("Enter Vehicle ID to return: ")

        vehicle = find_vehicle(vehicle_id)

        if isinstance(vehicle, Vehicle):

            if vehicle.return_vehicle():

                print("Vehicle returned successfully.")

            else:

                print("Vehicle is already available.")

        else:

            print("Vehicle not found.")


    # SHOW VEHICLE DETAILS
    elif choice == "5":

        if len(vehicles) == 0:

            print("No vehicles available.")

        else:

            print("\n--- Vehicle Details ---")

            for vehicle in vehicles:

                vehicle.display()

                print("------------------------")


    # MAKE PAYMENT
    elif choice == "6":

        vehicle_id = input("Enter Vehicle ID for payment: ")

        vehicle = find_vehicle(vehicle_id)

        if isinstance(vehicle, Vehicle):

            if vehicle.get_rental_days() == 0:

                print("Vehicle has not been rented yet.")

            else:

                print("Total Rent:", vehicle.get_total_rent())
                print("Payment Already Received:",
                      vehicle.get_payment_received())

                amount = float(input("Enter Payment Amount: "))

                if amount <= 0:

                    print("Payment amount must be greater than 0.")

                else:

                    vehicle.add_payment(amount)

                    print("Payment received successfully.")
                    print("Total Payment Received:",
                          vehicle.get_payment_received())
                    print("Remaining Payment:",
                          vehicle.get_remaining_payment())

        else:

            print("Vehicle not found.")


    # CHECK PAYMENT BALANCE
    elif choice == "7":

        vehicle_id = input("Enter Vehicle ID to check payment: ")

        vehicle = find_vehicle(vehicle_id)

        if isinstance(vehicle, Vehicle):

            print("\n--- Payment Details ---")
            print("Vehicle ID:", vehicle.vehicle_id)
            print("Rental Days:", vehicle.get_rental_days())
            print("Rental Price per day:",
                  vehicle.get_rental_price())
            print("Total Rent:", vehicle.get_total_rent())
            print("Payment Received:",
                  vehicle.get_payment_received())
            print("Remaining Payment:",
                  vehicle.get_remaining_payment())

        else:

            print("Vehicle not found.")


    # EXIT
    elif choice == "8":

        vehicles.clear()

        print("Exiting the system. All resources have been freed.")
        print("Goodbye!")

        break


    else:

        print("Invalid choice. Please try again.")


     
