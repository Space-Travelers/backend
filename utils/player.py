import json
from utils.db import conection_db
from models.player import PlayerRegister, PlayerLogin



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


