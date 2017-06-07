from flask import Flask, render_template
from os import environ
import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/hello")
def say_hi():
    return render_template('template.html', my_greeting="Hello World!",
                            current_time=datetime.datetime.now())

"""    return "Hello World!"
"""    
@app.route("/hello/<name>")
def hi_person(name):
    return render_template('template2.html', my_greeting="Hello! {}".format(name.title()),
                            my_string="Here's a picture of a kitten.  Awww...",
                            image_pl="http://placehold.it/350x150")


@app.route("/jedi")    
def nav_2_jedi():
    return render_template('template2a.html', my_greeting="Hi, padawan...",
                            my_string="Please type your first and last name after the URL in the address bar like this:",
                            linkurl="/jedi/obiwan/kenobi",
                            linktext="/jedi/obiwan/kenobi",
                            current_time=datetime.datetime.now())


@app.route("/jedi/<fname>/<lname>")
def hi_jedi(fname, lname):
    jedi_name = lname[:3] + fname[:2]
    return render_template('template2.html', my_greeting="Hello Jedi knight {}!".format(jedi_name.title()),
                            my_string="May the force be with you! \n I'm not your father, by the way.",
                            image_pl="https://s3-us-west-2.amazonaws.com/kyoshidaisy/catvader.jpg")


@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """Convert a datetime to a different format."""
    return value.strftime(format)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
