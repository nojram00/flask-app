import mysqlconfig
from collections import OrderedDict


#Sample only
class records():
    def __init__(self):
        self.m = mysqlconfig.mysqlconfig('localhost', 'root', '', 'inventory_db')
        pass

    def getData(self):
        data = self.m.retrieve_all('sample_tb')
        dataArray = []
        for d in data:
            dt = dict(
                id = d[0],
                firstname = d[1],
                lastname = d[2],
                age= d[3]
            )
            dataArray.append(dt)
        return dataArray

    def getDataById(self, id):
        data = self.m.retrieve_by_id('sample_tb', id)
        dataArray = []

        for d in data:
            dt = dict(
                id = d[0],
                firstname = d[1],
                lastname = d[2],
                age= d[3]
            )
            dataArray.append(dt)

        return dataArray

    def insertNewData(self, fname, lname, age):
        params = "'{}','{}','{}'".format(fname, lname, age)
        keys ="`first_name`, `last_name`, `age`"
        data = self.m.insertData('sample_tb', keys, params)
        return data
# r = Records()

# r.getData()
