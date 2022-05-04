import os
import pymysql
import sshtunnel


server = sshtunnel.SSHTunnelForwarder(( '20.70.0.41', 22),
                                    ssh_username="nasagameespol287",
                                    ssh_pkey= 'nasagameespol287.pem',
                                    remote_bind_address=('localhost', 3306),
                                    )  
server.start()



def conection_db(server):
    return pymysql.connect(host='localhost',
                                user='root',
                                password='5aLmbzTc4CSFyeH9uf',
                                db='spacetravelers',
                                port=server.local_bind_port)





