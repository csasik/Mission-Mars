from flask import Flask, render_template, redirect
#from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    #listings = mongo.db.listings.find_one()
    featured_img_url = ""
    news = mission_to_mars.latest_news_headline()
    para = mission_to_mars.latest_news_para()
    featured_img_url = mission_to_mars.featured_image()
    mars_weather = mission_to_mars.current_weather()
    mars_facts = mission_to_mars.mars_facts()
    hemispheres = mission_to_mars.hemispheres(

    )
    return render_template("index.html", news = news, para = para, featured_img_url = featured_img_url, mars_weather = mars_weather,
        mars_facts = mars_facts, hemispheres = hemispheres )



# @app.route("/scrape")
# def scraper():
#     listings = mongo.db.listings
#     listings_data = mission_to_mars.scrape()
#     listings.update({}, listings_data, upsert=True)
#     return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
