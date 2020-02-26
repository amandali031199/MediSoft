from lib.HealthSystem import *
from lib.User import Patient, Provider
from flask_login import current_user, login_required, login_user, logout_user
from flask import redirect, url_for
from functools import wraps
import csv
import pickle
from lib.UserManager import AuthenticationManager
from datetime import datetime

def bootstrap_system(auth_manager):

    system = HealthSystem(auth_manager)

    # IMPORT CSV FILES
    def readPatient(filename):
        patient_email = []
        patient_password = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print('email {} password {}'.format(row['patient_email'], row['password']))
                patient_email.append(row['patient_email'])
                patient_password.append(row['password'])
        return patient_email,patient_password
        
    patient_email,patient_password = readPatient('patient2.csv')

     
        #readPatient('patient.csv')
        
    print(patient_email)
    print(patient_password) 
     
    
        
    def readAffiliation(filename):
        provider_email_centre = []
        health_centre_name =[]
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                provider_email_centre.append(row['provider_email'])
                health_centre_name.append(row['health_centre_name'])
            return provider_email_centre, health_centre_name
        
    provider_email_centre,health_centre_name = readAffiliation('provider_health_centre2.csv')
        
    print(provider_email_centre)
    print(health_centre_name)
        
        
    def readProvider(filename):
        provider_email = []
        provider_password = []
        provider_service = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print('email {} password {} service {}'.format(row['provider_email'], row['password'], row[
                    'provider_type']))
                provider_email.append(row['provider_email'])
                provider_password.append(row['password'])
                provider_service.append(row['provider_type'])
        return provider_email, provider_password, provider_service
    
    provider_email,provider_password,provider_service = readProvider('provider2.csv')
        
    print(provider_email)
    print(provider_password) 
    print(provider_service)
        
    def readHealthCentre(filename):
        centre_type = []
        centre_btn = []
        centre_name = []
        centre_number = []
        centre_location = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print('Type {} ABN {} Name {} Contact {} Suburb{}'.format(row['centre_type'], row['abn'], row['name'], row['phone'], row['suburb']))
                centre_type.append(row['centre_type'])
                centre_btn.append(row['abn'])
                centre_name.append(row['name'])
                centre_number.append(row['phone'])
                centre_location.append(row['suburb'])
        return centre_type,centre_btn,centre_name,centre_number,centre_location  
            
    centre_type,centre_btn,centre_name,centre_number,centre_location = readHealthCentre('health_centres2.csv')

    print(centre_btn)
    print(centre_name)


    # PUT INTO THE CLASS
    
    # PATIENT
    #name, phone_no, email,password,medicare_no
    phone_no = 618932
    medicare_no = 1717
    patient_names = ["Jack","Tom","Isaac","Hao"]
    counter = 0
    provider_no = 32131

    for name in patient_names:
        email = patient_email[counter]
        password = patient_password[counter]
        phone_no += 1
        medicare_no += 1        
        system.add_patient(Patient(email, password, name, phone_no, medicare_no))
        counter += 1
    
    print("databaseee patient")       
    system.show_patients()
    print("end database patient")   
    # PROVIDER
    provider_names = ["Toby","Gary","Samuel","Sid","Michael","Anna","Thomas","Ian"]
    #start_work = '1:00PM' #trying to give working hours to providers not complete
    #end_work = '3:00PM'
    counter2 = 0       
    start_work = []
    end_work= []
    for n in provider_names:
        i = 0
        affiliated_centres = []
        email = provider_email[counter2]
        pw = provider_password[counter2]
        service = provider_service[counter2]
        phone_no += 1
        provider_no += 1
        if ((n == "Samuel") or (n == "Sid") or (n == "Michael") or (n == "Thomas") or (n=="Ian")):
           start_work.append('9:00AM')
           end_work.append('5:00PM')
        elif ((n == "Toby") or (n == "Gary")):
            start_work.append('9:00AM')
            start_work.append("3:00PM")
            end_work.append('11:00AM')
            end_work.append("5:00PM")
        elif ((n == "Anna")):
            start_work.append('8:00AM')
            start_work.append("1:00PM")
            start_work.append("3:00PM")
            end_work.append('10:00AM')
            end_work.append('2:00PM')
            end_work.append("5:00PM")
        for names in provider_email_centre:
            if names == email:
                affiliated_centres.append(health_centre_name[i])
            i += 1
        p = Provider(email, pw, n, phone_no, provider_no, service,affiliated_centres,start_work,end_work)
        system.add_provider(p)
        #clear the list!
        start_work = []
        end_work = []
        counter2 += 1
        
    print("databaseee") 
    system.show_providers()
    print("end data")
    #s = Provider()
    print("S IS HERE " )
    #print(s.email)
    #print(s)   
        # CENTRE
    counter3 = 0
    for centre_n in range(len(centre_name)):
        i = 0
        affiliated_providers = []
        c_type = centre_type[counter3]
        c_btn = centre_btn[counter3]
        c_name = centre_name[counter3]
        c_number = centre_number[counter3]
        c_location = centre_location[counter3]
        for names in health_centre_name:
            if names == c_name:
                affiliated_providers.append(provider_email_centre[i])
            i += 1
        system.add_centre(c_type,c_btn,c_name,c_number,c_location, affiliated_providers)
        counter3 += 1
        system.show_centres()
    
    return system
    
    
'''   
################################ 
from flask import Flask
from flask_login import LoginManager
from flask_login import LoginManager  
app = Flask(__name__)
app.secret_key = 'very-secret-123' 

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class StoreDatabase:  
    auth_manager = AuthenticationManager(login_manager)
    provider_system = ProviderSystem(auth_manager)
    system = HealthSystem(provider_system,auth_manager)
    
    def readPatient(filename):
        patient_email = []
        patient_password = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print('email {} password {}'.format(row['patient_email'], row['password']))
                patient_email.append(row['patient_email'])
                patient_password.append(row['password'])
        return patient_email,patient_password
    patient_email,patient_password = readPatient('patient2.csv')

 
    #readPatient('patient.csv')
   
    def readAffiliation(filename):
        provider_email_centre = []
        health_centre_name =[]
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                provider_email_centre.append(row['provider_email'])
                health_centre_name.append(row['health_centre_name'])
        return provider_email_centre, health_centre_name
    
    provider_email_centre,health_centre_name = readAffiliation('provider_health_centre2.csv')
    
    print(provider_email_centre)
    print(health_centre_name)
    

    def readProvider(filename):
        provider_email = []
        provider_password = []
        provider_service = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print('email {} password {} service {}'.format(row['provider_email'], row['password'], row[
                'provider_type']))
                provider_email.append(row['provider_email'])
                provider_password.append(row['password'])
                provider_service.append(row['provider_type'])
        return provider_email, provider_password, provider_service
    provider_email,provider_password,provider_service = readProvider('provider2.csv')
    
    print(provider_email)
    print(provider_password) 
    print(provider_service)
    
    def readHealthCentre(filename):
        centre_type = []
        centre_btn = []
        centre_name = []
        centre_number = []
        centre_location = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print('Type {} ABN {} Name {} Contact {} Suburb{}'.format(row['centre_type'], row['abn'], row['name'], row['phone'], row['suburb']))
                centre_type.append(row['centre_type'])
                centre_btn.append(row['abn'])
                centre_name.append(row['name'])
                centre_number.append(row['phone'])
                centre_location.append(row['suburb'])
        return centre_type,centre_btn,centre_name,centre_number,centre_location  
        
    centre_type,centre_btn,centre_name,centre_number,centre_location = readHealthCentre('health_centres2.csv')

    print(centre_btn)
    print(centre_name)

    #store in pickle

    with open('provider.pickle', 'wb') as provider_file:
        pickle.dump(system._providers, provider_file)
            
    with open('patient.pickle', 'wb') as patient_file:
        pickle.dump(system._patients, patient_file)

    with open('centre.pickle', 'wb') as centre_file:
        pickle.dump(system._centres, centre_file)
        
      
    #@classmethod
    def load_data_provider():
        try:
            with open('provider.pickle', 'rb') as provider_file:
                provider_db = pickle.load(provider_file)
        except IOError:
            provider_db = pickle.load(provider_file)
        return provider_db

    def load_data_patient():
        try:
            with open('patient.pickle', 'rb') as patient_file:
                patient_db = pickle.load(patient_file)
        except IOError:
            patient_db = pickle.load(patient_file)
        return patient_db

    def load_data_centre():
        try:
            with open('centre.pickle', 'rb') as centre_file:
                centre_db = pickle.load(centre_file)
        except IOError:
            centre_db = pickle.load(centre_file)
        return centre_db
'''
