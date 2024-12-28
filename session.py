from sqlalchemy import create_engine, exc, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
#import psycopg2

#creating session

create_flag = False

db_user = "postgres"
db_password = "1234"
db_host = "localhost"
db_port = "5432"
db_name = "db_proj"
owner_user = "postgres"
