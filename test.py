from abc import ABC, abstractmethod
from enum import Enum

class SpotType(Enum):
    Compact, large, MotorBike, Electric = 1, 2, 3, 4

class Address:
    def __init__(self, street, city, state, zip, country):

class Person:
    def __init__(self, name, email, adress, phone):
        self.__name = name
        self.__address = adress
        self.__email = email
        self.__phone = phone

class Account:
    def __init__(self, username, password, accountStatus, person):

    def reset_password(self):
        pass

class Admin(Account):
    def __init__(self, username, password, accountStatus, person):
        super.__init__(username, password, accountStatus, person)

    def addParkingFloor(self):
    def addParkingSPot(self):
    def addParkingDisplayBoard(self):
    def add_entrance_panel(self):
    def add_exit_panel(self):

class ParkingAttendant(Account):
    def __init__(self, username, password, accountStatus, person):
        super.__init__(username, password, accountStatus, person)

    def process_ticket(self, ticket_number):
        pass

class ParkingSpot:
    def __init__(self, name, spot_type):
    def is_free(self):
    def assignVehicle(self, vehicle):
    def removeVehicle(self):

class Compact(ParkingSpot):
    def __init__(self, number):
        super.__init__(number, spotType)

class ParkingFloor:
    def __init__(self, name):
        self.__displayBoard = ParkingDisplayBoard()

    def add_parking_spot(self, spot):
        switcher = {
            SpotType.Compact = self.__compact_spot.put(spot.get_number, spot)
        }

    def assign_vehicleToSpot(self,vehicle, spot):
        self.updateDisplatyBoard(spot)

    def updateDisplayBoard(self, spot):



class ParkingDisplayBoard:
    def __init__(self, floor_number):
        self.__electric_free_spot = None

    def show_message(self):








