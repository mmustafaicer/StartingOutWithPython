# course information

def main():
    
    # create dictionaries
    room_number={"CS101": 3004, "CS102": 4501, "CS103": 6755,
                  "NT110": 1244, "CM241": 1411}
    instructors={"CS101": "Haynes", "CS102": "Alvarado", 
                 "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
    times={"CS101": "8:00 a.m.", "CS102": "9:00 a.m.", 
                 "CS103": "10:00 a.m.", "NT110": "11:00 a.m.", "CM241": "1:00 p.m."}
    
    # get the course number
    course_number=input("Enter a course number: ")
    
    # display results
    display(room_number, instructors, times, course_number)
    
def display(r, i, t, course):
    print()
    print("Room Number:", r[course])
    print("Instructor:", i[course])
    print("Meeting Time: :", t[course])
    
# call the main function
main()