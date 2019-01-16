# capital quiz alternative using random library
import random
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
        state=StateRandomizer(states)
        print("What is the capital of", state, end="")
        user_capital=input(": ").lower()
        
        # check if it is correct. remember: dict[key]=value
        if states[state].lower()==user_capital:
            print("Correct!")
            count+=1
        else:
            print("Wrong! The correct answer is", states[state].capitalize())
        print("You have", count, "correct answer so far.")
        print("------------------------------------------")      
    
def StateRandomizer(a):
    # use random.choice. It returns only keys remember.
    # list function on dictionary returns a list of ONLY KEYs. only state names will
    # be acquired.
    state=random.choice(list(a))        # it gets a random choice among state names list.
    return state  

# call the main function
main()