# # from flask import Flask, render_template
# #from datetime import datetime

# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Get the current date and time
#     current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     # Pass the current date to the HTML template
#     return render_template('index.html', current_date=current_date)

# if __name__ == '__main__':
#     app.run(debug=True)

import subprocess
from flask import Flask, render_template
from datetime import datetime
#import 
app = Flask(__name__)
def date():
    # re1 = 'date +"%Y-%m-%d %H:%M:%p"'
    # ou1 = subprocess.run(re1, shell=True, capture_output=True, text=True)
    #re = 'date -u +"%Y-%m-%d %I:%M %p" | xargs -I {} date -d "{} -6 hours"'
    re = 'date -u -d "-6 hours" +"%Y-%m-%d %I:%M %p"'
    #re = 'date -u -d "-6 hours" +"%Y-%m-%d %I:%M %p"'
    ou = subprocess.run(re, shell=True, capture_output=True, text=True)
    # print (ou.stdout.strip()) 
    # print ("thois is actual",ou1.stdout.strip())
    #print(current_date)
    return render_template('index.html', current_date=ou.stdout.strip())
if __name__ == '__main__':
    app.run(debug=True, port=8080)
