# Attendance Marker for ITCLMS

## Intro
This is a script for automatically marking attendance on a learning management system of the University of Tokyo called ITCLMS.
https://itc-lms.ecc.u-tokyo.ac.jp/login

At the University of Tokyo, students are usually required to mark their attendance using the passocode that the professor gives during class. This scirpt automatically searches for your current class and sends an attendance passcode to the system.


## Setup
Change USER_NAME and PASSWORD in .env file to your username and password for ITCLMS.

Also, You need to install Selenium and python-dotenv if you do not have them.

## How to use
1. Run `python main.py`
2. Enter the passcode for the class.
```
Enter a passcode for attendance:
passcodefortheclass
```
3. The script will opens up Chrome, guide you to the class page, and send the passcode for you.
