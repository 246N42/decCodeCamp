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
        confirm = input(question + random_selection + '? (Y/N?)')
        if confirm == 'N':
            notlists.remove(random_selection)
            if len(notlists) == 0:
                confirm = ''
                print('You rejected all options.')
        elif confirm == 'Y':
            print('Great choice! Next question.')

confirmation(destinations,'Would you like to go to ')

confirmation(restaurants, 'Would you like to go to ')

confirmation(transportation, 'Would you like to get there by ')

confirmation (entertainment, 'While you\'re there do you want to go to a ')