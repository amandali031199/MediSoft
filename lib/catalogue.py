# catalogue to provide results for patient's search
from lib import *
from abc import ABC, abstractmethod


class Health_system(ABC):
        
    @abstractmethod
    def __init__(self, name, rating, contact):
        self._name = name
        self._rating = rating
        self._contact = contact
        
    @property
    def name(self):
        return self._name
     
    @property
    def rating(self):
        return self._rating
        
    @property
    def contact(self):
        return self._contact
    
   
class Provider(Health_system):
    def __init__(self, name='none', rating=0.0, contact=00000000, service='none', affiliated_centre='none'):
        super().__init__(name, rating, contact)
        self._service = service
        self._affliated_centre = affiliated_centre

    def get_service(self):
        return self._service

    def get_affiliated_centre(self):
        return self._affiliated_centre


class Centre(Health_system):
    def __init__(self, name='none', rating=0.0, contact=00000000, suburb='none', type_centre='none', providers='none'):
        super().__init__(name, rating, contact)
        self._suburb = suburb
        self._type_centre = type_centre
        self._providers = providers
        
    def get_suburb(self):
        return self._suburb

    def get_type_centre(self):
        return self._type_centre
        
    def get_providers(self):
        return self._providers


