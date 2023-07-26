from mysqlconfig import mysqlconfig as mysql
class items():

    def __init__(self):
        self.m = mysql('localhost', 'root', '', 'inventory_db')

    def retrieve(self):
        data = self.m.retrieve_all('items')

        dataArray = []
        dataArray.clear()

        for d in data:
            dataArray.append(
                {
                    "id": d[0],
                    "name": d[1],
                    "price": d[2],
                    "quantity": d[3],
                    "description": d[4],
                }
            )
        return dataArray

    def retrieve_by_category(self, category):
       data = self.m.retrieve_by_category(category)

       dataArray = []
       dataArray.clear()
       for d in data:
        dataArray.append({
            'id': d[0],
            'name': d[1],
            'price': d[2],
            'quantity': d[3],
            'description': d[4],
            'category': d[5]
        })

       return dataArray
