# capital quiz
# there is an alternative version using random library

def main():
    
    # create a dictionary.
    states=capital_dic={'Alabama': 'Montgomery', 'Alaska': 'Juneau','Arizona':'Phoenix',
    'Arkansas':'Little Rock', 'California': 'Sacramento', 'Colorado':'Denver',
    'Connecticut':'Hartford', 'Delaware':'Dover','Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinios': 'Springfield', 'Indiana': 'Indianapolis','Iowa': 'Des Monies',
    'Kansas': 'Topeka','Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Neveda': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakoda': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    
    # set an accumulator
    count=0
    for i in range(len(states)):
        state, capital=StateRandomizer(states)
        print("What is the capital of", state, end="")
        user_capital=input(": ").lower()
        
        # check if it is correct
        if capital==user_capital:
            print("Correct!")
            count+=1
        else:
            print("Wrong! The correct answer is", capital.capitalize())
        print("You have", count, "correct answer so far.")
        print("------------------------------------------")      
    
def StateRandomizer(a):
    # use popitem method to choose a random key-value pair.
    state, capital=a.popitem()
    return state, capital.lower()   

# call the main function
main()