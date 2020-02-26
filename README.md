# MediSoft
An online healthcare appointment management system (HAMS) that would streamline the process of patients booking healthcare appointments and general practitioners sending referrals to specialists. This was created in a team and I implement the backend and frontend for the booking algorithm and history of patients and appointments. The website was created using object-oriented design principles and implemented using **Python, Flask, Jinja2, CSS and HTML. Agile Development** was also tested through change of specifications after the first iteration. 

# Health-Care Centres

The e-health system stores all health-care centres (which can be a hospital or a medical centre) that are affiliated with MediSoft and health-care providers working for these health-care centres. A health centre may employ one or more health providers, and consequently, the set of services provided by a health centre depends on the group of providers working for that centre.

## User Types

The users of the proposed system can be grouped broadly into two categories, namely patients and health-care providers. Every user registered on the system has their full name, email address, and their phone number stored in the system. Patients additionally have their Medicare card number recorded as well, while health providers have their provider number stored on the system.

Health-care providers can be further categorised by their professions, that is, the type of healthcare service they provide. For example, a provider may be classified as a general practitioner (GP), a pharmacist, a physiotherapist or a pathologist. Every health provider has exactly one health profession. A health provider may work for one or more health centres. Furthermore, different health providers may have different workings hours; and if a provider is affiliated with multiple centres, then the provider will have different working hours associated with each centre. (You can assume that these hours do not conflict)

Every user registered on the e-health system can update their personal information through a profile page. For health-care providers, the profile page additionally displays their current rating and the health-centres they are associated with.

## Patients

### Searching for a Healthcare Service to Book an Appointment

On the proposed system, the patients can search for a health provider or a health centre that suits their interest using the search engine provided. The search engine has the following options:

search for a particular health-care centre by their name (e.g., Garners Medical Centre)

search for health-care centres by suburb (e.g., Kensington)

search for a particular type of service (e.g., GP) (e.g., a search for a ‘GP’ service will list all the GPs currently registered on the system).

### search for health-care providers by their name (e.g., Jackson)

For any of the four search options, the search should not only return the exact matches but ‘near-matches’ also. For example, if there is a health centre called “Royal Randwick Hospital”, then it should be returned as a result of the patient searching for ‘centres by name’ with the keyword “royal rand”. Each entry of the search result should contain brief details about the centre/provider, and a link to the corresponding profile page.

### Viewing Health Centre Profile

The profile page of a health centre should display details about the centre and its customer rating. Furthermore, there should be a list of all health providers working for the centre, categorised by the type of service they provide. For each provider, there should be a link to the provider’s profile as well as a button to proceed to booking an appointment with the provider at the centre.

### Viewing Health Provider Profile

Similarly, the profile page of a health provider should display details about the health provider, including their average rating. Furthermore, the page should display a list of all affiliated health centres. For each centre, there should be a link to the centre’s profile, as well as a button to proceed to booking an appointment with the provider at the centre.

### Booking an Appointment

Once the patient clicks a button to proceed onto booking an appointment, they should be presented with a form that consists of the following components.

A user-friendly widget that lets the patient select the time slots for the appointment. Every day is partitioned into 48 equally-sized time slots, each of which are 30 minutes long in length. The patient can select available time-slots e.g, [08:00-08:30]

A section for the patient to optionally write a brief reason of visit, e.g. “I want to take a blood test”.

After selecting the time slots, the patient can click ‘book’ to finalise the booking. Once the patient has successfully booked the appointment, a confirmation is displayed to the user.

### Provide Rating

Both health providers and health centres have an average rating that is displayed in the search results and their profiles. In addition to viewing profiles, patients should be able to rate any provider or centre registered on the HAMS. If a patient rates the same provider/centre more than once, only the patient’s most recent rating should count towards their overall average rating.

### Viewing Appointments History

A patient should be able to view their own appointments history, a chronological list of their current appointments with the health providers on HAMS. Each entry on the list should contain links to the profile pages of the corresponding health provider and the corresponding health centre.

## Health Providers

### Viewing Appointments History

Similarly, health providers should also have access to their own appointments history, a chronological list of all current appointments made by patients with the provider. Each entry on the list should contain a link to the corresponding patient’s profile page. On the patient’s profile page, the provider should be able to see details about the patient’s past history.

### Viewing Patient History

Registered health-care providers will also be able to use the e-health system. A health-care provider is able to view all their patient appointments. During consultation with a patient, the health-care provider is able to:

record notes of the patient’s visit

view the past history of the patient (i.e, notes taken at the previous visit).

record any medication prescribed to the patient

### Login and Authentication

The HAMS must only be accessible by the pre-registered users, whose login credentials will be provided in csv files. Hence, no registration is required yet. Users should be able to log into the system with their email and password. Once a user has logged into the system, they should be granted access to the rest of the features in system already described above.
