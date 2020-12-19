from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy is essentially a flask extension that simplifies database handling.
# Fx. it handles setting up connection, the cursor, committing and closing.
#     Even the query creation to some extent. (Look at comments in the models)
# note: The models inherits the db.Models. this tells SQLAlchemy that this is
#       A model used for handling database insertion, extraction etc.
#       __tablename__ = <name_of_table>
#       followed by the table columns.
db = SQLAlchemy()
