# This program demonstrates polymorphism.

import animals

def main():
    # create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    # display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

# the show_mammal_info function accepts an object
# as an argument, and calls its show_species
# and make_sound methods.
def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Call the main function.
main()