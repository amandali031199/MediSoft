class HealthCentre: 
        def __init__(self,centre_type,centre_abn,centre_name,centre_number,centre_location, affiliated_providers):

            self._centre_type = centre_type
            self._centre_abn = centre_abn
            self._centre_name = centre_name
            self._centre_number = centre_number
            self._centre_location = centre_location
            self._affiliated_providers = affiliated_providers
            self._ratings = {}

            
        @property
        def centre_type(self):
            return self._centre_type
        
        @property
        def centre_abn(self):
            return self._centre_abn
            
        @property
        def centre_name(self):
            return self._centre_name
        
        @property
        def centre_number(self):
            return self._centre_number
        
        @property
        def centre_location(self):
            return self._centre_location
            
        @property
        def affiliated_providers(self):
            return self._affiliated_providers
            
        def add_affiliated_providers(self,provider):
            self._affiliated_providers.append(provider)
            
        @property
        def ratings(self):
            return self._ratings
        
        def add_rating(self, patient, rating):
            return self.ratings.update({patient:rating})  
        
        def average_rating(self):
            count = 0
            _sum = 0
            for key in self.ratings:
                print(key)
                count += 1
                _sum += self.ratings[key]
            #return _sum/count
            if count == 0:
                return 0
            else:
                return round(_sum/count,2)
        
        
        def __str__(self):
            return ('Centre Type : {} ABN: {} Name: {}, No. {}, Location {} Providers {}'.format(self._centre_type, self._centre_abn, self._centre_name, self._centre_number, self._centre_location, self._affiliated_providers))
        

