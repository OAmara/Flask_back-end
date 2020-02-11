### all models

## modules
# peewee (similar to mongoose)
# import *, imports everything! including:
	# SqliteDatabase (adapter)
	# Model -- Model() class
from peewee import *
import datetime


## change to psql later for deployment
# portable data for development
# value: Database connection string
DATABASE = SqliteDatabase('accounts.sqlite')


# helpful: http://docs.peewee-orm.com/en/latest/peewee/models.html#
## Defining Account model
class Account(Model):
	institution = CharField() # associated bank
	name = CharField()
	balance = IntegerField()
	created_at = DataTimeField(default=datetime.datetime.now)

	# specialized constructor to specify to class how to connect to DB
	class META:
		database = DATABASE





# method called in app.py to set-up DBs connection
def initialize():
	DATABASE.connect()


DATABASE.create_tables([Account], safe=True)
print('Connected to DB and created tables if non-existed')


## close DB connection to free space in connection pool
# more specific to SQL DBs,
DATABASE.close()
