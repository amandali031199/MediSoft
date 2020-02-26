from datetime import datetime,timedelta
from lib.Appointments import *
from lib.User import *

import pickle

class AppointmentSystem():
    def __init__(self):
        """
        Pass in a new appointment
        """
        self._appointmentlist = []
        self._alltimeslots = {}
    
    def addAppointment(self, appointment):
        self._appointmentlist.append(appointment)
        pass
  
    def sortAppointments(self):
        self._appointmentlist.sort(key = lambda appoint: appoint._starttime)
        self._appointmentlist.sort(key = lambda appoint: appoint._date)
        pass

    def initAllSlots(self):
        start = '12:00AM'
        start = datetime.strptime(start,"%I:%M%p")
        for i in range(48):
            end = start + timedelta(minutes = 30)
            self._alltimeslots[start.strftime("%I:%M%p")] = end.strftime("%I:%M%p")
            start = start + timedelta(minutes = 30)
        pass    
            

    def find_valid_times(self, start_work, end_work, Date, Provider, Centre, date_datetime):
        appointmentlist =Provider.appointments
        print(appointmentlist)
        valid_times = {}
        no_compatible_appoints = True
        booked = False
        self.initAllSlots()
        alltimeslots = self.alltimeslots
        for start, end in alltimeslots.items(): 
            booked = False
            for appointments in appointmentlist:
                if (appointments.centre == Centre)  and (appointments.date == Date):
                    no_compatible_appoints = False
                    if (datetime.strptime(start,"%I:%M%p") == datetime.strptime(appointments.starttime, "%I:%M%p")):
                            booked = True
            if booked == False:
                if (datetime.strptime(start,"%I:%M%p") >= datetime.strptime(start_work,"%I:%M%p")) and (datetime.strptime(start,"%I:%M%p") <      datetime.strptime(end_work,"%I:%M%p")):
                    if date_datetime.day == datetime.today().day:
                        print(start)
                        time_now = (datetime.now()).strftime("%I:%M%p")
                        time_now = datetime.strptime(time_now,"%I:%M%p")
                        if datetime.strptime(start,"%I:%M%p") >= time_now:
                             valid_times[start] = end
                    else:
                        print("what")
                        print(start)
                        valid_times[start] = end
        if no_compatible_appoints == True:
            for start, end in alltimeslots.items():
                if (datetime.strptime(start,"%I:%M%p") >= datetime.strptime(start_work,"%I:%M%p")) and (datetime.strptime(start,"%I:%M%p") < datetime.strptime(end_work,"%I:%M%p")):
                    if date_datetime.day == datetime.today().day:
                         print("ok here")
                         time_now = (datetime.now()).strftime("%I:%M%p")
                         time_now = datetime.strptime(time_now,"%I:%M%p")
                         if datetime.strptime(start,"%I:%M%p") >= time_now:
                             valid_times[start] = end
                    else:
                        valid_times[start] = end
        if len(valid_times) == 0:
            return "There are no available times left for this date. Please choose another."
        return valid_times
                      
    @property
    def appointments(self):
        return self._appointmentlist
    
    @property
    def alltimeslots(self):
        return self._alltimeslots                                          


    '''
    Pickle
    '''
    
    def save_data(self):
        with open('appointments.pickle', 'wb') as appointments_file:
            pickle.dump(self, appointments_file)
    
    def load_data(self):
        try:
            with open('appointments.pickle', 'rb') as appointments_file:
                appointmentSystem = pickle.load(appointments_file)
        except IOError:
            print("ERROR IN OPENING DATA")
            appointmentSystem = AppointmentSystem()
        return appointmentSystem
