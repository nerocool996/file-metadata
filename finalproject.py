import os,sys
from flask import Flask, render_template, request, redirect, url_for, jsonify,make_response
from werkzeug.utils import secure_filename
from datetime import date,timedelta
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from sqlalchemy import create_engine,desc,func
from sqlalchemy.orm import sessionmaker
from urlparse import urlparse
from random import random

@app.route('/',methods = ['GET','POST'])
def mainpage():
	if request.method == 'POST':
		Mfile = request.files['file']
		if Mfile.filename == '':
            		return jsonify({"Error":'No selected file'})
            	filename = secure_filename(Mfile.filename)
		return jsonify({"size":str(request.content_length-192)+" bytes"})	
	else:
		return render_template('main.html')        


	
##if __name__ == '__main__':
app.secret_key = 'super_secret_key'
app.debug = True
##	app.run(host = '0.0.0.0', port = 5000)
