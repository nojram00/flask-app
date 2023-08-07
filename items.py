from mysqlconfig import mysqlconfig as mysql
class items():

    m = mysqlconfig('localhost', 'root', '', 'inventory_db')

    @staticmethod
    def fetch_items_by_category(categoryname):
        res = m.select('items').innerjoin('categories', 'id', 'category_index').where('category',f'{categoryname}').where('items.id', '3').execute()
        return res


