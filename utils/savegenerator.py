import json


class SaveGenerator:

    '''

        UNUSED BUT IT WILL COMEBACK LATER

        when game end and you get best score it will generate running.save

        -- encrypt function explain --
        1. add make best score into this string "score_is_{personal_best}".
        2. convert each character into ascii and convert to hexadecimal (aka. HEX).
        3. add delimeter with "," but convert it to ASCII and convert to octadecimal (aka. OCT). 

        -- decrypt function explain --
        1. split string into list by "0o54" (",") comma.
        2. convert each hexadecimal into ASCII integer and convert back to UTF-8.
        3. split text with "_" underscore and get last index of it.

    '''

    def encrypt(self, score: int):
        hashed = f'{oct(ord(","))}'.join(
            list(map(lambda x: hex(ord(x)), list(f"score_is_{score}"))))
        return hashed

    def decrypt(self, string_hashed: str):
        unhashed = ''.join([chr(int(i, 16))
                           for i in string_hashed.split("0o54")]).split("_")[-1]
        return int(unhashed)

    def save_file(self, best_score, username):
        with open("running.save", "w+") as f:

            self.scoreboard[username] = self.encrypt(best_score)

            json.dump(self.scoreboard, f, indent=2)

    def read_file(self, username):
        try:
            with open("running.save", "r+") as f:
                s = json.load(f)
            self.scoreboard = s
            return self.decrypt(s[username])
        except:
            self.scoreboard.setdefault(username, 0)
            return self.scoreboard[username]
