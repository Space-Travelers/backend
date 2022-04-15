import json
from utils.db import conection_db

def register_player(player:PlayerRegister):
    conection = conection_db()
    try:
        with conection.cursor() as cursor:
            cursor.execute(f"insert into player(email, password, name, last_name, age, gender, level, school) values ({player.email},{player.password},{player.name},{player.last_name},{player.age},{player.gender},{player.level},{player.school})")
        conection.close()
        return True
    except:
        print("An exception occurred")
        return False

def authentication_player(player:PlayerLogin):
    autentication = 0
    conection = conection_db()
    try:
        with conection.cursor() as cursor:
            cursor.execute(f"set @si = 2;
                            call playerAuthentication("frego202@gmail.com",md5("12345"), @si);
                            select @si;")
            


    except:
