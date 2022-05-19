from utils.db import conection_db,server

def decrese_stats_players_in_db():
    
    conection = conection_db(server)
    with conection.cursor() as cursor:
        cursor.execute("UPDATE player SET avatar_health = avatar_health-1;")
        cursor.execute("UPDATE player SET avatar_nutrition = avatar_nutrition-1;")
        cursor.execute("UPDATE player SET avatar_physical_condition = avatar_physical_condition-1;")
        cursor.execute("UPDATE player SET avatar_happiness = avatar_happiness-1;")
    conection.commit()
    conection.close()