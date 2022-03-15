#Day Trip Generator
from operator import truediv
import random

destinations = ["Hogwarts", "Tatooine", "Gallifrey", "Middle-earth"]
transportations = ["67 Chevy Impala", "Tardis", "Broomstick", "Port Key"]
restaurants = ["The Three Broomsticks Inn", "The Mos Eisley Cantina", "Harvelle's Roadhouse", "The Prancing Pony Inn"]
entertainments = ["Bilbo Baggins Birthday Party", "Playing Holochess with Chewbacca", "Fighting off Cybermen with The Doctor", "Play a game of quidditch" ]

def get_list_len(list):
    list_len = len(list)
    return list_len
def get_random_element(list, list_len):
    random_index = random.randrange(0,list_len)
    return list[random_index]
def generate_destination():
    destination = get_random_element(destinations, get_list_len(destinations))
    return destination
def generate_transportation():
    transportation = get_random_element(transportations, get_list_len(transportations))
    return transportation
def generate_restaurant():
    restaurant = get_random_element(restaurants, get_list_len(restaurants))
    return restaurant
def generate_entertainment():
    entertainment = get_random_element(entertainments, get_list_len(entertainments))
    return entertainment
def change_destination(trip_list):
    new_destination = trip_list[0]
    while new_destination == trip_list[0]:
        new_destination = generate_destination()
    return new_destination
def change_transportation(trip_list):
    new_transportation = trip_list[1]
    while new_transportation == trip_list[1]:
        new_transportation = generate_transportation()
    return new_transportation
def change_restaurant(trip_list):
    new_restaurant = trip_list[2]
    while new_restaurant == trip_list[2]:
        new_restaurant = generate_restaurant()
    return new_restaurant
def change_entertainment(trip_list):
    new_entertainment = trip_list[3]
    while new_entertainment == trip_list[3]:
        new_entertainment = generate_entertainment()
    return new_entertainment
def create_trip():
    trip = []
    trip.append(generate_destination())
    trip.append(generate_transportation())
    trip.append(generate_restaurant())
    trip.append(generate_entertainment())
    return trip
def print_trip(trip):
    print( f"You will be traveling to {trip[0]} using a {trip[1]}. You will be dinning at {trip[2]} and tonights entertainment will be {trip[3]}." )
def user_satisfied():
    user_input = input("Are you happy with this trip? Enter y/n: ")
    user_input = user_input.lower()
    if user_input == 'y':
        return True
    else:
        return False
def change_trip():
    user_input = int(input("What would you like to change 1. destination 2. transportation 3. restaurant 4. entertainment: "))
    if user_input == 1:
            user_confirm = False
            while user_confirm == False:
                destination = change_destination(final_trip)
                if input(f"We selected {destination} for you. Would you like to change again? y/n: ") == "y":
                    final_trip.pop(0)
                    final_trip.insert(0, destination)
                else:
                    final_trip.pop(0)
                    final_trip.insert(0, destination)
                    user_confirm = True
    elif user_input == 2:
            user_confirm = False
            while user_confirm == False:
                transportation = change_transportation(final_trip)
                if input(f"We selected {transportation} for you. Would you like to change again? y/n: ") == "y":
                    final_trip.pop(1)
                    final_trip.insert(1, transportation)
                else:
                    final_trip.pop(1)
                    final_trip.insert(1, transportation)
                    user_confirm = True
    elif user_input == 3:
            user_confirm = False
            while user_confirm == False:
                restaurant = change_restaurant(final_trip)
                if input(f"We selected {restaurant} for you. Would you like to change again? y/n: ") == "y":
                    final_trip.pop(2)
                    final_trip.insert(2, restaurant)
                else:
                    final_trip.pop(2)
                    final_trip.insert(2, restaurant)
                    user_confirm = True
    elif user_input == 4:
            user_confirm = False
            while user_confirm == False:
                entertainment = change_entertainment(final_trip)
                if input(f"We selected {entertainment} for you. Would you like to change again? y/n: ") == "y":
                    final_trip.pop(3)
                    final_trip.insert(3, entertainment)
                else:
                    final_trip.pop(3)
                    final_trip.insert(3, entertainment)
                    user_confirm = True

def run():
    print("Wellcome to the Day Trip Generator")
    print_trip(final_trip)
    while user_satisfied() == False:
        change_trip()
    print("\nYou have selected your final trip:")
    print_trip(final_trip)
final_trip = create_trip()
run()