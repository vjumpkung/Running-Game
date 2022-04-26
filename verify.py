import requests
import bcrypt
from typing import ByteString
from utils.settings import Settings

URL = Settings().URL

class Authenticate:
    
    def hash_password(self, password: str) -> ByteString :
            byte_password = password.encode('utf-8')
            salt = bcrypt.gensalt()
            return bcrypt.hashpw(byte_password, salt)

    def register(self, user:str, password:str) -> bool :
    
        
        hash_passwords = self.hash_password(password)
        str_passwords = hash_passwords.decode('utf-8')
        r = requests.post(url=f"{URL}/register?username={user}&password={str_passwords}")
        if r.status_code == 400:
            return False
        else:
            return True

    def login(self, user:str, password:str) -> bool :
        r = requests.get(url=f"{URL}/?username={user}")
        if r.status_code == 404:
            return False
        byte_password = password.encode("utf-8")
        return bcrypt.checkpw(byte_password, r.json()[user].encode("utf-8"))
