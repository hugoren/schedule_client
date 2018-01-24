import os

env = os.getenv('ENV')

if env == 'test':
    HOST = '192.168.0.108'
    PORT = 20000
    TOKEN = 'b0350c8c75ddcd99738df4c9346bec48dc9c4914'


elif env == 'prod':
    HOST = '192.168.0.103'
    PORT = 9200
    TOKEN = 'b0350c8c75ddcd99738df4c9346bec48dc9c4914'

else:
    SERVER_ADD = '127.0.0.1'
    PUB_PORT = 14505
    MSG_CLIENT_PORT = 14506
    HEART_SERVER_CONN_IN = 14508
    HEART_SERVER_CONN_OUT = 14509