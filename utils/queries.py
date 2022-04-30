from typing import List
import pymongo
from datetime import datetime
from utils.settings import Settings

# loading MongoDB url, username and password
st = Settings()
URL = st.URL
USERNAME = st.USERNAME
PASSWORD = st.PASSWORD

# connect to MongoDB server
client = pymongo.MongoClient(URL, username = USERNAME, password = PASSWORD)
db = client["running_game"]
col = db["usernames"]

def get_score(username:str):
    
    # query username and return score only
    
    q = list(col.find({'username':username}))
    return q[0]['score']
    
def update_score(username:str, score:int):
    
    # query username and update new score
    
    argss = {'username':username}
    n = {"$set" : {'score': score}}
    print(f"{datetime.now()} : {username} has updated new record.")
    col.update_one(argss,n)
    
def get_top_five() -> List:
    
    #query top five in database.
    
    return list(col.find({}, {"username": 1, "score": 1, '_id': 0}).sort('score',-1).limit(5))
        
class MaximumScore:
    
    # manage maximum score and save it
    
    def update_score(self, newscore:int, username:str):
        
        # save best score in local and db
        
        if newscore > self.get_max_score(username):
            
            # sg.save_file(newscore, username) unused but it will return after i made offline mode
            
            update_score(username, newscore)
            self.personal_best = newscore
    def get_max_score(self, username:str):
        
        # get max score 
        
        return get_score(username) 