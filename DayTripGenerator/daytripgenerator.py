#Create random choices
import random

# Define lists
restaurants = ['Freddys Pizza', 'Burger King', 'Red Lobster', 'Los Pollos Hermanos', 'Spaghetti Factory']
transportation = ['car', 'plane', 'boat', 'bike', 'train']
entertainment = ['concert', 'movie', 'comedy show', 'bar', 'museum']
destinations = ['Detroit', 'Los Angeles', 'Honolulu', 'New York', 'Seattle']

#Messages to user
print('Hello! Welcome to the Day Trip Generator!')
print('')

def confirmation(notlists,question): 
    confirm = 'N'
    while confirm == 'N':
        random_selection = random.choice(notlists)
        confirm = input(question + random_selection + '? (Y/N?) ')
        if confirm == 'N':
            notlists.remove(random_selection)
            if len(notlists) == 0:
                confirm = ''
                print('You rejected all options.')
        elif confirm == 'Y':
            print('Great choice!')
            print('')
    return random_selection
    
# Determine initial trip choices

user_destination = confirmation(destinations,'Would you like to go to ')

user_restaurant = confirmation(restaurants, 'Would you like to go to ')

user_transport = confirmation(transportation, 'Would you like to get there by ')

user_entertainment = confirmation(entertainment, 'While you\'re there do you want to go to a ')

# Make final confirmations to your trip and print results.
check_itinerary = True
 
while check_itinerary:
    full_trip = input('Are you happy with your entire trip? (Y/N) ')
    if full_trip == 'Y':
        check_itinerary = False
        print('Enjoy your trip to ' + user_destination + '. You\'ll arrive by ' + user_transport + ', followed by dinner at ' + user_restaurant + '. Finally, you\'ll get to finish the night at a ' + user_entertainment + '.')
    elif full_trip == 'N':
        answer = input('Do you want to change your anything about your trip? (Y/N?) ' )
        if answer == 'Y':
            amend_choice = input('Would you like to change your destinaion? (Y/N) ')
            if amend_choice == 'Y':
                user_destination = confirmation(destinations, 'Would you like to go to ')
            restaurant_change = input('Do you want to change your restaurant choice? (Y/N)? ')
            if restaurant_change == 'Y':
                user_restaurant = confirmation(restaurants, 'Would you like to go to ')
            transport_change = input('Do you want to change your transportation choice? (Y/N)? ')    
            if transport_change == 'Y':
                user_transport = confirmation(transportation, 'Would you like to get there by ')
            entertainment_change = input('Do you want to change your entertainment choice? (Y/N)? ')    
            if transport_change == 'Y':
                user_entertainment = confirmation(entertainment, 'While you\'re there do you want to go to a ')



