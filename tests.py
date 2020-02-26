import pytest
from lib.AppointmentSystem import *
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from lib.User import *
from routes import *
from lib.Appointments import *
'''
A comprehensive set of test-cases must be submitted for the acceptance criteria defined above. Please adhere to the following guide-lines in implementing the test-cases.
Test-cases must be written for three core user-stories: (1) book an appointment (2) view a patient history (3) manage a patient history. The test-cases must be implemented with PyTest.
Each user-story must have multiple test-cases defined. For example, if you are writing test-cases for ?book an appointment with a health-care provider?, you will be testing for (i) making a successful appointment and getting a confirmation of the appointment (ii)l booking an appointment in the past (ii) book multiple appointments in the same day/time-slot (ii) test that a provider cannot make an appointment with themselves etc.
(Note: these test-cases must match the acceptance criteria that you have defined for the chosen user-story.)
The test-cases must be in a file ?tests.py?. They will be run by your tutor. Hence, make sure that the test-cases execute successfully.
'''
# Note: Many implementations were made in the html and routes and thus can be tested via the web

def test_book():
    print("Test 1: making a successful appointment and getting a confirmation of the appointment")
    Patient = get_user_name('Tom')
    Provider = get_user_name('Gary')
    appointment1 = Appointment('30-10-2018', '09:00AM', '09:30AM', 'Sydney Children Hospital', 'Gary', 'Tom', ' ')
    Patient.add_appointments(appointment1)
    Provider.add_appointments(appointment1)
    assert(Provider.appointments == ([appointment1]))
    appointment1 = Appointment('30-10-2018', '9:00AM', '5:00PM', 'Sydney Children Hospital', 'Gary','Jack',' ')

def test_past_booking():
    print("Test 2: booking an appointment in the past")
    date=str(datetime.today().day)+"-10-2018"
    date_datetime = datetime.strptime(date,"%d-%m-%Y")
    Provider = get_user_name('Toby')
    Centre = get_centre('Sydney Children Hospital')
    print(AppointmentSystem.find_valid_times('09:00AM', '09:30AM', date, Provider, Centre, date_datetime))
    assert (AppointmentSystem.find_valid_times('09:00AM', '09:30AM', date, Provider, Centre, date_datetime) =="There are no available times left for this date. Please choose another.")

def test_no_booking():
    print("Test 3: all time slots booked for the day")
    Patient = get_user_name('Tom')
    Provider = get_user_name('Toby')
    Centre = get_centre('Sydney Children Hospital')
    date_datetime = datetime.strptime('30-10-2018',"%d-%m-%Y")
    appointment1 = Appointment('30-10-2018', '09:00AM', '09:30AM', 'Sydney Children Hospital', 'Toby', 'Tom', ' ')
    appointment2 = Appointment('30-10-2018', '09:30AM', '10:00AM', 'Sydney Children Hospital', 'Toby', 'Tom', ' ')
    appointment3 = Appointment('30-10-2018', '10:00AM', '10:30AM', 'Sydney Children Hospital', 'Toby', 'Tom', ' ')
    appointment4 = Appointment('30-10-2018', '10:30AM', '11:00AM', 'Sydney Children Hospital', 'Toby', 'Tom', ' ')
    Provider.add_appointments(appointment1)
    Provider.add_appointments(appointment2)
    Provider.add_appointments(appointment3)
    Provider.add_appointments(appointment4)
    assert (AppointmentSystem.find_valid_times('09:30AM', '10:00AM', '30-10-2018', Provider, 'Sydney Children Hospital', date_datetime) =="There are no available times left for this date. Please choose another.")
    
def test_booking_same_day():
    print("Test 4: booked multiple appointments in the same day/time-slot")
    Patient = get_user_name('Tom')
    Provider = get_user_name('Gary')
    Centre = get_centre('Sydney Children Hospital')
    date_datetime = datetime.strptime('30-10-2018',"%d-%m-%Y")
    appointment1 = Appointment('30-10-2018', '09:00AM', '09:30AM', 'Sydney Children Hospital', 'Gary', 'Tom', ' ')
    appointment2 = Appointment('30-10-2018', '09:30AM', '10:00AM', 'Sydney Children Hospital', 'Gary', 'Tom', ' ')
    appointment3 = Appointment('30-10-2018', '10:00AM', '10:30AM', 'Sydney Children Hospital', 'Gary', 'Tom', ' ')
    Provider.add_appointments(appointment1)
    Provider.add_appointments(appointment2)
    Provider.add_appointments(appointment3)
    assert (AppointmentSystem.find_valid_times('10:30AM', '11:00AM', '30-10-2018', Provider, 'Sydney Children Hospital', date_datetime) == {'10:30AM': '11:00AM'})
    
def test_repeated_booking():
    print("Test 5: booking an appointment on an already taken time-slot")
    Patient = get_user_name('Tom')
    Provider = get_user_name('Gary')
    Centre = get_centre('Sydney Children Hospital')
    date_datetime = datetime.strptime('31-10-2018',"%d-%m-%Y")
    appointment1 = Appointment('31-10-2018', '10:30AM', '11:00AM', 'Sydney Children Hospital', 'Gary', 'Tom', ' ')
    Provider.add_appointments(appointment1)
    assert (AppointmentSystem.find_valid_times('10:30AM', '11:00AM', '31-10-2018', Provider, 'Sydney Children Hospital', date_datetime) == "There are no available times left for this date. Please choose another.")
    
def test_patient_history():
    print("Test 6: add notes and view a patient's history")
    Patient = get_user_name('Jack')
    Provider = get_user_name('Gary')
    Centre = get_centre('Sydney Children Hospital')
    appointment1 = Appointment('31-10-2018', '09:00AM', '09:30AM', 'Sydney Children Hospital', 'Gary', 'Jack', ' ')
    appointment2 = Appointment('31-10-2018', '09:30AM', '10:00AM', 'Sydney Children Hospital', 'Gary', 'Jack', ' ')
    appointment3 = Appointment('31-10-2018', '10:00AM', '10:30AM', 'Sydney Children Hospital', 'Gary', 'Jack', ' ')
    Patient.add_appointments(appointment1)
    Patient.add_appointments(appointment2)
    Patient.add_appointments(appointment3)
    appointment1 = Patient.appointments[0]
    notes = appointment1.notes
    notes = "Patient's scan showed a lesion of size 1cm, features suggestive of tumour, biopsy recommended. Patient advised to see GP immediately."
    medication = "Panadol"
    appointment1.add_notes(notes)
    appointment1.add_medications(medication)
    appointment2 = Patient.appointments[1]
    notes = appointment2.notes
    notes = "Patient is fine, no need for biopsy"
    medication = "Panadol"
    appointment2.add_notes(notes)
    appointment2.add_medications(medication)
    assert(Patient.appointments[0].notes == "Patient's scan showed a lesion of size 1cm, features suggestive of tumour, biopsy recommended. Patient advised to see GP immediately.")
    assert(Patient.appointments[1].notes == "Patient is fine, no need for biopsy")
    
def test_edit_notes():
    print("Test 7: edit notes")
    Patient = get_user_name('Jack')
    assert(Patient.appointments[0].notes == "Patient's scan showed a lesion of size 1cm, features suggestive of tumour, biopsy recommended. Patient advised to see GP immediately.")
    appointment1 = Patient.appointments[0]
    notes = appointment1.notes
    notes = "This note has been edited"
    appointment1.add_notes(notes)
    assert(Patient.appointments[0].notes == "This note has been edited")
    
def test_edit_medication():
    print("Test 8: edit medication")
    Patient = get_user_name('Jack')
    assert(Patient.appointments[0].medications == "Panadol")
    appointment1 = Patient.appointments[0]
    medication = appointment1.medications
    medication = "Tylenol"
    appointment1.add_medications(medication)
    assert(Patient.appointments[0].medications == "Tylenol")
    
    
def test_sort_appointments_chronologically():
    print("Test 9: make sure history is in chronological order")
    Patient = get_user_name('Isaac')
    Provider = get_user_name('Ian')
    Centre = get_centre('Sydney Children Hospital')
    appointment1 = Appointment('1-11-2018', '09:00AM', '09:30AM', 'Sydney Children Hospital', 'Ian', 'Isaac', ' ')
    appointment2 = Appointment('27-10-2018', '09:00AM', '09:30AM', 'Sydney Children Hospital', 'Ian', 'Isaac', ' ')
    appointment3 = Appointment('28-10-2018', '09:00AM', '09:30AM', 'Sydney Children Hospital', 'Ian', 'Isaac', ' ')
    Provider.add_appointments(appointment1)
    Provider.add_appointments(appointment2)
    Provider.add_appointments(appointment3)
    appointment1 = Provider.appointments[0]
    notes = appointment1.notes
    notes = "Notes 1"
    appointment1.add_notes(notes)
    appointment2 = Provider.appointments[1]
    notes = appointment2.notes
    notes = "Notes 2"
    appointment2.add_notes(notes)
    appointment3 = Provider.appointments[2]
    notes = appointment3.notes
    notes = "Notes 3"
    appointment3.add_notes(notes)
    assert(Provider.appointments[0].notes == "Notes 1")
    assert(Provider.appointments[1].notes == "Notes 2")
    assert(Provider.appointments[2].notes == "Notes 3")
    Provider.sortAppointments()
    assert(Provider.appointments[0].notes == "Notes 2")
    assert(Provider.appointments[1].notes == "Notes 3")
    assert(Provider.appointments[2].notes == "Notes 1")

