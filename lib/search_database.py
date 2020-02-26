from lib.catalogue import *
from lib.warehouse import Warehouse
import csv                                                                       

class ProviderSearchData:
    def load_data():

        # make lists of all provider's details that will be shown in the 
        # search results
        name = ['Toby', 'Gary', 'Samuel', 'Sid', 'Michael', 'Anna',
                     'Thomas', 'Ian']
        contact = [12345678, 12344324, 10303231, 1111111, 22222222, 
                        33333333, 44444444, 55555555]
        service = []
        affiliated_centres = ['Sydney Children Hospital', 'UTS Health Service',
                                   'Kensington', 'Prince of Wales Hospital', 
                                   'Royal Prince Alfred Hospital', 
                                   'USYD Health Service', 'UTS Health Service',
                                   'Prince of Wales Hospital', 
                                   'Sydney Children Hospital']
        
        with open('provider2.csv') as providers_file:
            reader = csv.DictReader(providers_file)
            for row in reader:
                service.append(row['provider_type'])
     
        # initialise instance variables found in catalogue
        # rating is 0 since the rating system has not been implemented yet 
        
        warehouse = Warehouse()
        for i in range(len(name)):
            item = Provider(name[i], 0, contact[i], service[i], affiliated_centres[i])
            # make a list in this order: ['name', 'rating', 'contact', 'services', 'affiliated_centres']
            # lists will be combined into a nested list
            warehouse.add_provider_details(item)
       
        return warehouse


class CentreSearchData: 
    def load_data2(): 
        name = []
        contact = []
        suburb = []
        c_type = []
        providers = ['Toby', 'Toby', 'Samuel', 'Sid', 'Michael', 'Anna', 
                     'Thomas', 'Ian', 'Gary', 'Anna', 'Anna', 'Gary']
       
        with open('health_centres2.csv') as centres_file:
            reader = csv.reader(centres_file, delimiter=',') 
            for row in reader:
                name.append(row[2])
                c_type.append(row[0])
                suburb.append(row[4])
                contact.append(row[3])
                
       
        # initialise instance variables found in catalogue
        # rating is 0 since the rating system has not been implemented yet 
        
        warehouse = Warehouse()
        for i in range(len(name)):
            item = Centre(name[i], 0, contact[i], suburb[i], c_type[i], providers)
            # make a list in this order: ['name', 'rating', 'contact', 'suburb', 'centre_type', 'providers']
            # lists will be combined into a nested list
            warehouse.add_centre_details(item)
      
        return warehouse
