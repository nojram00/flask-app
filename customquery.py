from mysqlconfig import mysqlconfig
import json

m = mysqlconfig('localhost', 'root', '', 'inventory_db')
# res  = m.select('categories').execute()



# m.select('items').innerjoin('categories', 'id', 'category_index').where('category','motherboards').where('items.id', '3').testQuery()
res = m.select('items').innerjoin('categories', 'id', 'category_index').execute()

# j = json.dumps(res)
# print()
for r in res:
    print({
        'item' : r[1],
        'category': r[7]
    })
