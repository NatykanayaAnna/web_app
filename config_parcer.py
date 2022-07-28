import sys
from configparser import ConfigParser, NoOptionError, NoSectionError
config = ConfigParser()

CONFIG_FILE = 'config.ini'
config.read(CONFIG_FILE)

try:
    dbms = config.get('database', 'dbms')
    db_user = config.get('database', 'db_user')
    db_password = config.get('database', 'db_password')
    db_url = config.get('database', 'db_url')
    db_port = config.get('database', 'db_port')
    db_name = config.get('database', 'db_name')
except (NoOptionError, NoSectionError) as e:
    print(f"Some configs for database connection are missing. Please, check {CONFIG_FILE} file:")
    print(e)
    sys.exit(1)

db_connection_string = f"{dbms}://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"

