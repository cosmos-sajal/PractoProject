from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, DateTime
from database import Base
from sqlalchemy.orm import relationship, backref

class Doctor(Base):
	__tablename__ = 'doctor'
	email_id = Column(String(50), primary_key = True)
	name = Column(String(50), nullable = False)
	info = Column(String(1000))
	image = Column(String(100))

	#relationships
	experiences = relationship('Experience', backref = 'Experience', lazy = 'dynamic')
	doc_clinic_links = relationship('Doctor_Clinic_Link', backref = 'doc_link', lazy = 'dynamic')
	specialities = relationship('Speciality', backref = 'Speciality', lazy = 'dynamic')
	qualifications = relationship('Qualification', backref = 'Qualification', lazy = 'dynamic')

	def __init__(self, email_id, name, info = None, image = None):
		self.email_id = email_id
		self.name = name
		self.info = info
		self.image = image

	def __repr__(self):
		return '<Doctor name = %s, email = %s>'%(self.name, self.email_id)


class Clinic(Base):
	__tablename__ = 'clinic'
	id = Column(Integer, autoincrement = True , primary_key = True)
	name = Column(String(100), nullable = False)
	first_address = Column(String(50), nullable = False)
	locality = Column(String(50), nullable = False)
	city = Column(String(25), nullable = False)
	pin_code = Column(String(10), nullable = False)
	country = Column(String(15), nullable = False)

	#relationships
	doc_clinic_links = relationship('Doctor_Clinic_Link', backref = 'clinic_link', lazy = 'dynamic')

	def __init__(self, name, first_address, locality, city, pin_code, country):
		self.name = name
		self.first_address = first_address
		self.locality = locality
		self.city = city
		self.pin_code = pin_code
		self.country = country

	def __repr__(self):
		return '<Clinic id = %s name = %s, locality = %s, city = %s, pin_code = %s>'%(self.id, self.name, self.locality, self.city, self.pin_code)

class Doctor_Clinic_Link(Base):
	__tablename__ = 'doctorClinicLink'
	doctor_id = Column(String(50), ForeignKey(Doctor.email_id), primary_key = True)	
	clinic_id = Column(Integer, ForeignKey(Clinic.id), primary_key = True)
	start_day = Column(String(10), nullable = False, primary_key = True)
	end_day = Column(String(10), nullable = False, primary_key = True)
	#start_time = Column(DateTime, nullable = False, primary_key = True)
	#end_time = Column(DateTime, nullable = False)
	fees = Column(Integer, nullable = False)
	contact_num = Column(String(15), nullable = False)
	#services = Column(String(500), nullable = False)

	def __init__(self, doctor_id, clinic_id, start_day, end_day, fees, contact_num): #, start_time = None,  end_time = None, services = None):
		self.doctor_id = doctor_id
		self.clinic_id = clinic_id
		self.start_day = start_day
		self.end_day = end_day
		#self.start_time = start_time
		#self.end_time = end_time
		self.fees = fees
		self.contact_num = contact_num
		#self.services = services

	def __repr__(self):
		return '<DoctorClinicLink doctor_id = %s, clinic_id = %s, fees = %s, contact_num = %s>'%(self.doctor_id, self.clinic_id, self.fees, self.contact_num)	

class Experience(Base):
	__tablename__ = 'experience'
	doctor_id = Column(String(50), ForeignKey(Doctor.email_id), primary_key = True)
	clinic_name = Column(String(50), nullable = False)
	start_date = Column(DateTime, nullable = False , primary_key = True)
	end_date = Column(DateTime)

	def __init__(self, doctor_id, clinic_name, start_date, end_date):
		self.doctor_id = doctor_id
		self.clinic_name = clinic_name
		self.start_date = start_date
		self.end_date = end_date

	def __repr__(self):
		return '<Experience doctor_id = %s, clinic_name = %s>'%(self.doctor_id, self.clinic_name)	

class Speciality(Base):
	__tablename__ = 'speciality'
	doctor_id = Column(String(50), ForeignKey(Doctor.email_id), primary_key = True)	
	speciality_info = Column(String(50), nullable = False, primary_key = True)

	def __init__(self, doctor_id, speciality_info):
		self.doctor_id = doctor_id
		self.speciality_info = speciality_info

	def __repr__(self):
		return '<Speciality doctor_id = %s, speciality_info = %s'%(self.doctor_id, self.speciality_info)

class Qualification(Base):
	__tablename__ = 'qualification'
	doctor_id = Column(String(50), ForeignKey(Doctor.email_id), primary_key = True)	
	college = Column(String(50), nullable = False)
	start_date = Column(DateTime, nullable = False, primary_key = True, autoincrement = False)
	end_date = Column(DateTime, nullable = False)

	def __init__(self, doctor_id, college, start_date, end_date):
		self.doctor_id = doctor_id
		self.college = college
		self.start_date = start_date
		self.end_date = end_date

	def __repr__():
		return '<Qualification doctor_id = %s, college'
