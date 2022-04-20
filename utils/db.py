import pymysql

def conection_db():
    return pymysql.connect(host='mysql-76280-0.cloudclusters.net',
                                user='admin',
                                password='npqSNlv1',
                                db='spaceTravelers',
                                port= 19065)