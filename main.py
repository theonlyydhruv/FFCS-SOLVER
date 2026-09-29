from data_manager import load_offerings, group_by_course
from prefrences import get_preferences, select_courses, select_teachers
from scheduler import generate_timetables
from slot_data import slot_data

def get_class_for_slot(timetable, slot_name):
    for offering in timetable:
        slots = offering["slot_group"].split("+")
        for slot in slots:
            if slot == slot_name:
                return offering
    return None

def show_timetable_grid(timetable):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]
    times = [
        "08:30-10:00",
        "10:05-11:35",
        "11:40-13:10",
        "Lunch",
        "13:15-14:45",
        "14:50-16:20",
        "16:25-17:55",
        "18:00-19:30"
    ]
    slots = [
        ["A11", "B11", "C11", "Lunch", "A21", "A14", "B21", "C21"],
        ["D11", "E11", "F11", "Lunch", "D21", "E14", "E21", "F21"],
        ["A12", "B12", "C12", "Lunch", "A22", "B14", "B22", "A24"],
        ["D12", "E12", "F12", "Lunch", "D22", "F14", "E22", "F22"],
        ["A13", "B13", "C13", "Lunch", "A23", "C14", "B23", "B24"],
        ["D13", "E13", "F13", "Lunch", "D23", "D14", "D24", "E23"]
    ]
    print("\n")
    print("=" * 150)
    print("                         GENERATED FFCS TIMETABLE")
    print("=" * 150)
    print("{:<8}".format("DAY"), end="")
    for time in times:
        print("{:<18}".format(time), end="")
    print()
    print("-" * 150)
    for day_index in range(len(days)):
        print("{:<8}".format(days[day_index]), end="")
        for time_index in range(len(times)):
            current_slot = slots[day_index][time_index]
            if current_slot == "Lunch":
                print("{:<18}".format("LUNCH"), end="")
                continue
            offering = get_class_for_slot(timetable, current_slot)
            if offering is None:
                print("{:<18}".format("-"), end="")
            else:
                course = offering["course_code"]
                print("{:<18}".format(course), end="")
        print()
        print("{:<8}".format(""), end="")
        for time_index in range(len(times)):
            current_slot = slots[day_index][time_index]
            if current_slot == "Lunch":
                print("{:<18}".format(""), end="")
                continue
            offering = get_class_for_slot(timetable, current_slot)
            if offering is None:
                print("{:<18}".format(""), end="")
            else:
                teacher = offering["faculty"]
                print("{:<18}".format(teacher[:17]), end="")
        print()
        print("{:<8}".format(""), end="")
        for time_index in range(len(times)):
            current_slot = slots[day_index][time_index]
            if current_slot == "Lunch":
                print("{:<18}".format(""), end="")
                continue
            offering = get_class_for_slot(timetable, current_slot)
            if offering is None:
                print("{:<18}".format(""), end="")
            else:
                venue = offering["venue"]
                print("{:<18}".format(venue), end="")
        print()
        print("-" * 150)


def show_detailed_timetable(timetable):
    print("\n")
    print("=" * 100)
    print("                         DETAILED TIMETABLE")
    print("=" * 100)

    for offering in timetable:
        print()
        print(offering["course_code"], "|", offering["course_name"], "|", offering["faculty"], "|", offering["venue"])
        slots = offering["slot_group"].split("+")
        for slot in slots:
            if slot in slot_data:
                day = slot_data[slot][0]
                start = slot_data[slot][1]
                end = slot_data[slot][2]
                print("   ", slot, "|", day, "|", start + " - " + end, "|", offering["venue"])


def main():
    data = load_offerings()
    courses = group_by_course(data)
    print("===== FFCS TIMETABLE SOLVER =====\n")
    selected_courses = select_courses(courses)
    if not selected_courses:
        print("No courses selected.")
        return
    preferences = get_preferences()
    teacher_preferences = select_teachers(courses, selected_courses)
    selected_offerings = {}
    for code in selected_courses:
        selected_offerings[code] = courses[code]
    timetables = generate_timetables(selected_offerings, preferences, teacher_preferences)
    if not timetables:
        print("\nNo timetable could be created with the current preferences.")
        print("Try changing the timing, lunch gap, AB01/AB02 preference,")
        print("or one of the teacher preferences.")
        return
    print("\nTimetable found!")
    timetable = timetables[0]
    show_timetable_grid(timetable)
    show_detailed_timetable(timetable)
if __name__ == "__main__":
    main()