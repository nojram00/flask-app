from .db import Database
import json
# from models import basemodel as model
class Items():

    table = 'items'
    def __init__(self):
        self.m = Database()

    def all(self):
        d = self.m.select(Items.table).execute()
        # print (__name__)
        return d

    def insert(self, **cols):
        self.m.insert(__name__,cols).executeInsert()
        return "success"

    def itemsWithCategory(self):
        data = (self.m.select('items')
                    .innerjoin('categories', "'categories.id'", '=', "'items.category_index'")
                    .testQuery())
        return data



