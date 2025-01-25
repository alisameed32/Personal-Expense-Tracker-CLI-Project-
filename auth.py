import hashlib
import json
import re
from interface import userInterface

class User_Authentication:

    def login(self, email, password):
        if self.__validate(email):
            try:
                with open('data/users.json', 'r') as file:
                    data = json.load(file)
                    hash_pass = self.__hash(password)
                    for db_data in data:
                        if  db_data["email"] == email and db_data["password"] == hash_pass:
                            filename = "data/"+email+".json"
                            obj = userInterface(filename)
                        else:
                            print("Invalid Credentials")    
                    
            except:
                raise FileNotFoundError
        else:
            print("Please enter valid email")        
        


    def signup(self, name, username, email, password):
        if self.__validate(email):
            hash_pass = self.__hash(password)
            new_data = {
                "name": name,
                "email": email,
                "username": username,
                "password": hash_pass
            }
            data = []
            try:
                with open('data/users.json', 'r') as file:
                    data = json.load(file)
            except:
                data = []


            if self.__isUserExist(data, username, email):
                data.append(new_data)  

                with open('data/users.json', 'w') as file:
                    json.dump(data, file, indent=4)
        else:
            print("Please enter valid email")

           

    def __isUserExist(self,data, username, email):
        if not data:
            return True
        else:
            for db_data in data:
                if db_data["email"] == email or db_data["username"] == username:
                    print("Username or Email Already Exist")
                    return False
                
        return True        
     


    def __hash(self, password):
        h = hashlib.new("SHA256")
        h.update(password.encode())
        db_pass = h.hexdigest()
        return db_pass
    

    def __validate(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            return True
        return False
