# MediSoft
An online healthcare appointment management system (HAMS) that would streamline the process of patients booking healthcare appointments and general practitioners sending referrals to specialists. This was created in a team and I implemented the backend and frontend for the booking algorithm and history of patients and appointments. 
This project was designed using object-oriented design principles and implemented using **Python, Flask,Pickle for database, Jinja2, CSS and HTML. Agile Development** was tested through adapting the website to changes in specifications after the first iteration. 

## Health-Care Centres

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

search for a particular type of service (e.g., GP) (e.g., a search for a ?GP? service will list all the GPs currently registered on the system).

search for health-care providers by their name (e.g., Jackson)

For any of the four search options, the search should not only return the exact matches but ?near-matches? also. For example, if there is a health centre called ?Royal Randwick Hospital?, then it should be returned as a result of the patient searching for ?centres by name? with the keyword ?royal rand?. Each entry of the search result should contain brief details about the centre/provider, and a link to the corresponding profile page.

### Viewing Health Centre Profile

The profile page of a health centre should display details about the centre and its customer rating. Furthermore, there should be a list of all health providers working for the centre, categorised by the type of service they provide. For each provider, there should be a link to the provider?s profile as well as a button to proceed to booking an appointment with the provider at the centre.

### Viewing Health Provider Profile

Similarly, the profile page of a health provider should display details about the health provider, including their average rating. Furthermore, the page should display a list of all affiliated health centres. For each centre, there should be a link to the centre?s profile, as well as a button to proceed to booking an appointment with the provider at the centre.

### Booking an Appointment

Once the patient clicks a button to proceed onto booking an appointment, they should be presented with a form that consists of the following components.

A user-friendly widget that lets the patient select the time slots for the appointment. Every day is partitioned into 48 equally-sized time slots, each of which are 30 minutes long in length. The patient can select available time-slots e.g, [08:00-08:30]

A section for the patient to optionally write a brief reason of visit, e.g. ?I want to take a blood test?.

After selecting the time slots, the patient can click ?book? to finalise the booking. Once the patient has successfully booked the appointment, a confirmation is displayed to the user.

### Provide Rating

Both health providers and health centres have an average rating that is displayed in the search results and their profiles. In addition to viewing profiles, patients should be able to rate any provider or centre registered on the HAMS. If a patient rates the same provider/centre more than once, only the patient?s most recent rating should count towards their overall average rating.

### Viewing Appointments History

A patient should be able to view their own appointments history, a chronological list of their current appointments with the health providers on HAMS. Each entry on the list should contain links to the profile pages of the corresponding health provider and the corresponding health centre.

## Health Providers

### Viewing Appointments History

Similarly, health providers should also have access to their own appointments history, a chronological list of all current appointments made by patients with the provider. Each entry on the list should contain a link to the corresponding patient?s profile page. On the patient?s profile page, the provider should be able to see details about the patient?s past history.

### Viewing Patient History

Registered health-care providers will also be able to use the e-health system. A health-care provider is able to view all their patient appointments. During consultation with a patient, the health-care provider is able to:

record notes of the patient's visit

view the past history of the patient (i.e, notes taken at the previous visit).

record any medication prescribed to the patient

### Login and Authentication

The HAMS must only be accessible by the pre-registered users, whose login credentials will be provided in csv files. Hence, no registration is required yet. Users should be able to log into the system with their email and password. Once a user has logged into the system, they should be granted access to the rest of the features in system already described above.

# Client reflection following the recent iteration demo
The client is satisfied with the overall functionality demonstrated and has requested for some additional changes/enhancements to their existing project specification which are outlined below for your perusal

## Changes to Patient History Management
As a healthcare centre may offer typically many services (e.g. pathology, imaging) which a patient may need following a consultation with a GP, your client feels that the patient history should be more centralised. Further, as providers can work at multiple healthcare centres, they would like access to the patient?s history at all those centres. The rules governing access to patient history are as follows:

A healthcare provider records notes for a patient, following a consultation.
This history will now be visible to subsequent healthcare providers that the patient visits at any healthcare centre.
Each healthcare provider seen by the patient may request access to able to view/edit the history of the patient to add their specific notes during the consultation with the patient. Healthcare providers will not be able to edit the past history recorded by other providers, but will only be able to add their own specific notes about the patient?s visit.
A few sample scenarios are provided below to clarify this feature:
If a GP (Jack) works in centres A and B, and if a patient visits Jack at both centres A and B, then he should be able to access the patient?s past history.
Assume a patient (Tony) has never seen any healthcare provider registered on the system. Tony now sees a GP (Jack) at a centre A. As no previous history exists, Jack will start the history of the patient, recording notes about the consultation. Then Tony makes an appointment to have a scan with a radiographer at centre B. The radiographer will now be able to click on the patient?s appointment and then click on the patient?s history and record their findings following the scan, e.g. ?Patient?s scan showed a lesion of size 1cm, features suggestive of tumour, biopsy recommended. Patient advised to see GP immediately.? Tony then makes an appointment to see his GP (Jack) at a different centre C. Jack will be able to access the patient?s updated history by clicking on the patient?s appointment.
A provider is granted access to a patient?s history only after the patient has made an appointment with the provider.
Healthcare providers in healthcare centres that the patient has not visited must NOT have access to the patient?s history.

## More robust error handling
The clients feel that the current system (demonstrated in the recent iteration) was not robust enough and did not have adequate error handling. They have not done an exhaustive user-acceptance testing, but these are some of the flaws that were picked by the client:

Unauthorised access to dashboards of roles.
Patients were able to book appointments with invalid inputs (e.g. invalid date/period).
Patients were able to book multiple appointments in the same day/time-slot.
Providers were able to book appointments for themselves.
Searches were not flexible enough. (There should be support for partial name matches, case-insensitive matches, etc.)
## Provision of a new type of provider - 'Specialist' and a referral system
The client has requested an optional feature if the current project velocity permits - book appointments with specialists and an automated referral system. This functionality will support the following features:

The system will add a new healthcare provider, a specialist. For each specialist, details similar to that of a GP will need to be stored. In addition each specialist will have an expertise in a particular health-related area.
Patients will now be able to search for a particular specialist in a particular healthcare domain.
Patients will also be able to book an appointment with a specialist, but they will only be able to make this appointment once the GP has sent a referral to the specialist.
During a consultation, a GP will be able to provide a referral for a patient to a specialist. To implement this feature, during recording details for the patient visit, the GP must also be able to record a letter for a specialist and clicking on a send button will enable the patient to book an appointment with the specialist. (You can make the assumption that clicking on this send button will run a background process to send the email to the specialist. The email functionality does not need to be implemented.)
A specialist will also be able to access a patient?s history, once the patient has made an appointment with the specialist.
The clients have expressed that they would like to see all of the above flaws handled and they will conduct more exhaustive user-acceptance testing in the next iteration.

Unless otherwise stated, all the features that the client had requested in the original specification remain valid.
