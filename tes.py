from utils.db import conection_db
import json

def challenge_type(challenge):
    conection = conection_db()
    game = []
    with conection.cursor() as cursor:
        cursor.execute(f"SELECT data FROM challenge WHERE challenge_type = '{challenge}'")
        game = cursor.fetchall()
    conection.close()
    return json.loads((game[0][0]))






