import pymysql

def conection_db():
    return pymysql.connect(host='mysql-75127-0.cloudclusters.net',
                                user='admin',
                                password='WWc5GKaK',
                                db='spaceTravelers',
                                port= 12977)
