from flask import Flask, render_template, send_from_directory, request, redirect
import os
import datetime
import csv

app = Flask(__name__)
#print(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def get_date():
    date_today = datetime.datetime.now()
    return date_today

def write_to_file(data):
    with open('text.txt', 'a') as database:
        email =data['email']
        subject = data['subject']
        message = data['message']
        date_and_time = get_date()
        file = database.write(f'\n{date_and_time}\nEmail: {email}\nSubject: {subject}\nMessage: {message}\n')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email =data['email']
        subject = data['subject']
        message = data['message']
        date_and_time = get_date()
        csv_writer = csv.writer(database2, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([date_and_time, email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #print(data)
            write_to_csv(data=data)
            return redirect ('Thankyou.html')
        except:
            return 'did not save to database'
    else:
        return'Something went wrong'

    
    
              
              


