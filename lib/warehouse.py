from lib.catalogue import *
from lib.search_database import *
from abc import ABC, abstractmethod

class Inventory(ABC):
    @abstractmethod
    def search_provider(self, provider, name):
        pass

    @abstractmethod
    def search_centre(self, centre, name):
        pass

    @abstractmethod 
    def add_provider_details(self, item):
        pass
        
    @abstractmethod
    def add_centre_details(self,item):
        pass
        
    ''' 
    @abstractmethod
    def get_item(self, code):
        pass

    @abstractmethod
    def get_all_items(self):
        pass

    '''
    
class Warehouse(Inventory):
    def __init__(self):
        # database for providers
        self._providers = []
        # database for centres
        self._centres = []
        
    def add_provider_details(self, item):
        nested_list = [item]
        self._providers.append(nested_list)
    
    def add_centre_details(self,item):
        nested_list = [item]
        self._centres.append(nested_list)
   
    # note: name is what the user searched and provider is the choice that 
    # the user selected in the dropdown section
    
    def search_provider(self, provider, name):
        pass

    def search_centre(self, centre, name):
        pass
    
