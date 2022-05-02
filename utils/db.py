import os
import pymysql
import sshtunnel

from dotenv import load_dotenv
load_dotenv()

server = sshtunnel.SSHTunnelForwarder(( os.getenv('PORT'),22),
                                    ssh_username=os.getenv('SSH_USERNAME'),
                                    ssh_pkey= os.getenv('SSH_PKEY'),
                                    remote_bind_address=('localhost', 3306),
                                    )  
server.start()



def conection_db(server):
    return pymysql.connect(host='localhost',
                                user='root',
                                password='5aLmbzTc4CSFyeH9uf',
                                db='spacetravelers',
                                port=server.local_bind_port)





