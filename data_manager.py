# read the offering file
def load_offerings():
    offerings = []

    with open("CONTENT/offerings.txt", "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue
            parts = line.split("|")
            course_code = parts[0]
            course_name = parts[1]
            faculty = parts[2]
            slot_group = parts[3]
            component = parts[4]
            venue = parts[5]
            offerings.append({
                "course_code": course_code,
                "course_name": course_name,
                "faculty": faculty,
                "slot_group": slot_group,
                "component": component,
                "venue": venue
            })
    return offerings

# group the course by course code 
def group_by_course(offerings):
    courses = {}
    for offering in offerings:
        code = offering["course_code"]
        if code not in courses:
            courses[code] = []
        courses[code].append(offering)

    return courses