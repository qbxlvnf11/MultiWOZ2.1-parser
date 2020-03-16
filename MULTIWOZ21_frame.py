class MultiWOZDataFrame:
	def __init__(self):
		self.__domains_list = []
		self.__dialogue_list = []
		self.__dialogue_state_list = []
		self.__dialogue_acts_list = []
	
	def substitute_domain_list(self, domains):
		self.__domains_list = domains
		
	def get_domain_list(self):
		return self.__domains_list
		
	def append_dialogue(self, user_dialogue):
		self.__dialogue_list.append(user_dialogue)
		
	def get_dialogue_list(self):
		return self.__dialogue_list
		
	def append_dialogue_state(self, dialogue_state):
		self.__dialogue_state_list.append(dialogue_state)
		
	def get_dialogue_state_list(self):
		return self.__dialogue_state_list
		
	def append_dialogue_acts(self, dialogue_acts):
		self.__dialogue_acts_list.append(dialogue_acts)
		
	def get_dialogue_acts_list(self):
		return self.__dialogue_acts_list
		
class DialogueState:
	def __init__(self, metadata):
		# taxi
		self.metadata = metadata
		try:
			self.__build_taxi_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'taxi\'':
				self.taxi_bool = False
		try:
			self.__build_police_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'police\'':
				self.police_bool = False
		try:
			self.__build_restaurant_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'restaurant\'':
				self.restaurant_bool = False
		try:
			self.__build_bus_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'bus\'':
				self.bus_bool = False
		try:
			self.__build_hospital_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'hospital\'':
				self.hospital_bool = False
		try:
			self.__build_hotel_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'hotel\'':
				self.hotel_bool = False
		try:
			self.__build_attraction_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'attraction\'':
				self.attraction_bool = False
		try:
			self.__build_train_info()
		except Exception as e:
			#print(e)
			if str(e) == '\'train\'':
				self.train_bool = False
                
	def __build_taxi_info(self):
		self.taxi_bool = True
		# book
		self.taxi_book_booked = self.metadata['taxi']['book']['booked']
		# semi
		self.taxi_semi_leaveAt = self.metadata['taxi']['semi']['leaveAt']
		self.taxi_semi_destination = self.metadata['taxi']['semi']['destination']
		self.taxi_semi_departure = self.metadata['taxi']['semi']['departure']
		self.taxi_semi_arriveBy = self.metadata['taxi']['semi']['arriveBy']
		if self.taxi_semi_leaveAt == '':
			self.taxi_bool = False 
		
	def __build_police_info(self):
		self.police_bool = True
		# book
		self.police_book_booked = self.metadata['police']['book']['booked']
		# semi
		self.police_semi = self.metadata['police']['semi']
		if not self.police_semi:
			self.police_bool = False 
		
	def __build_restaurant_info(self):
		self.restaurant_bool = True
		# book
		self.restaurant_book_booked = self.metadata['restaurant']['book']['booked']
		self.restaurant_book_time = self.metadata['restaurant']['book']['time']
		self.restaurant_book_day = self.metadata['restaurant']['book']['day']
		self.restaurant_book_people = self.metadata['restaurant']['book']['people']
		# semi
		self.restaurant_semi_food = self.metadata['restaurant']['semi']['food']
		self.restaurant_semi_pricerange = self.metadata['restaurant']['semi']['pricerange']
		self.restaurant_semi_name = self.metadata['restaurant']['semi']['name']
		self.restaurant_semi_area = self.metadata['restaurant']['semi']['area']
		if self.restaurant_semi_food == '':
			self.restaurant_bool = False
		
	def __build_bus_info(self):
		self.bus_bool = True
		# book
		self.bus_book_booked = self.metadata['bus']['book']['booked']
		self.bus_book_people = self.metadata['bus']['book']['time']
		# semi
		self.bus_semi_leaveAt = self.metadata['bus']['semi']['leaveAt']
		self.bus_semi_destination = self.metadata['bus']['semi']['destination']
		self.bus_semi_day = self.metadata['bus']['semi']['day']
		self.bus_semi_arriveBy = self.metadata['bus']['semi']['arriveBy']
		self.bus_semi_departure = self.metadata['bus']['semi']['departure']
		if self.bus_semi_leaveAt == '':
			self.bus_bool = False
		
	def __build_hospital_info(self):
		self.hospital_bool = True
		# book
		self.hospital_book_booked = self.metadata['hospital']['book']['booked']
		# semi
		self.hospital_semi_department = self.metadata['hospital']['semi']['department']
		if self.hospital_semi_department == '':
			self.hospital_bool = False 
		
	def __build_hotel_info(self):
		self.hotel_bool = True
		# book
		self.hotel_book_booked = self.metadata['hotel']['book']['booked']
		self.hotel_book_people = self.metadata['hotel']['book']['people']
		self.hotel_book_day = self.metadata['hotel']['book']['day']
		self.hotel_book_stay = self.metadata['hotel']['book']['stay']
		# semi
		self.hotel_semi_name = self.metadata['hotel']['semi']['name']
		self.hotel_semi_area = self.metadata['hotel']['semi']['area']
		self.hotel_semi_parking = self.metadata['hotel']['semi']['parking']
		self.hotel_semi_pricerange = self.metadata['hotel']['semi']['pricerange']
		self.hotel_semi_stars = self.metadata['hotel']['semi']['stars']
		self.hotel_semi_internet = self.metadata['hotel']['semi']['internet']
		self.hotel_semi_type = self.metadata['hotel']['semi']['type']
		if self.hotel_semi_name == '':
			self.hotel_bool = False
		
	def __build_attraction_info(self):
		self.attraction_bool = True
		# book
		self.attraction_book_booked = self.metadata['attraction']['book']['booked']
		# semi
		self.attraction_semi_type = self.metadata['attraction']['semi']['type']
		self.attraction_semi_name = self.metadata['attraction']['semi']['name']
		self.attraction_semi_area = self.metadata['attraction']['semi']['area']
		if self.attraction_semi_type == '':
			self.attraction_bool = False
			
	def __build_train_info(self):
		self.train_bool = True
		# book
		self.train_book_booked = self.metadata['train']['book']['booked']
		self.train_book_people = self.metadata['train']['book']['people']
		# semi
		self.train_semi_leaveAt = self.metadata['train']['semi']['leaveAt']
		self.train_semi_destination = self.metadata['train']['semi']['destination']
		self.train_semi_day = self.metadata['train']['semi']['day']
		self.train_semi_arriveBy = self.metadata['train']['semi']['arriveBy']
		self.train_semi_departure = self.metadata['train']['semi']['departure']
		if self.train_semi_leaveAt == '':
			self.train_bool = False
    