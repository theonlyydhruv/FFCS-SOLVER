FFCSolver

FFCSolver is a command-line based timetable planner for FFCS. It takes the available course offerings and lets the user select courses and preferences before generating a suitable timetable.

The project is made for the VITyarthi project submission and is based on the Python course domain.

What the project does

The program can:

Load course and faculty information from an offerings file.

Let the user select the courses they need.

Prevent the same course from being selected twice.

Take a preferred timing: morning, evening, or any.

Ask whether a lunch gap is required.

Consider AB01/AB02 venue movement.

Allow a teacher preference for each selected subject.

Check timetable clashes.

Generate possible timetables from the available offerings.

Display the final timetable in a day-and-time grid.

Display a detailed version with slot, day, timing, teacher, and venue.

The course data contains the course code, course name, faculty, slot group, component, and venue. The program reads these fields from CONTENT/offerings.txt.

Project structure

FFCSolver/
│
├── offerings.txt
├── data_manager.py
├── main.py
├── prefrences.py
├── scheduler.py
├── slot_data.py
└── README.md

File details

main.py
This is the main file of the project. It connects all the other files, takes user input, generates the timetable, and displays the result.

data_manager.py
Reads the offerings file and converts each course offering into a dictionary. It also groups the offerings according to course code.

prefrences.py
Handles user preferences and course/teacher selection.

scheduler.py
Contains the timetable generation logic. It checks clashes, timing preferences, lunch preference, teacher preference, and AB01/AB02 movement.

slot_data.py
Contains the mapping between slot names and their day, start time, and end time.

offerings.txt
Contains the course offering data used by the program.

Requirements

Python 3.x

Command Prompt or PowerShell

No external Python packages are required.

Setup

1. Download or clone the repository

Clone the public GitHub repository or download the project files.

Make sure the project has the same folder structure shown above.

2. Check Python

Open Command Prompt or PowerShell and run:

python --version

If python does not work, try:

py --version

Python 3.x should be installed.

3. Open the project folder

Move into the FFCSolver folder:

cd path\\to\\FFCSolver

For example:

cd Desktop\\FFCSolver

4. Check the data file

Make sure this file exists:

offerings.txt

The program reads the course data from this file.

5. Run the project

Run:

python main.py

or:

py main.py

No GUI or additional setup is required.

How to use

When the program starts, it asks for the course codes.

Enter the required course code one at a time:

Enter course code (or type done): MAT1003
Enter course code (or type done): CHY1006
Enter course code (or type done): CSE1021
Enter course code (or type done): ENG1004
Enter course code (or type done): done

After selecting courses, the program asks for preferences.

Timing preference

Choose:

morning
evening
any

Lunch preference

Enter:

yes

or:

no

AB01/AB02 preference

Enter:

yes

or:

no

Teacher preference

For every selected subject, the program asks whether a teacher preference is required.

If yes is selected, the available teachers for that subject are displayed and the user can choose one.

If no is selected, the program does not force a particular teacher for that subject.

Timetable generation

The scheduler first considers the selected teacher preferences and then checks the other timetable preferences.

The slot information is used to determine the actual day and time of each class. For example, slots contain information such as Monday 08:30-10:00, Tuesday 10:05-11:35, and so on.

The scheduler also checks whether two selected offerings have overlapping classes on the same day.

Output

The program displays the generated timetable in a grid similar to a normal college timetable.

The grid contains:

Days

Class timings

Course codes

Faculty

Venue

A detailed timetable is also displayed with:

Course code

Course name

Faculty

Slot

Day

Start time

End time

Venue

Example course data

The offerings file uses the following format:

course_code|course_name|faculty|slot_group|component|venue

Example:

MAT1003|Calculus|MANISHA JAIN|A11+A12+A13+A14+D11+D12|LT|AB-519

This contains the course code, course name, faculty, available slot group, component type, and venue.

Important notes

Run the program from the project root directory.

Do not move offerings.txt out of the CONTENT folder.

Keep the Python files together as shown in the project structure.

The project is designed to run completely through the command line.

No external libraries are needed.