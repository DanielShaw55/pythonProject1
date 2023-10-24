from datetime import datetime

# Define a dictionary with college mascots, their year of birth, fun facts, and special events
college_mascots = {
    "University of Alabama": {"Mascot": "Big Al", "Year of Birth": 1979,
                              "Fun Fact": "Big Al is known for his big elephant head and friendly demeanor.",
                              "Special Event": "Big Al makes appearances at University of Alabama football games."},
    "Clemson University": {"Mascot": "The Tiger", "Year of Birth": 1954,
                           "Fun Fact": "The Tiger is Clemson's costumed mascot that represents the university.",
                           "Special Event": "The Tiger is a beloved figure at Clemson sporting events."},
    "University of Texas": {"Mascot": "Bevo the Longhorn", "Year of Birth": 1916,
                            "Fun Fact": "Bevo is a longhorn steer and symbol of the University of Texas.",
                            "Special Event": "Bevo attends UT football games."},
    "University of Michigan": {"Mascot": "Wolverine", "Year of Birth": 1927,
                               "Fun Fact": "Wolverine represents the university's fighting spirit.",
                               "Special Event": "Wolverine cheers for the Michigan Wolverines."},
    "University of Florida": {"Mascot": "Albert and Alberta Gator", "Year of Birth": 1970,
                              "Fun Fact": "Albert and Alberta are alligators and represent UF's mascot.",
                              "Special Event": "They appear at UF sporting events."},
    "Ohio State University": {"Mascot": "Brutus Buckeye", "Year of Birth": 1965,
                              "Fun Fact": "Brutus is a buckeye nut and a beloved OSU mascot.",
                              "Special Event": "He energizes the OSU crowd."},
    "University of Oregon": {"Mascot": "Puddles the Duck", "Year of Birth": 1947,
                             "Fun Fact": "Puddles is the friendly duck mascot of UO.",
                             "Special Event": "Puddles shows up at UO games."},
    "Texas A&M University": {"Mascot": "Reveille the Collie", "Year of Birth": 1931,
                             "Fun Fact": "Reveille is a collie and the highest-ranking member of the Texas A&M Corps of Cadets.",
                             "Special Event": "She attends A&M events."},
    "University of Georgia": {"Mascot": "Uga the Bulldog", "Year of Birth": 1956,
                              "Fun Fact": "Uga is an English Bulldog and a UGA icon.",
                              "Special Event": "He's a fixture at UGA games."},
    "Stanford University": {"Mascot": "Stanford Tree", "Year of Birth": 1975,
                            "Fun Fact": "The Stanford Tree is a mascot representing Stanford University.",
                            "Special Event": "The Tree appears at Stanford events."},
    "OSU": {"Mascot": "Brutus Buckeye", "Year of Birth": 1965,
            "Fun Fact": "Brutus is a buckeye nut and a beloved OSU mascot.",
            "Special Event": "He energizes the OSU crowd."},
    "UA": {"Mascot": "Big Al", "Year of Birth": 1979,
           "Fun Fact": "Big Al is known for his big elephant head and friendly demeanor.",
           "Special Event": "Big Al makes appearances at University of Alabama football games."},
    "Clemson": {"Mascot": "The Tiger", "Year of Birth": 1954,
                "Fun Fact": "The Tiger is Clemson's costumed mascot that represents the university.",
                "Special Event": "The Tiger is a beloved figure at Clemson sporting events."},
    "UT": {"Mascot": "Bevo the Longhorn", "Year of Birth": 1916,
           "Fun Fact": "Bevo is a longhorn steer and symbol of the University of Texas.",
           "Special Event": "Bevo attends UT football games."},
    "UM": {"Mascot": "Wolverine", "Year of Birth": 1927,
           "Fun Fact": "Wolverine represents the university's fighting spirit.",
           "Special Event": "Wolverine cheers for the Michigan Wolverines."},
    "UF": {"Mascot": "Albert and Alberta Gator", "Year of Birth": 1970,
           "Fun Fact": "Albert and Alberta are alligators and represent UF's mascot.",
           "Special Event": "They appear at UF sporting events."},
    "UO": {"Mascot": "Puddles the Duck", "Year of Birth": 1947,
           "Fun Fact": "Puddles is the friendly duck mascot of UO.", "Special Event": "Puddles shows up at UO games."},
    "TAMU": {"Mascot": "Reveille the Collie", "Year of Birth": 1931,
             "Fun Fact": "Reveille is a collie and the highest-ranking member of the Texas A&M Corps of Cadets.",
             "Special Event": "She attends A&M events."},
    "UGA": {"Mascot": "Uga the Bulldog", "Year of Birth": 1956, "Fun Fact": "Uga is an English Bulldog and a UGA icon.",
            "Special Event": "He's a fixture at UGA games."},
    "SU": {"Mascot": "Stanford Tree", "Year of Birth": 1975,
           "Fun Fact": "The Stanford Tree is a mascot representing Stanford University.",
           "Special Event": "The Tree appears at Stanford events."},
}


# Function to calculate the age of a mascot
def calculate_mascot_age(year_of_birth):
    current_year = datetime.now().year
    return current_year - year_of_birth


# Function to get the mascot for a given college, ignoring case and allowing partial matches
def get_mascot_info(college_name):
    college_name = college_name.lower()
    for name, info in college_mascots.items():
        if college_name in name.lower() or college_name in info["Mascot"].lower():
            age = calculate_mascot_age(info["Year of Birth"])
            return info["Mascot"], age, info.get("Fun Fact"), info.get("Special Event")
    return None, None, None, None


# Function to interact with the user about the mascot
def mascot_info_dialogue(college_name):
    mascot, age, fun_fact, special_event = get_mascot_info(college_name)
    if mascot and age is not None:
        print(f"The mascot of {college_name} is {mascot}, and it is {age} years old.")
        while True:
            print("Menu:")
            print("1. Fun Fact")
            print("2. Special Event")
            print("3. Exit")
            user_question = input("Enter the number of your choice: ")
            if user_question == "1":
                if fun_fact:
                    print(f"Fun Fact: {fun_fact}")
                else:
                    print("No fun fact available.")
            elif user_question == "2":
                if special_event:
                    print(f"Special Event: {special_event}")
                else:
                    print("No special event information available.")
            elif user_question == "3":
                return
            else:
                print("Please select a valid option (1, 2, or 3).")


while True:
    # Get user input for a college name or abbreviation (or 'done' to exit)
    user_input = input("Enter a college name or abbreviation (or 'done' to exit): ")

    if user_input.lower() == 'done':
        break  # Exit the loop if the user is done

    mascot_info_dialogue(user_input)
