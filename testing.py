# for testing only wag pansinin ang name....



# from db import Database
# from items import Items
import json
from pprint import pprint
from models.items import Items
from models.orders import Orders
# res = (items().select()
#             .innerjoin("categories",
#                 "categories.id",
#                     "=",
#                 "items.category_index")
#             .go())
# pprint(res)
# items().test()

# m = Database('localhost', 'root', '', 'inventory_db')
# res  = m.select('items').execute()



# # m.select('items').innerjoin('categories', 'id', 'category_index').where('category','motherboards').where('items.id', '3').testQuery()
# res = m.select('items').innerjoin('categories', 'id', 'category_index').execute()
i = Items()
o = Orders()
# res = items.table()
# res = i.itemsWithCategory()
# res = i.all()
res = o.order(1)
pprint(res)

# j = json.dumps(res)

# for r in res:
#     print({
#         'item' : r[1],
#         'category': r[7]
#     })

# x = m.insert('items', name='motherboard4', price=9000, quantity=4, description='wala trip lang ulit', category_index=1).executeInsert()
# print(x)
