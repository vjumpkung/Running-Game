import pymongo
from datetime import datetime
from utils.settings import Settings

st = Settings()
URL = st.URL
USERNAME = st.USERNAME
PASSWORD = st.PASSWORD


client = pymongo.MongoClient(URL, username = USERNAME, password = PASSWORD)
db = client["running_game"]
col = db["usernames"]

def get_score(username:str):
    # query
    q = list(col.find({'username':username}))
    if len(q) == 0:
        return False
    else:
        print(f"{datetime.now()} : {username} get his/her best score.")
        return q[0]['score']
    
def update_score(username:str, score:int):
    # query
    argss = {'username':username}
    q = list(col.find({'username':username}))
    if len(q) == 0:
        return False
    n = {"$set" : {'score': score}}
    print(f"{datetime.now()} : {username} has updated new record.")
    col.update_one(argss,n)
    
# manage maximum score and save it
class MaximumScore:
        
    def update_score(self, newscore:int, username:str):
        # save best score in local and db
        if newscore > self.get_max_score(username):
            # sg.save_file(newscore, username) unused but it will return after i made offline mode
            update_score(username, newscore)
            self.personal_best = newscore
    def get_max_score(self, username:str):
        # get max score
        return get_score(username) # online only