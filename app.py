from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars
from splinter import Browser
import pymongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
# mongo = PyMongo(app)
# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

@app.route("/")
def index():
    #listings = mongo.db.listings.find_one()
    # featured_img_url = ""
    # news = mission_to_mars.latest_news_headline()
    # para = mission_to_mars.latest_news_para()
    # featured_img_url = mission_to_mars.featured_image()
    # mars_weather = mission_to_mars.current_weather()
    # mars_facts = mission_to_mars.mars_facts()
    # hemispheres = mission_to_mars.hemispheres(   )

    # return render_template("index.html", news = news, para = para, featured_img_url = featured_img_url, mars_weather = mars_weather,
    #     mars_facts = mars_facts, hemispheres = hemispheres )

    mars = db.mars_table.find_one()
    return render_template("index.html", mars = mars)


@app.route("/scrape")
def scraper():
    # mars = mongo.db.mars_table
    mission_to_mars.scrape()
    # mars.update({}, mars_data, upsert=True)
    # db.mars_table.insert_many(
    # [
    #     {
    #         'news_t': 'news_t',
    #         'position': 'Point Guard'
    #     },
    #     {
    #         'player': 'Mark',
    #         'position': 'Center'
    #     }
    # ]
    # )
    
    return redirect("/", code=302)
    #return "success"

if __name__ == "__main__":
    app.run(debug=True)
