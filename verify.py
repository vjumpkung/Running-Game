import bcrypt
from typing import ByteString
from utils.settings import Settings
import pymongo

st = Settings()
URL = st.URL
USERNAME = st.USERNAME
PASSWORD = st.PASSWORD


client = pymongo.MongoClient(URL, username = USERNAME, password = PASSWORD)
db = client["running_game"]
col = db["usernames"]


class Authenticate:

    def hash_password(self, password: str) -> ByteString:
        byte_password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(byte_password, salt)

    def register(self, user: str, password: str) -> bool:

        hash_passwords = self.hash_password(password)
        str_passwords = hash_passwords.decode('utf-8')

        # query
        q = list(col.find({'username': user}))
        if not len(q) == 0:
            return False

        # insert
        dic = {'username': user, 'password': str_passwords, 'score': 0}
        col.insert_one(dic)

        return True

    def login(self, user: str, password: str) -> bool:
        # query
        q = list(col.find({'username': user}))
        if len(q) == 0:
            return False
        byte_password = password.encode("utf-8")
        return bcrypt.checkpw(byte_password, q[0]['password'].encode("utf-8"))
