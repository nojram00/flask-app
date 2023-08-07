import mysql.connector

#Database Controller lahat ng papasok at lalabas dederetsyo dito:
class mysqlconfig():

    def __init__(self, host, username, password, database):
        # initialize msql connection:
        self.connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database)
        # self.kupal = "wews"

        #initialize cursor
        self.mcursor = self.connection.cursor()

    def select(self, table):
        self.query = f"SELECT * FROM {table}"
        self.table = table
        return self

    def insert(table, **items):
        cols = items.keys()
        values = items.values()
        self.query = f"INSERT INTO {', '.join(cols)} {table} VALUES {', '.join(values)}"
        return self

    def where(self, colm, value):
        if 'WHERE' in self.query:
            self.query += f" AND {colm} = '{value}'"
        else:
            self.query += f" WHERE {colm} = '{value}'"
        return self

    def innerjoin(self, joinTable, joinCol, tableCol):
        self.query += f" INNER JOIN {joinTable} ON {joinTable}.{joinCol} = {self.table}.{tableCol}"
        return self

    def testQuery(self):
        print(self.query)

    def execute(self):
        self.mcursor.execute(self.query)
        data = self.mcursor.fetchall()
        self.mcursor.close()
        return data



