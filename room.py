import random

class Dojo(object):
	living_spaces = {}
	offices = {}
	staff = {}
	fellows = {}

	def create_room(self, room_type, room_name):
		all_rooms = [Dojo.offices.keys(), Dojo.living_spaces.keys()]
		if(room_name.lower() in (key.lower() for room in all_rooms for key in room)):
			return "Room already exists"
		if room_type.lower() == "office":
			Dojo.offices[room_name] = Office(room_name)
		elif room_type.lower() == "living space":
			Dojo.living_spaces[room_name] = LivingSpace(room_name)
		else:
			return "Please choose either office or living space"

		return "You have created {} successfully".format(room_name)

	
	def add_person(self, name, employment_type, wants_accommodation = "N"):
		if employment_type.lower() == "fellow":
			Dojo.fellows[name] = Fellow(name, wants_accommodation)
		elif employment_type.lower() == "staff":
			if wants_accommodation == "Y":
				return "Staff can't be offered accomodation"
			Dojo.staff[name] = Staff(name)
		else:
			return "Please choose either staff or fellow"
		if wants_accommodation == "Y":
			print("{} has been allocated {}".format(name, random.choice(Dojo.living_spaces.keys())))
		print("{} has been allocated {}".format(name, random.choice(Dojo.offices.keys())))

		return "You have created {} successfully".format(name)
		
class Room(Dojo):
	
	def __init__(self, name):
		self.max_num = 4
		self.current_occupants = []
		self.name = name

class Office(Room):
	def __init__(self, name):
		super(Room, self).__init__()
		self.max_num = 6


class LivingSpace(Room):
	def __init__(self, name):
		super(Room, self).__init__()
	

class Person(object):
	def __init__(self, name):
		self.name = name

class Staff(Person):
	def __init__(self, name):
		super(Person, self).__init__()

class Fellow(Person):
	def __init__(self, name, wants_accommodation):
		super(Person, self).__init__()
		self.wants_accommodation = wants_accommodation

y = Dojo()
p = Room("yeaah")
print(y.create_room("office", p.name))
y.create_room("office", "naaah")
y.create_room("living space", "pliz")
z = Person("meeee")
print(y.add_person(z.name, "fellow", "Y"))
