# Railway-Tickets Booking System_

**Overview of the Project**

This Railway Tickect Booking System is a program written in python language. In this program the user provides personal and journey details such as name, age, starting and destination stations, train number and train name. The system will display available coach types and their fares, ask the user to select a coach and then print the formed ticket and total fare to be paid.

This project demonstrates fundamental programming concepts such as: 

*# Dictionaries*

*# Input/Output operations*

*# Conditional statements*

*# Basic validation*


**FEATURES**

* Collects Passenger details like Name, Age,
* Accepts travel information From, To, Train Number, Train Name.
* Displays available coachs their types and their respective fares.
* Calculate total fare based on selected coach.
* Validates coach selection,
* Generates a structured ticket-summary.


**Technology Used**
  
Component -   Details

Language   -  Python 3.x

Interface  -  Terminal

Logic     -   Dictionary-based fare mapping, input validation.


**Steps to install & run the project**

*1. Install Python* -
 
   Make sure Python 3 is installed on your system.

   If not then install, download it from the official website.

*2. Download the Project File*

Save the file for e.g. : railway_ticket.py

*3. Run the Program*

Open the Terminal and Run the following Code

The program will start and ask you for the Details.


**Instructions for Testing**

Follow the following steps to test the program:

1. Run the script

The program displays the heading "Railway Ticket Booking System".

2. Enter valid user inputs, For example:

Passenger name: PALAK GUPTA

Age: 19

From station: Bhopal

To station: Jhansi

Train number: 12712

Train name: Dakshin Express 

3. View available coaches

The program displays on terminal window:

1st AC

2nd AC

3rd AC


4. Select a valid coach

Enter exactly one from the provided list(case-sensitive).

for example: 3rd AC

(AC should be in capital as mentioned in the list)

5. Check whether ticket is generated

If you filled the valid coach, the trailling options will appear which will ask the user to enter:

Passenger details

Journey details

Coach selected

Fare

"Booking Successful!!" message

6. Test invalid input

Enter something like ac or Premium.

The program will print:

#Oops Sorry#

Invalid coach selected, Please try again.

