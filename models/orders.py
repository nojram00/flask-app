from .db import Database
import json

class Orders:
    table = 'orders'

    def __init__(self):
        self.m = Database()

    def order(self, orderID):
        # raise 'tuple' object has no attribute 'where' error
        # d = self.m.select(('orders', *("JSON_UNQUOTE(item_order->'$.motherboard.id') AS motherboard_id",
        #                             "JSON_UNQUOTE(item_order->'$.motherboard.name') AS motherboard_name")).where("id", orderID).execute())

        # Success
        d = self.m.select('orders', *("JSON_UNQUOTE(item_order->'$.motherboard.id') AS motherboard_id",
                                    "JSON_UNQUOTE(item_order->'$.motherboard.name') AS motherboard_name"))\
                        .where("id", orderID)\
                        .execute()
        return d
