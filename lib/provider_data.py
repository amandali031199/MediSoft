from lib.catalogue import *
from lib.warehouse import Warehouse
import csv                                                                       

class Provider_search_data:
    def load_data():
        # make lists of all provider's details that will be shown in the 
        # search results
        
        prov_name = ["Toby", "Gary", "Samuel", "Sid", "Michael", "Anna",
                     "Thomas", "Ian"]
        prov_contact = [12345678, 12344324, 10303231, 1111111, 22222222, 
                        33333333, 44444444, 55555555]
        prov_affiliated_centres = [] 
        prov_service = []
        
        with open('provider.csv') as providers_file:
            values = csv.reader(providers_file, delimiter=',') 
            for row in providers_file:
                prov_affiliated_centres.append(row[1])
                prov_service.append(row[2])
     
        # initialise instance variables found in catalogue
        # rating is 0 since the rating system has not been implemented yet 
        
        warehouse = Warehouse()
        
        #for i in range(len(prov_name)):
            #item = Provider(prov_name[i], 0, prov_contact[i], prov_service[i], prov_affiliated_centres[i])
            # key = ['name', 'rating', 'contact', 'services', 'affiliated_centres']
            # item = dict(zip(key, values2)
        warehouse.add_item(prov_name)
        warehouse.add_item(prov_contact)
        warehouse.add_item(prov_service)
        warehouse.add_item(prov_affiliated_centres)
       
        return warehouse
        
        
            
       
    
