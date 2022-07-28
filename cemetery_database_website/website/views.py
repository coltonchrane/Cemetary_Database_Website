#Where we activate events based on URL and reuqest type and talk to our HTML page (Jinja)
import csv
from io import BytesIO
import os
from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file, send_from_directory
from flask_login import login_required, current_user
from sqlalchemy import null, nulls_first, true
import sqlite3 as sql
from .models import Directory
from . import db
import flask_excel as excel



views = Blueprint('views', __name__)

#Home screen
#Returns SELECT * FROM Directory table to the grave object using db model
#env used to compare empty strings in Jinja
#Search
#Tries to load home page with user and grave site data
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    graves=Directory.query.all()
    env=""
    if request.method == 'POST':
        last_name = request.form['last_name']
        return redirect(url_for("views.search_results", user=current_user, query = last_name))
    return render_template("home.html", user=current_user, items=graves,env=env)

#Edit Grave site
#data pulled from db using db model and id
#data taken from HTML when updating grave
#then sent to grave object built to handle this data
#update db 
@views.route('/<int:id>/update/', methods=['GET', 'POST'])
def update(id):
    grave = Directory.query.get_or_404(id)

    if request.method == 'POST':
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        date_of_birth = request.form['date_of_birth']
        date_of_death = request.form['date_of_death']
        reserved = bool(request.form.get('reserved', 0))
        phone_number = request.form['phone_number']
        address = request.form['address']
        notes = request.form['notes']

        grave.first_name = first_name
        grave.middle_name = middle_name
        grave.last_name = last_name
        grave.date_of_birth = date_of_birth
        grave.date_of_death = date_of_death
        grave.reserved = reserved
        grave.phone_number = phone_number
        grave.address = address
        grave.notes = notes
 
        db.session.add(grave)
        db.session.commit()
        flash('Grave Updated', category='success')
        return redirect(url_for('views.home')) 
    return render_template("update.html", user=current_user, item = grave)

#Sends search query as sql command
#sends data back to site to publish
@views.route('/search-results/<query>')
def search_results(query):
    grave = Directory.query.filter_by(last_name=query).all()
    return render_template("search-results.html", user=current_user, items = grave)

#Exports Directory database for reporting. Needs formatting to make formal report
@views.route("/export", methods=['GET'])
def export():
    #Need to format report better. List of sections that writes seperate books into a csv file?
    conn=sql.connect('website\database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT section|| '-' ||lot AS Location , first_name || ' ' || middle_name || ' ' || last_name AS Name, date_of_birth|| ' ~ ' ||date_of_death AS Date, phone_number AS [Phone Number], address AS Address FROM Directory;")
    with open("Cemetary-roster.csv", "w",encoding="utf-8",newline='') as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=",")
      csv_writer.writerow([i[0] for i in cursor.description])
      csv_writer.writerows(cursor)
    dirpath = os.getcwd() + "/Cemetary-roster.csv"
    return send_file(dirpath, as_attachment= True)
