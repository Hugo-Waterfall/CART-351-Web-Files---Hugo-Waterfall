from flask import Flask,render_template,request
import os
app = Flask(__name__)

#STEP 1:

# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************

#Task: Variables and JinJa Templates
@app.route("/t1")
def t1():
      the_topic = "donuts"
      number_of_donuts = 28
      donut_data= {
      "flavours":["Regular", "Chocolate", "Blueberry", "Devil's Food"],
      "toppings": ["None","Glazed","Sugar","Powdered Sugar",
      "Chocolate with Sprinkles","Chocolate","Maple"]
      }

      donut_flavor_count = len(donut_data["flavours"])
      donut_toppings_count = len(donut_data["toppings"])

            
      icecream_flavors = ["Vanilla","Raspberry","Cherry", "Lemon"]

      icecream_flavors_count = len(icecream_flavors)

      #Since I am using url_for() in html, I do not need the full path name, just the image file name. 
      donut_pink_path = "donut_pink.png"
      donut_a_path = "donut_a.png"
      donut_b_path = "donut_c.png"
      donut_c_path = "donut_e.png"

      #STEP 2.3
      #Here, I pass all the previous variables as parameters to be used by the html template, using JINJA
      return render_template("t1.html", the_topic=the_topic, number_of_donuts=number_of_donuts, donut_data=donut_data, icecream_flavors=icecream_flavors, donut_pink_path=donut_pink_path, donut_a_path=donut_a_path, donut_b_path=donut_b_path, donut_c_path=donut_c_path, donut_flavor_count=donut_flavor_count, donut_toppings_count=donut_toppings_count, icecream_flavors_count=icecream_flavors_count)

#*************************************************

#Task: HTML Form get & Data 
@app.route("/t2")
def t2():
      return render_template("t2.html")

# STEP 3.4 (b)
@app.route("/thank_you_t2")
def thank_you_t2():
      app.logger.info(request.args)

      fav_flavor=request.args["fav_flavor"]
      lfav_flavor=request.args["lfav_flavor"]
      d_date=request.args["d_date"]

      # STEP 3.5
      # Combining data into one long string
      returnString = f"Your data has been processed. We know your favorite flavor is {fav_flavor}, your least favorite flavor is {lfav_flavor}, and the date of your discount is {d_date}."
      returnStringAlt = ""
              
      # Changing the string to have asterisks in place of vowels
      returnStringAlt2 = ""

      for char in returnString:

            if (char in "aeiou"):
                  returnStringAlt += "*"
            
            else:
                  returnStringAlt += char

      for char in returnString:

            if (char != " "):
                  returnStringAlt2 += "*"
            
            else:
                  returnStringAlt2 += char

      # STEP 3.6
      #Passing the strings to the template
      return render_template("thank_you_t2.html", returnString=returnString, returnStringAlt=returnStringAlt, returnStringAlt2=returnStringAlt2, lfav_flavor=lfav_flavor)

#*************************************************

#run
app.run(debug=True)