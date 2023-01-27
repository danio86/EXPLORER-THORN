import os
import json
from flask import Flask, render_template
""" Alternative zu direktem HTML
hier wird das Tepmlate in HTML gerändert """


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    """ die render_temp funktion ruft index.html auf.
    der file ist im ordner templates """


@app.route("/about")
def about():
    data = []
    with open('data/company.json', 'r') as json_data:
        """ python soll die daten aus json importieren
        der file ist in directory """
        data = json.load(json_data)
        """ set our empty 'data' list to equal the parsed JSON data """
    return render_template("about.html", page_title="About", company=data)


"""The angle brackets pass in data from the URL path, into view below
wenn auf der aubut seite auf einen link geklickt wird, wird member_name
hier eingefügt"""
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj
    return render_template("member.html", member=member)



@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
