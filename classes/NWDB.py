import sqlite3


class NWDB(object):
    """sqlite3 database class that holds testers jobs"""
    DB_LOCATION = "testing/db/resources.db"

    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(self.DB_LOCATION)
        self.cur = self.connection.cursor()

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def executemany(self, many_new_data):
        """add many new data to database in one go"""
        self.create_table()
        self.cur.executemany('REPLACE INTO jobs VALUES(?, ?, ?, ?)', many_new_data)

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute('''CREATE TABLE IF NOT EXISTS jobs(title text, \
                                                            job_id integer PRIMARY KEY, 
                                                            company text,
                                                            age integer)''')

    def commit(self):
        """commit changes to database"""
        self.connection.commit()

    def get_auctioneer_resources(self):
        self.cur.execute("SELECT * FROM resources")
        return self.cur.fetchall()

    def insert_new_resource(self, item):
        self.cur.execute("insert into resources (name, image_name, searchable_name) values (?, ?, ?)", item)