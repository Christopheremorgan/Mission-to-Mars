from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# index / home page route
@app.route("/")
def index():
   # ??????????  need to fix line below ?????? does it need to match config line?
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# route that calls scraping function and data from Mongo
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# run prompt for flask
if __name__ == "__main__":
   app.run(debug=True)