from databaseApp.database import db_session, init_db
from databaseApp.models import Doctor, Clinic, Doctor_Clinic_Link, Experience, Speciality, Qualification
import datetime
from jinja2 import Environment, PackageLoader

init_db()


#Doctor_Clinic_Link.query.delete()
#Speciality.query.delete()
#Experience.query.delete()
#Qualification.query.delete()
#Doctor.query.delete()
#Clinic.query.delete()
doc = Doctor('doctor5@Doctor.com', 'Neel5')
clinic = Clinic('Raj Dental Clinic', '33-4', 'Koramangala', 'Bangalore', '560078', 'India')
db_session.add(doc)
db_session.add(clinic)
db_session.commit()
link = Doctor_Clinic_Link(doc.email_id, clinic.id, 'Mon', 'Fri', '4', '7', '400', '893491281', 'random services')
start_date = datetime.datetime.strptime('2012-12-04','%Y-%m-%d');
end_date = datetime.datetime.strptime('2014-12-04','%Y-%m-%d');
experience = Experience(doc.email_id, 'Some old Clinic', start_date, end_date)
speciality = Speciality(doc.email_id, "Dentist")
qualification = Qualification(doc.email_id, 'college5', start_date, end_date)
db_session.add(link)
db_session.add(experience)
db_session.add(speciality)
db_session.add(qualification)
db_session.commit()



