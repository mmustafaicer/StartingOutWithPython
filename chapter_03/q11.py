# book club points

# ask user to enter the number of books that he or she bought

n_books=int(input("Enter the the number of books purchased: "))

# create decision structure to award points
print()
if n_books==0:
    points=0
    print("You have been", points, "point awarded with your purchase of", n_books, "books.")
elif n_books>=2 and n_books<4:
    points=5
    print("You have been", points, "points awarded with your purchase of", n_books, "books.")
elif n_books>=4 and n_books<6:
    points=15
    print("You have been", points, "points awarded with your purchase of", n_books, "books.")
elif n_books>=6 and n_books<8:
    points=30
    print("You have been", points, "points awarded with your purchase of", n_books, "books.")
elif n_books>=8:
    points=60
    print("You have been", points, "points awarded with your purchase of", n_books, "books.")
else:
    print("ERROR: You entered an invalid entry!")

    