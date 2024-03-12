from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        ownerName = request.form['ownerName']
        citizenship = request.form['citizenship']
        phoneNumber = request.form['phoneNumber']
        email = request.form['email']
        businessAddress = request.form['businessAddress']
        province = request.form['province']
        businessType = request.form['businessType']
        companyName = request.form['companyName']
        tinNumber = request.form['tinNumber']
        registrationDate = request.form['registrationDate']
        businessProvince = request.form['businessProvince']
        productCategory = request.form['productCategory']
        weight = request.form['weight']
        unitOfMeasurement = request.form['unitOfMeasurement']
        quantity = request.form['quantity']
        description = request.form['description']

        # Compose the email message
        subject = 'New Form Submission'
        body = f'''Citizenship: {citizenship}
Business Owner Name: {ownerName}
Phone Number: {phoneNumber}
Email: {email}
Business Address: {businessAddress}
Province: {province}
Business Type: {businessType}
Company Name: {companyName}
TIN Number: {tinNumber}
Registration Date: {registrationDate}
Business Province: {businessProvince}
Product Category: {productCategory}
Weight: {weight}
Unit of Measurement: {unitOfMeasurement}
Quantity: {quantity}
Description: {description}'''
        message = f'Subject: {subject}\n\n{body}'

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'i.shema@alustudent.com'
        receiver_email = 'shemaivan27@gmail.com'
        password = 'c44R3ksN7uW.VZr'

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

        return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
