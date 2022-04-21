
from utils.db import conection_db
from models.player import PlayerRegister, PlayerLogin

def register_player(player:PlayerRegister):
    conection = conection_db()
    try:
        with conection.cursor() as cursor:
            cursor.execute(f"insert into player(email, password, name, last_name, age, gender, level, school, avatar) values ('{player.email}',md5('{player.password}'),'{player.name}','{player.last_name}','{player.age}','{player.gender}','{player.level}','{player.school}','{player.avatar}')")
        conection.commit()
        conection.close()

        return True
    except:
        print("An exception occurred")
        return False

def authentication_player(player:PlayerLogin):
    autentication = 0
    conection = conection_db()
    with conection.cursor() as cursor:
        cursor.execute(f"set @authentication = 2; ")
        cursor.execute(f"call playerAuthentication('{player.email}', md5('{player.password}'), @authentication);")
        cursor.execute("select @authentication;")
        autentication = cursor.fetchall()
        conection.close()
        return autentication[0][0]
 

