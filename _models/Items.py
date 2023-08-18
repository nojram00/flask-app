from .basemodel import Model

class items(Model):
    table = 'items'
    def __init__(self):
        super().__init__(items.table)

    def allItems(self):
        return (self.select()
                    .innerjoin("categories",
                                "categories.id", "=",
                                "items.category_index")
                    .go())

    @classmethod
    def test(cls):
        print(items.table)



