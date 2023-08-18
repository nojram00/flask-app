import mysql.connector

#Database Controller lahat ng papasok at lalabas dederetsyo dito:
class Database():

    cursor = None

    host = 'localhost'
    username = 'root'
    password = ''
    database = 'hub_db'


    def __init__(self):
        # initialize msql connection:
        self.connection = mysql.connector.connect(
            host=Database.host,
            user=Database.username,
            password=Database.password,
            database=Database.database)
        # self.kupal = "wews"

        #initialize cursor
        self.mcursor = self.connection.cursor(dictionary=True)
        Database.cursor = self.mcursor

    def select(self, table, *cols):

        if not cols:
            self.query = f"SELECT * FROM {table}"
        else:
            self.query = f"SELECT {', '.join(cols)} FROM {table}"

        self.table = table
        return self

    def insert(self, table, **items):
        cols = items.keys()
        values = items.values()

        new_cols = []
        new_values = []

        for col in cols:
            new_cols.append(f"`{col}`")

        for val in values:
            if isinstance(val, str):
                new_values.append(f"'{val}'")
            elif isinstance(val, int):
                new_values.append(f"{val}")

        self.query = f"INSERT INTO {table} ({', '.join(new_cols)}) VALUES ({', '.join(new_values)})"
        return self

    def executeInsert(self):
        self.mcursor.execute(self.query)
        self.connection.commit()

        self.mcursor.close()
        self.connection.close()

    def where(self, colm, value):
        if 'WHERE' in self.query:
            self.query += f" AND {colm} = '{value}'"
        else:
            self.query += f" WHERE {colm} = '{value}'"
        return self

    def innerjoin(self, joinTable, *args):
        self.query += f" INNER JOIN {joinTable} ON {' '.join(args)}"
        print(self.query)
        return self

    def testQuery(self):
        print(self.query)

    def execute(self):
        self.mcursor.execute(self.query)
        print(self.query)
        data = self.mcursor.fetchall()
        self.mcursor.close()
        self.connection.close()
        return data



