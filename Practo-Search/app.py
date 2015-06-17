from flask import Flask
from flask import render_template
from databaseApp.database import db_session, init_db
from databaseApp.models import Doctor, Clinic, Doctor_Clinic_Link, Experience, Speciality, Qualification
import datetime
from jinja2 import Environment, PackageLoader

app = Flask(__name__)

@app.route('/search')
def search():
	return render_template('search.html')

@app.route('/search/<address>/<speciality>', methods=['GET','POST'])
def getValues(address,speciality):
	address = address.replace("%20"," ")

	init_db()
	doctor_ids = []
	clinic_ids = []
	
	for speciality in db_session.query(Speciality).filter(Speciality.speciality_info == speciality):
		doctor_ids.append(speciality.doctor_id)
	
	for clinic in db_session.query(Clinic).filter(Clinic.locality == address):
		clinic_ids.append(clinic.id)
	
	output_doc_ids = []
	output_clinic_ids = []
	output_doc_names = []
	output_doc_speciality = []
	output_doc_qualifications = []
	output_clinic_names = []
	output_locations = []

	for doc_id in doctor_ids:
		links = db_session.query(Doctor_Clinic_Link).filter(Doctor_Clinic_Link.doctor_id == doc_id)
		for clinic_id in clinic_ids:
			for link in links:
				if(link.clinic_id == clinic_id):
					output_doc_ids.append(link.doctor_id)
					output_clinic_ids.append(clinic_id)
	
	for doc_id in output_doc_ids:
		docs = db_session.query(Doctor).filter(Doctor.email_id==doc_id)
		qualifications = db_session.query(Qualification).filter(Qualification.doctor_id==doc_id)
		specialities = db_session.query(Speciality).filter(Speciality.doctor_id==doc_id)
		for doc in docs:
			output_doc_names.append(doc.name)
		for sp in specialities:
			output_doc_speciality.append(sp.speciality_info)
		for qualification in qualifications:
			output_doc_qualifications.append(qualification.college)
	
	for clinic_id in output_clinic_ids:
		clinics = db_session.query(Clinic).filter(Clinic.id == clinic_id)
		for clinic in clinics:
			output_clinic_names.append(clinic.name)
			output_locations.append(clinic.locality)
	
	output = []
	for i in range(0,len(output_doc_ids)):
		info = {}
		info['name'] = output_doc_names[i]
		info['email'] = output_doc_ids[i]
		info['clinic'] = output_clinic_names[i]
		info['qualifications'] = output_doc_qualifications[i]
		info['speciality'] = output_doc_speciality[i]
		output.append(info)

	speciality = output_doc_speciality[0]	
	return render_template('results.html',job=speciality, address= address, infos=output, localities=output_locations)

if __name__ == '__main__':
	app.run(host='0.0.0.0')