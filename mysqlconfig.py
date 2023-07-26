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

        #initialize cursor
        self.mcursor = self.connection.cursor()

    def test(self):
        pass

    def retrieve_all(self, table):
        data = []
        data.clear()

        query = "SELECT * FROM {}"

        print(query.format(table))

        self.mcursor.execute(query.format(table))

        for d in self.mcursor:
            data.append(d)

        return data

    def retrieve_by_id(self, table, id):
        data = []
        data.clear()
        query = "SELECT * FROM {} WHERE id = {}"
        print(query.format(table, id))

        self.mcursor.execute(query.format(table, id))

        for d in self.mcursor:
            data.append(d)

        return data

    def insertData(self, table, key, value):
        query = "INSERT INTO {} ( {} ) VALUES ( {} )".format(table, key, value)
        # query = "INSERT INTO `sample_tb` (`id`, `first_name`, `last_name`, `age`) VALUES (NULL, 'Rendon', 'Labador', 30)"
        print(query)
        self.mcursor.execute(query)
        self.connection.commit()

        message = "message: success!"
        return message

    def retrieve_by_category(self, category):
        data = []
        data.clear()
        query = "SELECT * FROM items WHERE `category` = '{}'".format(category)
        print(query)
        self.mcursor.execute(query)

        for d in self.mcursor:
            data.append(d)

        return data
    # def get_data(self):
    #     return self.data

