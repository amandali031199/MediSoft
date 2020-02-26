from flask_login import UserMixin
from abc import ABC, abstractmethod
from lib.Appointments import *
from lib.AppointmentSystem import *
from datetime import datetime


class User(UserMixin,ABC):
        __id = -1
     
        def __init__(self, email, password, name, phone_no):
            self._id = self._generate_id()
            self._email = email
            self._password = password
            self._name = name
            self._phone_no = phone_no
            self._appointments = []
        @property
        def email(self):
            return self._email
        
        @property
        def name(self):
            return self._name
            
        @property
        def phone_no(self):
            return self._phone_no
            
        @property
        def password(self):
            return self._password
         
        @property
        def is_authenticated(self):
            return True

        @property
        def is_active(self):
            return True

        @property
        def is_anonymous(self):
            return False
 
        def get_id(self):
            """Required by Flask-login"""
            return str(self._id)

        def _generate_id(self):
            User.__id += 1
            return User.__id

        def add_appointments(self,appoint):
            self._appointments.append(appoint)

        def sortAppointments(self):
            self._appointments.sort(key = lambda appoint: appoint._starttime)
            self._appointments.sort(key = lambda appoint: appoint._date)
            pass
            
        @classmethod
        def set_id(cls, id):
            cls.__id = id

        def validate_password(self, password):
            return self._password == password
        
        def as_list():
            pass             
        
        @abstractmethod
        def is_provider(self):
            pass
        
        @phone_no.setter
        def phone_no(self, new_phone_no):
            print("CHANGING PHONE NO FROM")
            print(self._phone_no)
            self._phone_no = new_phone_no
            print("TO")
            print(self._phone_no)
          
           
class Patient(User): 
        def __init__(self, email, password, name, phone_no, medicare_no):
                    
            super().__init__(email, password, name, phone_no)
            self._medicare_no = medicare_no
            self._is_provider = False
            
        @property
        def medicare_no(self):
            return self._medicare_no
            
        @medicare_no.setter
        def medicare_no(self, new_medicare_no):
            print("CHANGING MEDICARE NO FROM")
            print(self._medicare_no)
            self._medicare_no = new_medicare_no
            print("TO")
            print(self._medicare_no)
    
        @property
        def appointments(self):
            return self._appointments
        
        @property
        def is_provider(self):
            return False
            
        
        def __str__(self):
            return ('Patient email : {} password: {} name: {}, phone_no {}, medicare_no {}, is_provider {}'.format(self._email, self._password, self._name, self._phone_no, self._medicare_no, self.is_provider))
        

        #addappoitnments method 
           
        #def as_list():
            #return {'patient_email:{}'.format(self.patient_email),'name :{}'.format(self._name)}
           
            
                                                                                                                                                                        
          #addappoitnments method 

class Provider(User):
        def __init__(self, email, password, name, phone_no, provider_no,
                        service,affiliated_centres,start_work, end_work):
            super().__init__(email, password, name, phone_no)
            self._provider_no = provider_no
            self._service = service
            self._affiliated_centres = affiliated_centres
            self._start_work = start_work
            # times are input as h:mAM/PM , assume providers work the same shifts everyday
            self._end_work = end_work
            self._is_provider = True
            self._ratings = {}
            
        
        @property
        def provider_no(self):
            return self._provider_no
            
        @provider_no.setter
        def provider_no(self, new_provider_no):
            print("CHANGING PROVIDER NO FROM")
            print(self._provider_no)
            self._provider_no = new_provider_no
            print("TO")
            print(self._provider_no)
            
        '''@property
        def is_provider(self):
            return self._is_provider
        '''
            
        @property
        def service(self):
            return self._service
            
        @property
        def appointments(self):
            return self._appointments
        
        @property
        def affiliated_centres(self):
            return self._affiliated_centres
            
        def add_affiliated_centres(self,centre):
            self._affiliated_centres.append(centre)

        def is_provider(self):
            return True

        #returns time as a printable string
        @property
        def start_work(self):
            return self._start_work    
        @start_work.setter
        def start_work(self,newtime):
            self._start_work = datetime.strptime(newtime,"%I:%M%p")
 
        #returns time as datetime object
        @property
        def start_work_datetime(self):
            return self._start_work

        @property
        def end_work(self):
            return self._end_work
        @end_work.setter
        def end_work(self,newtime):
            self._end_work = datetime.strptime(newtime,"%I:%M%p")
        
        @property
        def end_work_datetime(self):
            return self._end_work
            
        @property
        def ratings(self):
            return self._ratings
        
        def add_rating(self, patient, rating):
            return self.ratings.update({patient:rating})  
        
        def average_rating(self):
            count = 0
            _sum = 0
            for key in self.ratings:
                print("rating here")
                count += 1
                _sum += self.ratings[key]
            #return _sum/count
            if count == 0:
                return 0
            else:
                return round(_sum/count,2)
        
        
        def __str__(self):
            return ('Provider email : {} password: {} name: {}, phone_no: {}, provider_no: {}, provider_service: {} is_provider: {} affiliated_centres: {}'.format(self._email, self._password, self._name, self._phone_no, self._provider_no, self._service, self._is_provider, self._affiliated_centres))

        '''
        def add_appointment(...):
            self._appointments.append(Appointment(...))
        '''
