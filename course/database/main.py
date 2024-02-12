# Connexion à MySQL
from sqlalchemy import create_engine, text
connection_str = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/myblog'
engine = create_engine(connection_str, echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM users"))

for row in result.mappings():
    print("Users:" , row["username"])
