from flask import render_template, request, redirect, url_for
from flask_login import LoginManager,login_user, current_user, login_required, logout_user
from lib.User import User
from lib.UserManager import *
from lib.HealthCentre import *
from server import app,auth_manager,system
from lib.AppointmentSystem import *
from lib.Appointments import *
from Database import *
from lib.HealthSystem import HealthSystem
from datetime import datetime
import string

a = AppointmentSystem()
AppointmentSystem = a.load_data() #not sure where this goes, initialising the whole thing 

'''
provider_db = system.get_providers()
print(provider_db)
patient_db = system.get_patients()
print(patient_db)
centre_db = system.get_centres()
print(centre_db)
patient_email,patient_password = StoreDatabase.readPatient('patient2.csv')
print(patient_email)
provider_email,provider_password,provider_service = StoreDatabase.readProvider('provider2.csv')
print(provider_email)
centre_type,centre_btn,centre_name,centre_number,centre_location = StoreDatabase.readHealthCentre('health_centres2.csv')
print(centre_type)
print("helloo")
system.show_patients
print("World")
provider_db = StoreDatabase.load_data_provider()
print(provider_db)
patient_db = StoreDatabase.load_data_patient()
print(patient_db)
centre_db = StoreDatabase.load_data_centre()
print(centre_db)
'''
@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''

    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        
        if system.login_patient(email, password) == True:
            global is_patient 
            is_patient = True
            return redirect(url_for('home',email = email))
        elif system.login_provider(email, password) == True:
            global is_provider
            is_provider = True
            return redirect(url_for('home_provider',email = email))
        else:
            message = "Login failed.You have inputed the wrong password or username."

    
    return render_template("login.html", message=message)   

        
def get_user(email):
    for user in system.get_patients():
        if user.email == email:
            return user
    for user in system.get_providers():
        if user.email == email:
            return user
            
def get_user_name(name):
    for user in system.get_patients():
        if user.name == name:
            return user
    for user in system.get_providers():
        if user.name == name:
            return user
           
def get_centre(name):
    for centre in system.get_centres():
        if centre.centre_name == name:
            return centre

@app.route('/logout')
@login_required
def logout():
    auth_manager.logout()
    #logout_user 
    return redirect(url_for('login'))


@app.route('/patient_profile/<name>')
@login_required
def patient_profile(name):
    #email=request.args.get('email')
    user = get_user_name(name)
    can_view = False
    patient = True
    history = False
    patient_name = user.name
    patient_email = user.email
    patient_phone_no = user.phone_no
    patient_medicare_no = user.medicare_no
    print(current_user.name)
    if current_user.name == user.name:
        can_view = True
    for person in system.get_providers():
        if person.name == current_user.name:
           patient = False
    if patient == False:
        print('yes')
        appointmentlist = current_user.appointments
        for a in appointmentlist:
            print(a.get_patient().name)
            print(user.name)
            if user.name == a.get_patient().name:
                can_view = True
    for a in user.appointments:
        if a.finish == True:
            history = True    
    system.save_data()
    '''
    users = {"Jack": {name: 'Jack', email: 'jack@gmail.com', 
                      phone: '123456789', medicare: '0001233', 
                      medication: 'Panadol', 
                      past_history: 'Vomiting and diarrhoea'}} 
    '''                 
    return render_template('patient_profile.html', patient_email= patient_email, patient_name = patient_name, patient_phone_no = patient_phone_no, patient_medicare_no = patient_medicare_no, user = user, can_view = can_view, history = history, current_user = current_user)

system.show_providers()


@app.route('/home')       
@login_required 
def home():
    results = [] # I set the default value of results to be 0 
    n_results = [] # name
    service = []
    suburb = []
    p_contact = []
    c_type = []
    p_rating = []
    c_rating = []
    provider_chosen = -1 # when no radio button has been chosen
    name_chosen = -1
    service_chosen = -1
    c_name_chosen = -1
    suburb_chosen = -1
    no_results = -1
    pick_category = 0
    print(current_user)
    print("THIS IS THE CURRENT USER ^")
    # search is the name of the search field
    search_string = ""
    search_string = request.args.get('search')
    
    # select is the radio button 
    select = request.args.get('select')
    
     # the drop down option user select
    chosen_provider = request.args.get('providers')
    chosen_centre= request.args.get('centres')
    
    if search_string:
        no_result = 0
        match = False
        search_string = search_string.upper()
        
        if select == 'provider_btn':
            provider_chosen = 1
            # check which drop down button is selected
            if chosen_provider == "Name":
                name_chosen = 1 
            elif chosen_provider == "Service":
                service_chosen = 1
            else:
                service_chosen = 2
                name_chosen = 2  
            
            n_results,service,p_contact,p_rating = (system.provider_search(name_chosen, service_chosen,search_string)) 
                 
        elif select == 'centre_btn':           
            provider_chosen = 0
            # check which drop down button is selected
            if chosen_centre == "Name":
                c_name_chosen = 1 
            elif chosen_centre == "Suburb":
                suburb_chosen = 1
            else:
                c_name_chosen = 2
                suburb_chosen = 2
            
            
            n_results,c_type,suburb,c_rating = system.centre_search(c_name_chosen, suburb_chosen,search_string)    
             
    elif not search_string:
        no_result = 0
        if select == 'provider_btn':
            # take what was selected with the label, 'provider' 
            #and take into consideration what was searched
            # the ' ' is a default value for provider
            provider_chosen = 1
          
            if chosen_provider == "Name":
                name_chosen = 1  
                service_chosen = -1   
            elif chosen_provider == "Service":
                service_chosen = 1
                name_chosen = -1    
            else:
                pick_category = 1
            
            n_results,service,p_contact,p_rating = (system.provider_search(name_chosen, service_chosen,search_string))
              
        elif select == 'centre_btn':
            #centre_or_provider = 'centres'
            provider_chosen = 0

            if chosen_centre == "Name":
                c_name_chosen = 1
            elif chosen_centre == "Suburb":
                suburb_chosen = 1
            else:
                pick_category = 1
              
            n_results,c_type,suburb,c_rating = system.centre_search(c_name_chosen, suburb_chosen,search_string)
            
    no_results = 0
    if not n_results:
        if not service:
            if not suburb:
                no_results = 1
    if (current_user.is_provider):
        return render_template('404.html'), 404                    
    return render_template('home.html', results=n_results,service = service,
                            suburb = suburb, c_type = c_type, c_rating = c_rating, pick_category=pick_category,
                            provider_chosen=provider_chosen,service_chosen=service_chosen,
                            name_chosen=name_chosen,c_name_chosen = c_name_chosen, 
                            suburb_chosen=suburb_chosen,p_contact = p_contact,p_rating = p_rating, no_results=no_results,
                            provider_choices=['Pick category','Service', 'Name'],
                            centre_choices=['Pick category','Suburb', 'Name'],search_string = search_string)


#temporary to test html, providers and patients should have a link based on their name


@app.route('/home_provider')
@login_required
def home_provider():
    email=request.args.get('email')
    #user = get_user(email)
    #name = user.name
    name = ' '
    if not (current_user.is_provider):
        return render_template('404.html'), 404  
    return render_template('home_provider.html', name = name)

@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

@app.route('/booking/<provider_name>/<centre>/<start>/<end>',methods=['GET', 'POST'])
@login_required
def booking(provider_name,centre,start,end): #should take in Provider, Centre
    print(provider_name)
    print(centre)
    print(start)
    print(end)
    Date =""
    Provider = get_user_name(provider_name)
    Centre = get_centre(centre)
    start_work = start
    end_work = end
    print(start_work)
    valid_times = {}
    message = ""
    Reason = ""

    #end_work = Provider.end_work
    if request.method == "POST":
        message = ""
        if request.form['btn_identifier'] == 'viewtimes':
            print('inside')
            Date = request.form['date']
            try:
                assert(Date)
            except AssertionError:
                print("fgh")
                message = message +' Please enter in a date you want to book an appointment at.'
            
            if Reason != "":
                print(Reason)
                try:
                    assert(str.isnumeric(Reason) == False)
                    # check if reason only contains punctuation marks or whitespace
                    valid = 0
                    for char in Reason:
                        if char not in string.punctuation and char not in string.whitespace:
                            valid = 1
                            break
                    assert(valid == 1)
                    
                except AssertionError:
                    message = message +' Please write a valid reason.'
            
            if message != '':
                return render_template('bookings.html', message = message )
            date_datetime = datetime.strptime(Date,"%d-%m-%Y")
            print(Date)
            #date_datetime = datetime.strptime(Date, "%d-%m-%Y")
            valid_times = AppointmentSystem.find_valid_times(start_work, end_work, Date, Provider, Centre, date_datetime)
            if isinstance(valid_times,str) == True:
                message = message + valid_times
                valid_times = {}
            return render_template('bookings.html', valid_times = valid_times, date = Date,
                                   centre = Centre, provider = Provider, viewtimes = True, message = message)
        
        if request.form['btn_identifier'] == 'finishbooking':
            #make appointment, add appointment redirect to confirm
            print('finish')
            Start = ""
            Empty = False
            Reason = request.form['reason']
            
            # user input error handling
            try:
                Date = request.form['date']
                assert(Date)
            except AssertionError:
                print("fgh")
                message = message +' Please enter in a date you want to book an appointment at.'
            
            if Reason != "":
                print(Reason)
                try:
                    assert(str.isnumeric(Reason) == False)
                   
                    # check if reason only contains punctuation marks or whitespace
                    valid = 0
                    for char in Reason:
                        if char not in string.punctuation and char not in string.whitespace:
                            valid = 1
                            break
                    assert(valid == 1)
                    
                except AssertionError:
                    message = message +' Please write a valid reason.'
            print('ertre')
            try: 
                Start = request.form.get('time')
                assert(Start)
                print("thru")
            except AssertionError:
                message = message = 'Please select a time slot.'
            if message != '':
                print("final")
                return render_template('bookings.html', valid_times = valid_times, date = Date,
                                   centre = Centre, provider = Provider, viewtimes = True, message = message)
            Start = request.form['time']
            date_datetime = datetime.strptime(Date,"%d-%m-%Y")
            Start = datetime.strptime(Start,"%I:%M%p")
            End = Start + timedelta(minutes = 30)
            End = End.strftime("%I:%M%p")
            Start = Start.strftime("%I:%M%p")
            Patient = current_user.name
            Patient = get_user_name(Patient)   
            if Reason == "":
                Reason = 'N/A' 
            appointment = Appointment(Date, Start, End, Centre, Provider, Patient, Reason)
            print(appointment.date)
            print(appointment.starttime + appointment.endtime + appointment.centre.centre_name + appointment.provider.name + appointment.get_patient().name + appointment.reason)
            Patient.add_appointments(appointment)
            Patient.sortAppointments()
            Provider.add_appointments(appointment)
            Provider.sortAppointments()
            AppointmentSystem.addAppointment(appointment)
            AppointmentSystem.sortAppointments()
            system.save_data()
            
            if (current_user.is_provider):
                return render_template('404.html'), 404
        
            return redirect(url_for('confirm', patient = current_user.name,provider = Provider.name, centre = Centre.centre_name, date = Date, starttime = Start, endtime = End, message = message))
    return render_template('bookings.html', message = message)

@app.route('/confirm/<patient>/<provider>/<centre>/<date>/<starttime>/<endtime>')
def confirm(patient,provider, centre, date, starttime, endtime):
    return render_template('confirmation_page.html', patient = patient,
                           centre = centre, provider = provider,
                           date = date, start = starttime,
                           end = endtime)


@app.route('/health_centre_profile/<name>',methods=['GET', 'POST'])
@login_required
def health_centre_profile(name):
    #name=request.args.get('name')

    centre= get_centre(name)
    centre_name = centre.centre_name 
    centre_location = centre.centre_location
    centre_abn= centre.centre_abn
    centre_number= centre.centre_number
    centre_type= centre.centre_type
    affiliated_providers = centre.affiliated_providers
    affiliated_provider_names = []
    affiliated_provider_service = []
    affiliated_provider_id = []
    start_work = []
    end_work = []
    for provider in affiliated_providers:
        user = get_user(provider)
        if user == None:
            break
        print(provider)
        for j in range(len(user.affiliated_centres)):
            print("in")
            if centre_name == user.affiliated_centres[j]:
                print(user.start_work[j])
                start_work.append(user.start_work[j])
                end_work.append(user.end_work[j])
                break
        affiliated_provider_names.append(user.name)
        affiliated_provider_service.append(user.service)
        affiliated_provider_id.append(user.get_id)
    average_rating = centre.average_rating()
    print(centre.average_rating())
    print(start_work)
    print(end_work)
    if request.method == "POST":
        if request.form['btn_identifier'] == 'submit':
            rating = int(request.form['rating'])
            print(rating)
            centre.add_rating(current_user.name, rating)    
    average_rating = centre.average_rating()
    system.save_data()    
        
    is_prov = 0
    if (current_user.is_provider):
        is_prov = 1
        return render_template('health_centre_profile.html',centre_name =centre_name, centre_location=centre_location, centre_abn=centre_abn, centre_number=centre_number, centre_type=centre_type, affiliated_provider_names = affiliated_provider_names, affiliated_provider_service = affiliated_provider_service, affiliated_provider_id = affiliated_provider_id,is_prov = is_prov, average_rating = average_rating, start_work = start_work, end_work = end_work) 
    return render_template('health_centre_profile.html',centre_name =centre_name, centre_location=centre_location, centre_abn=centre_abn, centre_number=centre_number, centre_type=centre_type, affiliated_provider_names = affiliated_provider_names, affiliated_provider_service = affiliated_provider_service, affiliated_provider_id = affiliated_provider_id,is_prov = is_prov, average_rating = average_rating, start_work = start_work, end_work = end_work) 
    

@app.route('/health_provider_profile/<name>',methods=['GET', 'POST'])
@login_required
def health_provider_profile(name):
    #name=request.args.get('name')

    print(name)
    user = get_user_name(name)
    user_id = user.get_id
    #if user.is_provider == False:
    #    return redirect(url_for('patient_profile'))
    provider_name = user.name 
    provider_no = user.provider_no
    provider_phone = user.phone_no
    provider_service = user.service
    affiliated_centres = user.affiliated_centres

    average_rating = user.average_rating()
    print(user.average_rating())
    
    if request.method == "POST":
        if request.form['btn_identifier'] == 'submit':
            rating = int(request.form['rating'])
            print(rating)
            
            user.add_rating(current_user.name, rating)

    provider_start_work = user.start_work
    provider_end_work = user.end_work
    for n in provider_start_work:
        print(provider_name)
        print (n)

    '''if request.method == "POST":
        provider = user #change to whoever the provider's profile is
        centre = request.form['Centre']
        
        for centres in centre_db:
            if centre == centres.centre_name:
                centre = centres
                break 
        return redirect(url_for('booking'),Provider = provider, Centre = centre)'''

    average_rating = user.average_rating()
    system.save_data()
    print(user.average_rating())

    is_prov = 0
    if (current_user.is_provider):
        is_prov = 1
        return render_template('health_provider_profile.html', provider_name = provider_name, provider_no = provider_no, provider_phone = provider_phone, provider_service = provider_service, affiliated_centres = affiliated_centres, user_id = user_id,start_work = provider_start_work,end_work = provider_end_work,is_prov=is_prov, average_rating = average_rating) 
        
    return render_template('health_provider_profile.html', provider_name = provider_name, provider_no = provider_no, provider_phone = provider_phone, provider_service = provider_service, affiliated_centres = affiliated_centres, user_id = user_id,start_work = provider_start_work,end_work = provider_end_work,is_prov=is_prov, average_rating = average_rating)   

@app.route('/appointment')
@login_required
def appointment_history():
    user_name = current_user.name
    #if person logged in is patient
    for user in system.get_patients():
        if user.name == current_user.name:
            patient = True
    #if person logged in is provider change to 
    for user in system.get_providers():
        if user.name == current_user.name:
           patient = False
    user = current_user
    appointmentlist = user.appointments
    print(user.name)
    return render_template('appointment_history.html',appointmentlist = appointmentlist, patient = patient, user_name = user_name)

@app.route('/upcoming_appointments')
@login_required
def upcoming_appointments():
    user_name = current_user.name
    #if person logged in is patient
    for user in system.get_patients():
        if user.name == current_user.name:
            patient = True
    #if person logged in is provider change to 
    for user in system.get_providers():
        if user.name == current_user.name:
           patient = False
    user = current_user
    appointmentlist = []
    for app in user.appointments:
        if app.finish == False:
            appointmentlist.append(app)
    print(user.name)
    return render_template('upcoming_appointments.html',appointmentlist = appointmentlist, patient = patient, user_name = user_name)

@app.route('/past_appointments')
@login_required
def past_appointments():
    user_name = current_user.name
    #if person logged in is patient
    for user in system.get_patients():
        if user.name == current_user.name:
            patient = True
    #if person logged in is provider change to 
    for user in system.get_providers():
        if user.name == current_user.name:
           patient = False
    user = current_user
    appointmentlist = []
    for app in user.appointments:
        print(app.finish)
        if app.finish == True:
            appointmentlist.append(app)
    print(user.name)
    return render_template('past_appointments.html',appointmentlist = appointmentlist, patient = patient, user_name = user_name)

@app.route('/patient')
@login_required
def patient_history():
     #given the user provider: access the providers list of appointments
     Provider = current_user #for now
     seen = set()
     Provider.appointments.reverse()
     uniquelist = [appointment for appointment in Provider.appointments if appointment.get_patient().name 
                   not in seen and not seen.add(appointment.get_patient().name)]
     Provider.appointments.reverse()
     return render_template('patient_history.html', appointmentlist = uniquelist)


    
@app.route('/create_notes/<appointment_id>/<name>',methods=['GET', 'POST'])
@login_required
def create_notes(appointment_id, name):
    user = get_user_name(name)
    appointment_id = int(appointment_id)
    appointment = user.appointments[appointment_id]
    patient = False
    notes = 'N/A'
    medication = 'N/A'
    if request.method == 'POST':
        notes = request.form['notes'] #wtf none of the methods work
        medication = request.form['medication']
        if notes.isspace() == True:
            notes = 'N/A'
        if medication.isspace() == True:
            medication = 'N/A'
        #save notes and medication
        Patient = appointment.get_patient()
        appointment.add_notes(notes)
        appointment.add_medications(medication)
        appointment.set_finish(True)
        return render_template('appointment_history.html',appointmentlist = user.appointments, patient = patient, user_name = name)
    return render_template('create_notes.html', patient_name = appointment.get_patient().name)

@app.route('/edit_notes/<appointment_id>/<name>',methods=['GET', 'POST'])
@login_required
def edit_notes(appointment_id, name): 
    user = get_user_name(name)
    appointment_id = int(appointment_id)
    appointment = user.appointments[appointment_id]
    notes = appointment.notes
    medication = appointment.medications
    if request.method == 'POST':
        notes = request.form.get('notes')
        medication = request.form.get('medication')
        if notes.isspace() == True:
            notes = 'N/A'
        if medication.isspace() == True:
            medication = 'N/A'
        #save notes and medication
        Patient = appointment.get_patient()
        appointment.add_notes(notes)
        appointment.add_medications(medication)
        appointment.set_finish(True)
        can_view = True
        history = True
        system.save_data()
        return render_template('patient_profile.html', patient_email= Patient.email, patient_name = Patient.name, patient_phone_no = Patient.phone_no, patient_medicare_no = Patient.medicare_no, user = Patient, can_view = can_view, history = history, current_user = current_user)
    return render_template('edit_notes.html', patient_name = appointment.get_patient().name, medication = medication, notes = notes)
     
@app.route('/edit_profile',methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = current_user.name
    user = get_user_name(user)
    error_msg = ""
    if current_user.is_provider == False:
        patient_name = user.name
        patient_email = user.email
        patient_phone_no = user.phone_no
        patient_medicare_no = user.medicare_no
        
        if request.method == 'POST':
            if request.form['submit'] == 'Submit':
                error_msg = ""
                new_phone_number = request.form['new_phone_number']
                new_medicare_no = request.form['new_medicare_no']
                print(user.phone_no)
                
                
                try:
                    assert(new_phone_number)
                except AssertionError:
                    print("fgh")
                    error_msg = error_msg +' Please enter a valid phone number.'
                
                if new_phone_number != "":
                    try:
                        assert(str.isnumeric(new_phone_number) == True)
                    except AssertionError:
                        error_msg = error_msg +' Phone numbers should only contain numbers.'
                
                    '''
                    # can't get the same medicare no as someone else
                    valid = 1
                    for j in system.get_patients():
                        for i in j.medicare_no():
                            if i == new_medicare_no:
                                valid = 0
                    assert(valid == 1)
                    '''
                try: 
                    # only see to work after you save it for the first time
                    valid = 1
                    if new_medicare_no == patient_medicare_no or new_phone_number == patient_phone_no:
                        valid = 0
                    assert(valid == 1)
                    assert(new_medicare_no)
                except AssertionError:
                    print("fgh")
                    error_msg = error_msg +' Please enter a valid medicare number.'
               
                if new_medicare_no != "":
                    try:
                        assert(str.isnumeric(new_medicare_no) == True)
                    except AssertionError:
                        error_msg = error_msg +' Medicare numbers should only contain numbers.'
                
                if error_msg != '':
                    error_msg = error_msg +' Please try again.'
                    return render_template('edit_patient_profile.html', patient_name = patient_name, patient_email = patient_email, patient_phone_no = patient_phone_no, patient_medicare_no = patient_medicare_no, error_msg = error_msg)
                    
                    
                    
                user.phone_no = new_phone_number
                print(user.phone_no)
                print("uwahhhh2")
                user.medicare_no = new_medicare_no
                error_msg = "Saved!"
        system.save_data()
        patient_name = user.name
        patient_email = user.email
        patient_phone_no = user.phone_no
        patient_medicare_no = user.medicare_no
        return render_template('edit_patient_profile.html', patient_name = patient_name, patient_email = patient_email, patient_phone_no = patient_phone_no, patient_medicare_no = patient_medicare_no, error_msg = error_msg)
    else:
        provider_name = user.name
        provider_phone_no = user.phone_no
        provider_no = user.provider_no
        if request.method == 'POST':
            if request.form['submit'] == 'Submit':
                error_msg = ""
                new_phone_number = request.form['new_phone_number']
                new_provider_no = request.form['new_provider_no']
                print(user.phone_no)
                print("uwahhhh")
                try:
                    assert(new_phone_number)
                except AssertionError:
                    print("fgh")
                    error_msg = error_msg +' Please enter a valid phone number.'
                if new_phone_number != "":
                    try:
                        assert(str.isnumeric(new_phone_number) == True)
                    except AssertionError:
                        error_msg = error_msg +' Phone numbers should only contain numbers.'
                        
                try:
                    assert(new_provider_no)
                except AssertionError:
                    print("fgh")
                    error_msg = error_msg +' Please enter a valid provider number.'
                
                if new_provider_no != "":
                    try:
                        assert(str.isnumeric(new_provider_no) == True)
                    except AssertionError:
                        error_msg = error_msg +' Provider numbers should only contain numbers.'
                
                if error_msg != '':
                    error_msg = error_msg +' Please try again.'
                    print(error_msg)
                    return render_template('edit_provider_profile.html', provider_name = provider_name, provider_phone_no = provider_phone_no, provider_no = provider_no, error_msg = error_msg)

                user.phone_no = new_phone_number
                print(user.phone_no)
                user.provider_no = new_provider_no
                error_msg = 'Saved!'
        system.save_data()
        provider_name = user.name
        provider_phone_no = user.phone_no
        provider_no = user.provider_no
        return render_template('edit_provider_profile.html', provider_name = provider_name, provider_phone_no = provider_phone_no, provider_no = provider_no, error_msg = error_msg)
    

