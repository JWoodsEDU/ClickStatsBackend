import pymongo
from config import *
from pymongo import MongoClient
import matplotlib.pyplot as plt
from datetime import datetime

cluster = MongoClient(MONGOCODE)  
db = cluster["ClickStats"]
collection = db["GeneralUpdated1.2"]
all_years = []
all_scores = []
  

class GeneralCorpsDataManager:
    def __init__(self, collection):
        self.collection = collection
    def getAllScores(self, corps, year):
        print("[GeneralCorpsDataManager] Getting all scores for: " + corps)
        start = datetime.datetime(year, 6, 1)
        end = datetime.datetime(year, 9, 1)
        scores = self.collection.find({"Corps": corps}, {"Date": {'$lt': end, '$gte': start}}).sort("Date")
        for score in scores:
            all_scores.append(score["Score"])
            all_years.append(score["Date"])
        plt.plot(all_years, all_scores, label = corps)
        all_scores.clear()
        all_years.clear()

corps_manager = GeneralCorpsDataManager(collection)
corps = ["Bluecoats", "Blue Devils", "Carolina Crown", "The Cavaliers", "Phantom Regiment", "Santa Clara Vanguard", "Blue Knights", "Pacific Crest", "Mandarins",
"Boston Crusaders"]
for corp in corps:
    corps_manager.getAllScores(corp)

plt.title('DCI Scores By Year')
plt.xlabel('Year')
plt.legend(loc="upper left")
plt.ylabel('Score')
plt.show()