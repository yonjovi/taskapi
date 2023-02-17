from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_username = "task_db_e1hh_user"
db_password = "723vlQ1dcsrQbVOHsgwiBItUGugXUMVB"
db_host = "dpg-cfno4hta499f28cskvlg-a.oregon-postgres.render.com"
db_name = "task_db_e1hh"

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_username}:{db_password}@{db_host}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
