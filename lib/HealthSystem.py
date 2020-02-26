from lib.Appointments import *
from lib.User import Patient, Provider
from lib.HealthCentre import *
from Database import *
from server import *
import copy
import pickle

class HealthSystem:
    def __init__(self,auth_manager):
        self.patients = []
        self.providers = []
        self.centres = []
        self._bookings = []
        #self._provider_system = provider_system
        self._auth_manager = auth_manager
    
              
    def add_patient(self,patient):
        self.patients.append(patient)
        
    def show_patients(self):
        for i in self.patients:
            print(i)
        return 0
    
    def get_patients(self):
            return self.patients
            
    def add_provider(self, provider):
        self.providers.append(provider)
        
    def show_providers(self):
        for i in self.providers:
            print(i)
        return 0

    
    def get_providers(self):
            return self.providers
        
    def add_centre(self,centre_type,centre_btn,centre_name,centre_number,centre_location, affiliated_providers):
        self.centres.append(HealthCentre(centre_type,centre_btn,centre_name,centre_number,centre_location, affiliated_providers))

        
    def show_centres(self):
        for i in self.centres:
            print(i)
        return 0

    def get_centres(self):
            return self.centres
            
    def get_user_by_id(self, user_id):
        for c in self.patients:
            if c.get_id() == user_id:
                return c
        for provider in self.providers:
            if provider.get_id() == user_id:
                return provider
        return None        
    
    '''
    Search Processing 
    '''
    def provider_search(self, name_chosen, service_chosen,search_string):

        results = []
        service = []
        p_contact = []
        p_rating = []
        match = False
        
        if not search_string:
            for provider in self.providers:
                results.append(provider.name)
                service.append(provider.service)
                p_contact.append(provider.phone_no)
                p_rating.append(provider.average_rating())
        
        else:
            if name_chosen == 1:
                for provider in self.providers:
                    j = 0
                    for j in range(len(search_string)):
                        if search_string[j] == provider.name[j].upper():
                            match = True  
                        else:
                            match = False
                            break      
                    if provider.name not in results and match == True:
                        results.append(provider.name)
                        service.append(provider.service)
                        p_contact.append(provider.phone_no)
                        p_rating.append(provider.average_rating())
            
            if service_chosen == 1:
                for provider in self.providers:
                    j = 0
                    for j in range(len(search_string)):
                        if search_string[j] == provider.service[j].upper():
                            match = True  
                        else:
                            match = False
                            break      
                    if provider.name not in results and match == True:
                        results.append(provider.name)
                        service.append(provider.service)
                        p_contact.append(provider.phone_no) 
                        p_rating.append(provider.average_rating()) 
                               
        '''
        for i in range(len(provider_db)): 
                    j = 0
                    for j in range(len(search_string)):
                        if search_string[j] == provider_db[i].name[j]:
                            match = True  
                        else:
                            match = False
                            break       
                    if provider_db[i].name not in n_results and match == True:
                        n_results.append(provider_db[i].name)
                        service.append(provider_db[i].service)
                        p_contact.append(provider_db[i].phone_no)    
        '''
        return results,service,p_contact,p_rating
        
                        
    def centre_search(self,c_name_chosen, suburb_chosen,search_string):

        results = []
        c_type = []
        suburb = []
        c_rating = []
        
        if not search_string:
            for centre in self.centres:
                results.append(centre.centre_name)
                c_type.append(centre.centre_type)
                suburb.append(centre.centre_location)
                c_rating.append(centre.average_rating())
        else:
            if c_name_chosen == 1:
                for centre in self.centres:
                    j = 0
                    for j in range(len(search_string)):
                        if search_string[j] == centre.centre_name[j].upper():
                            match = True  
                        else:
                            match = False
                            break      
                    if centre.centre_name not in results and match == True:
                        results.append(centre.centre_name)
                        c_type.append(centre.centre_type)
                        suburb.append(centre.centre_location)
                        c_rating.append(centre.average_rating())
            
            if suburb_chosen == 1:
                for centre in self.centres:
                    j = 0
                    for j in range(len(search_string)):
                        if search_string[j] == centre.centre_location[j].upper():
                            match = True  
                        else:
                            match = False
                            break      
                    if centre.centre_location not in results and match == True:
                        results.append(centre.centre_name)
                        c_type.append(centre.centre_type)
                        suburb.append(centre.centre_location)
                        c_rating.append(centre.average_rating())
        
        return results,c_type,suburb,c_rating
        '''
        if c_name_chosen == 1:
                for i in range(len(centre_db)): 
                    j = 0
                    for j in range(len(search_string)):
                        if search_string[j] == centre_db[i].centre_name[j]:
                            match = True 
                        else:
                            match = False
                            break    
                    if centre_db[i].centre_name not in n_results and match == True:
                        n_results.append(centre_db[i].centre_name)
                        c_type.append(centre_db[i].centre_type)
                        suburb.append(centre_db[i].centre_location)
          
            if suburb_chosen == 1:
                for i in range(len(centre_db)): 
                    j = 0
                    for j in range(len(search_string)):
                        if search_string[j] == centre_db[i].centre_location[j]:
                            match = True  
                        else:
                            match = False
                            break      
                    if centre_db[i].centre_name not in n_results and match == True:
                        n_results.append(centre_db[i].centre_name)
                        c_type.append(centre_db[i].centre_type)
                        suburb.append(centre_db[i].centre_location)
         '''   
    '''
    Login Services
    '''

    def login_patient(self, email, password):
        for patient in self.patients:
            if self._auth_manager.login(patient,email, password):
                return True
        return False

    def login_provider(self, email, password):
        for provider in self.providers:
            if self._auth_manager.login(provider,email, password):
                return True
        return False

    '''
    Pickle
    '''
    
    def save_data(self):
        with open('alldata.pickle', 'wb') as all_file:
            pickle.dump(self, all_file)
            print("SYSTEM UPDATE")
    
    def load_data(self,system1):
        try:
            with open('alldata.pickle', 'rb') as all_file:
                system = pickle.load(all_file)
                for i in range(len(system.providers)):
                    print(system.providers[i].phone_no)
                print("READING FROM DATA")
        except IOError:
            print("ERROR IN OPENING DATA")
            system = system1
        return system
