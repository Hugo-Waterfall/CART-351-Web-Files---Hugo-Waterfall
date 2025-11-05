#STEP 1:

#importing and setting up the python document
from flask import Flask,render_template,request, jsonify
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads' # Or os.path.join(app.instance_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit

# the default route
@app.route("/")
def index():
      return render_template("index.html")

#STEP 2:
#*************************************************
#Task: CAPTURE & POST & FETCH & SAVE
@app.route("/t2")
def t2():
     return render_template("t2.html")

#STEP 2.5:
@app.route("/postDataFetch",methods = ['POST'])
def postDataFetch():

      #recieving data from fetch request
      data = request.get_json() 
      print("Recieved data: ", data)
     
     #parsing data from the request json object
      color = data.get("color")
      print ("color recieved:", color)

      #file path for reading and writing from files
      file_path = os.path.join("files", "data.txt")

      #because we want to identify if the picked color already exists in the server, we loop through the server file and count
      count = 0
      with open(file_path, "r") as f:
          for line in f:
               
               text = line.strip()

               if color in text:
                    count +=1

      #if that exact color was picked, then notify user. If not, notify user
      if (count < 1):
            message = "No other user has picked this colour!"

      else:
           message = f"This colour has been picked {count} time(s)!"

      #finally, after looping through all the exisitng colors, we can write this one to the file
      with open(file_path, "a") as f:
          f.write(color + "\n")

      app.logger.info(request.form)

      #returning the data
      return jsonify({"data_received":"yes", "color":color, "message":message})

#*************************************************
#run
app.run(debug=True)