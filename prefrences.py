def get_preferences():
    preferences = {}

    time_preference = input( "Preferred timing (morning/evening/any): ").lower()
    lunch_gap = input( "Lunch gap required? (yes/no): ").lower() 
    avoid_alternate = input("Avoid alternate AB01/AB02 classes? (yes/no): ").lower()
    preferences["time"] = time_preference
    preferences["lunch_gap"] = lunch_gap
    preferences["avoid_alternate"] = avoid_alternate
    return preferences 

def select_courses(courses):
    selected_courses = []
    while True:
        code = input("Enter course code (or type done): " ).upper()
        if code == "DONE":
            break
        if code in courses:
            if code not in selected_courses:
                selected_courses.append(code)
            else:
                print("Course already selected")
        else:
            print("Course code not found")
    return selected_courses


def select_teachers(courses, selected_courses):
    teacher_preferences = {}
    for code in selected_courses:
        print("\nCourse:", code)
        choice = input(
            "Do you want a teacher preference for this subject? (yes/no): "
        ).lower()
        if choice == "no":
            teacher_preferences[code] = None
            continue
        print("\nTeachers available:")
        offerings = courses[code]
        for i in range(len(offerings)):
            print(i + 1, ".", offerings[i]["faculty"])
        print("0. No preference")
        teacher_choice = int(input("Choose teacher: "))
        if teacher_choice == 0:
            teacher_preferences[code] = None
        else:
            teacher_preferences[code] = offerings[teacher_choice - 1]["faculty"]
    return teacher_preferences