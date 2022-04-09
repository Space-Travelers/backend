
import json
from utils.db import conection_db

def quiz_game():
    conection = conection_db()
    game = []
    with conection.cursor() as cursor:
        cursor.execute("SELECT data FROM challenge WHERE challenge_type = 'quiz'")
        game = cursor.fetchall()
    conection.close()
    return json.loads((game[0][0]))


def def_game():
    conection = conection_db()
    game = []
    with conection.cursor() as cursor:
        cursor.execute("SELECT data FROM challenge WHERE challenge_type = 'definiciones'")
        game = cursor.fetchall()
    conection.close()
    return json.loads((game[0][0]))

