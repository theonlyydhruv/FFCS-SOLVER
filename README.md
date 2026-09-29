FFCSolver
FFCSolver is a Python command-line program for generating an FFCS timetable based on course offerings and student preferences.
The idea is simple: select the courses you need, enter your preferences, and let the program check the available offerings and create a suitable timetable.
Features
Select required courses from the available offerings
Prevent duplicate course selection
Choose morning, evening, or no timing preference
Set a lunch-gap preference
Select a teacher for an individual subject
Check timetable clashes
Consider AB01 and AB02 venue movement
Generate a timetable from the available offerings
Show the result as a timetable grid
Show a detailed timetable with slot, day, time, teacher, and venue
Project Structure
```text
FFCSolver/
│── offerings.txt
│
├── data_manager.py
├── main.py
├── prefrences.py
├── scheduler.py
├── slot_data.py
└── README.md
```
What each file does
`main.py`
This is the starting point of the program. It loads the course data, takes the user's input, calls the scheduler, and displays the generated timetable.
`data_manager.py`
Reads `CONTENT/offerings.txt` and stores the course offerings. It also groups the offerings using the course code.
`prefrences.py`
Handles the user's general preferences, course selection, and teacher selection.
`scheduler.py`
Contains the main timetable logic. It checks conflicts and applies the selected preferences while generating possible timetables.
`slot_data.py`
Stores the day, start time, and end time for each slot.
`CONTENT/offerings.txt`
Contains the available course offerings and their faculty, slots, component type, and venue.
Requirements
Python 3.x
Command Prompt or PowerShell
No external Python packages are required
Setup
1. Clone or download the repository
Clone the public GitHub repository or download the project.
2. Check Python
Open Command Prompt or PowerShell:
```text
python --version
```
If that does not work:
```text
py --version
```
Python 3.x should be installed.
3. Open the project folder
For example:
```text
cd Desktop\FFCSolver
```
Make sure you are in the folder that contains `main.py`.
4. Check the course data
Make sure this file exists:
```text
offerings.txt
```
The program reads the course offerings from this file.
5. Run the program
```text
python main.py
```
or:
```text
py main.py
```
No GUI setup is required.
Using the Program
First, enter the course codes you want.
Example:
```text
Enter course code (or type done): MAT1003
Enter course code (or type done): CHY1006
Enter course code (or type done): CSE1021
Enter course code (or type done): ENG1004
Enter course code (or type done): done
```
The same course cannot be selected twice.
Timing
Enter one of:
```text
morning
evening
any
```
Lunch
Enter:
```text
yes
```
or:
```text
no
```
AB01/AB02
Enter:
```text
yes
```
or:
```text
no
```
Teacher preference
For each selected course, the program asks whether a teacher preference is required.
If `yes` is selected, the available teachers for that course are shown and one can be selected.
If `no` is selected, the scheduler does not force a particular teacher for that course.
How the Scheduler Works
The program first loads the available course offerings.
Each offering contains:
```text
course_code|course_name|faculty|slot_group|component|venue
```
Example:
```text
MAT1003|Calculus|MANISHA JAIN|A11+A12+A13+A14+D11+D12|LT|AB-519
```
The scheduler uses the slot information to find the actual day and time of each class.
It then checks whether selected offerings overlap on the same day. Timetables are also checked against the selected preferences.
Output
The program gives two views of the generated timetable.
Timetable Grid
The first view is arranged by day and time, showing the course code, teacher, and venue.
Detailed Timetable
The second view shows:
Course code
Course name
Faculty
Slot
Day
Start time
End time
Venue
Example
A course offering such as:
```text
MAT1003|Calculus|MANISHA JAIN|A11+A12+A13+A14+D11+D12|LT|AB-519
```
contains:
Course: MAT1003
Name: Calculus
Faculty: MANISHA JAIN
Slots: A11, A12, A13, A14, D11, D12
Component: LT
Venue: AB-519
The slot data is then used to determine when each slot takes place.
Notes
Run the project from the project root.
Keep `offerings.txt` 
Keep the Python files in the project structure shown above.
No external Python packages are required.
The generated timetable depends on the course offering data available in `offerings.txt`