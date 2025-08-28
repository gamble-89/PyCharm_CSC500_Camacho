# This is a program demonstrating the use of dictionaries in Python
# This program will prompt the user for a course # and output the instructor, room #, and meeting time

# Create three dictionaries based on the provided key-value pairs (Room Number, Instructors, and Meeting Time)
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Start a loop to keep prompting the user until a valid course number or 'q' is entered to quit
# Keep the loop active until 'q' is entered to allow for multiple queries
while True:
    # Prompt the user to input a course number, remove whitespace, and convert to lowercase for error handling
    course_number_input = input("Enter a course number you would like to search (e.g., CSC101) or 'q' to quit: ").strip().lower()

    # Check if the user wants to quit searching
    if course_number_input == "q":
        print("Good luck with your studies!")
        break

    # Create a reverse mapping to get the original capitalized key (continued error handling for lowercase inputs)
    capitalized_course = next((k for k in course_rooms.keys() if k.lower() == course_number_input), None)

    # Display the corresponding room number, instructor, and meeting time to the user
    if capitalized_course:
        print(f"Course Name: {capitalized_course}")
        print(f"Room #: {course_rooms[capitalized_course]}")
        print(f"Instructor Last Name: {course_instructors[capitalized_course]}")
        print(f"Meeting Time: {course_times[capitalized_course]}")
    else:
        print("Course not found. Please try again or enter 'q' to quit.")
