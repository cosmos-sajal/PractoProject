from flask import Flask
from flask import request, render_template, flash, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database import db_session, init_db
from models import Doctor, Clinic, Doctor_Clinic_Link, Experience, Speciality, Qualification
import os
from datetime import datetime
from form import ContactForm
from werkzeug import secure_filename
app = Flask(__name__)
UPLOAD_FOLDER = './images/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/doctor', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST':
         return form.name.data
    #    return redirect(url_for('index'))
    return render_template('doctor.html', form=form)

@app.route('/put_in_db', methods=['GET', 'POST'])
def put():
	#Doctor_Clinic_Link.query.delete()
	#Doctor.query.delete()
	#Clinic.query.delete()

	init_db()

	form = ContactForm(request.form)
	doc = Doctor(form.email.data, form.name.data, form.info.data)
	clinic = Clinic(form.clinic_name.data, form.first_addr.data, form.locality.data, form.city.data, form.pincode.data, form.country.data)
	db_session.add(doc)
	db_session.add(clinic)
	db_session.commit()
	link = Doctor_Clinic_Link(doc.email_id, clinic.id, form.start_day_booking.data, form.end_day_booking.data, form.fees.data, form.contact_num.data)
	db_session.add(link)
	db_session.commit()


	
	start_date_exp = datetime.strptime(form.start_date_exp()[-12:-2], "%Y-%m-%d")
	end_date_exp = datetime.strptime(form.end_date_exp()[-12:-2], "%Y-%m-%d")
	experience = Experience(doc.email_id, form.clinic_name.data, start_date_exp, end_date_exp)
	db_session.add(experience)
	db_session.commit()
	
	speciality = Speciality(doc.email_id, form.speciality.data)
	db_session.add(speciality)
	db_session.commit()

	start_date_edu = datetime.strptime(form.start_date_edu()[-12:-2], "%Y-%m-%d")
	end_date_edu = datetime.strptime(form.end_date_edu()[-12:-2], "%Y-%m-%d")
	qualification = Qualification(doc.email_id, form.college_name.data, start_date_edu, end_date_edu)
	db_session.add(qualification)
	db_session.commit()

	return 'Done!!!'

	'''
	form = ContactForm(request.form)
	if form.image.data:
		file = request.files['default.png']
		filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return form.image.data
     '''

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'jnaapti'
    app.run(host='0.0.0.0')