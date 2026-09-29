from slot_data import slot_data


def get_offering_slots(offering):
    slots = offering["slot_group"].split("+")
    result = []
    for slot in slots:
        if slot in slot_data:
            day = slot_data[slot][0]
            start = slot_data[slot][1]
            end = slot_data[slot][2]
            result.append({
                "slot": slot,
                "day": day,
                "start": start,
                "end": end
            })

    return result


def has_conflict(offering1, offering2):
    slots1 = get_offering_slots(offering1)
    slots2 = get_offering_slots(offering2)
    for first in slots1:
        for second in slots2:
            if first["day"] == second["day"]:
                if first["start"] < second["end"]:
                    if second["start"] < first["end"]:
                        return True

    return False


def fits_time_preference(offering, time_preference):
    if time_preference == "any":
        return True
    slots = get_offering_slots(offering)
    if len(slots) == 0:
        return False
    if time_preference == "morning":
        for slot in slots:
            if slot["start"] >= "13:15":
                return False
        return True
    if time_preference == "evening":
        for slot in slots:
            if slot["start"] < "13:15":
                return False
        return True
    return True


def has_lunch_gap(timetable):
    first_lunch_used = False
    second_lunch_used = False
    for offering in timetable:
        slots = get_offering_slots(offering)
        for slot in slots:
            if slot["start"] == "11:40":
                first_lunch_used = True
            if slot["start"] == "13:15":
                second_lunch_used = True

    if first_lunch_used == False:
        return True
    if second_lunch_used == False:
        return True
    return False


def fits_teacher_preference(offering, teacher_preferences):
    code = offering["course_code"]
    if code not in teacher_preferences:
        return True
    preferred_teacher = teacher_preferences[code]
    if preferred_teacher is None:
        return True
    if offering["faculty"] == preferred_teacher:
        return True
    return False


def get_block(venue):
    if venue.startswith("AB-"):
        return "AB01"
    if venue.startswith("AB2-"):
        return "AB02"
    return "OTHER"

def fits_ab_preference(timetable):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]
    for day in days:
        classes = []
        for offering in timetable:
            slots = get_offering_slots(offering)
            for slot in slots:
                if slot["day"] == day:
                    block = get_block(offering["venue"])
                    if block != "OTHER":
                        classes.append({
                            "start": slot["start"],
                            "block": block
                        })
        for i in range(len(classes)):
            for j in range(i + 1, len(classes)):
                if classes[i]["start"] > classes[j]["start"]:
                    temp = classes[i]
                    classes[i] = classes[j]
                    classes[j] = temp
        switches = 0
        for i in range(1, len(classes)):
            if classes[i]["block"] != classes[i - 1]["block"]:
                switches = switches + 1
        if switches > 2:
            return False

    return True


def create_combinations(possible_offerings):
    combinations = [[]]
    for offerings in possible_offerings:
        new_combinations = []
        for combination in combinations:
            for offering in offerings:
                new_combination = combination.copy()
                new_combination.append(offering)
                new_combinations.append(new_combination)
        combinations = new_combinations

    return combinations


def check_conflicts(timetable):
    for i in range(len(timetable)):
        for j in range(i + 1, len(timetable)):
            if has_conflict(timetable[i], timetable[j]):
                return True
    return False

def generate_timetables(course_offerings, preferences, teacher_preferences):
    course_codes = list(course_offerings.keys())
    possible_offerings = []
    for code in course_codes:
        valid = []
        for offering in course_offerings[code]:
            if fits_teacher_preference(
                offering,
                teacher_preferences
            ):

                valid.append(offering)
        if len(valid) == 0:
            return []
        possible_offerings.append(valid)
    combinations = create_combinations(possible_offerings)
    teacher_timetables = []
    for combination in combinations:
        if check_conflicts(combination):
            continue
        teacher_timetables.append(combination)
    if len(teacher_timetables) == 0:
        return []
    preferred_timetables = []

    for timetable in teacher_timetables:
        if preferences["time"] != "any":
            fits_time = True
            for offering in timetable:
                if fits_time_preference(
                    offering,
                    preferences["time"]
                ) == False:
                    fits_time = False
                    break
            if fits_time == False:
                continue
        if preferences["lunch_gap"] == "yes":
            if has_lunch_gap(timetable) == False:
                continue
        if preferences["avoid_alternate"] == "yes":
            if fits_ab_preference(timetable) == False:
                continue
        preferred_timetables.append(timetable)
    if len(preferred_timetables) > 0:
        return preferred_timetables
    return teacher_timetables