from datetime import datetime

class Appointment():
    def __init__(self, date, starttime, endtime, centre, HealthProvider, Patient,reason):
        """
        All appointments made by patients. Dates are inputed as dd-mm-yyyy. 
        Times are inputed as hour:min AM/PM. If want to print date/time string, use appointment._date/._time.strftime("{format}")
        """
        self._date = datetime.strptime(date, "%d-%m-%Y")
        self._starttime = datetime.strptime(starttime, "%I:%M%p")
        self._endtime = datetime.strptime(endtime, "%I:%M%p")
        self._centre = centre            
        self._provider = HealthProvider
        self._patient = Patient
        self._reason = reason
        self._finish = False
        self._notes = "N/A"
        self._medications = "N/A"

    @property
    def notes(self):
        return self._notes
    def add_notes(self, new_notes):
        self._notes = new_notes
    @property
    def medications(self):
        return self._medications
    def add_medications(self,new_med):
        self._medications = new_med
    @property
    def starttime(self):
        return self._starttime.strftime("%I:%M%p")
    @starttime.setter
    def starttime(self,newtime):
        self._starttime = datetime.strptime(newtime,"%I:%M%p")

    @property
    def starttime_datetime(self):
        return self._starttime
        
    @property
    def endtime_datetime(self):
        return self._endtime


    @property
    def endtime(self):
        return self._endtime.strftime("%I:%M%p")
    @endtime.setter
    def endtime(self,newtime):
        self._endtime = datetime.strptime(newtime,"%I:%M%p")

    @property
    def date(self):
        return self._date.strftime("%d-%m-%Y")
    @date.setter
    def date(self,newdate):
        self._time = datetime.strptime(newdate,"%d-%m-%Y")

    @property
    def centre(self):
        return self._centre
    @centre.setter
    def centre(self,newcentre):
        self._centre = newcentre

    @property
    def finish(self):
        return self._finish
    def set_finish(self,new):
        self._finish = new

    @property
    def provider(self):
        return self._provider
    @provider.setter
    def provider(self,newprovider):
        self._provider = newprovider

    def get_patient(self):
        return self._patient

    @property  #doesn't work just use get_patient, this stores the reason instead
    def patient(self):
        return self._patient
    @patient.setter
    def patient(self,newpatient):
        self._patient = newpatient

    @property
    def reason(self):
        return self._reason
    @reason.setter
    def patient(self,newreason):
        self._patient = newreason



'''
tests to make sure its sorting correctly
a1 = Appointment('11/11/2000','1:30AM','a','a','a')
a2 = Appointment('11/11/2000', '2:30AM','a','a','a')
a3 = Appointment('11/12/2000','1:30AM','a','a','a')  
a4 = Appointment('11/12/2000','1:30PM','a','a','a')  

k = AppointmentSystem()
k.addAppointment(a3)
k.addAppointment(a4)
k.addAppointment(a2)
k.addAppointment(a1)

k.sortAppointments()      

for x in k._appointmentlist:
print("date = {}, time = {}".format(x._date.strftime("%d/%m/%Y"),x._time.strftime("%I:%M%p")))  
'''
