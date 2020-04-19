## About Docker : 
# use docker build -t mywebsite to build the image
# Then docker run -p hostport:containerport mywebsite 
# this link https://pythonspeed.com/articles/docker-connection-refused/ explains why the image can't connect !
# Needs to tell Flask to listen to all incoming connexion, otherwise it listens to localhost only ! set host=0.0.0.0 in the app.run command. 
# pour monter le dossier utiliser -v hostfolder:containerfolder : docker run -rm -p 5000:5000 -v C:\Workspaces\Python\Mega_course\first_program\first_website:/usr/src/app mywebsite
# Flask has dynamic loading so all is nice.

from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    #return "Vous en savez desormais plus."
    return render_template("about.html")

if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        debug=True)
