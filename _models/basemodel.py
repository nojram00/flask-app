from db import Database

class Model:
    db = Database('localhost', 'root', '', 'inventory_db')
    table = ''
    query = ''
    def __init__(self, table):
        self.db = Model.db
        Model.table = table

    def insert(self, *cols):
        new_cols = []

        for col in cols:
            new_cols.append(f"`{col}`")

        Model.query = f"INSERT INTO {Model.table} {', '.join(cols)}"
        return self

    def values(self,*values):
        new_values = []

        for val in values:
            if isinstance(val, str):
                new_values.append(f"'{val}'")
            elif isinstance(val, int):
                new_values.append(f"{val}")

        Model.query += f"VALUES {', '.join(new_values)}"
        return self

    def AND(self, *args):
        Model.query += f"AND {' '.join(args)}"
        return self

    def execute(self):
        self.db.cursor.execute(Model.query)
        self.db.cursor.commit()
        self.db.cursor.close()

    @classmethod
    def select(cls):
        Model.query = f"SELECT * FROM {Model.table} "
        # return Model.db.cursor.fetchall()
        return cls

    @classmethod
    def innerjoin(cls, table, *args):
        # stmt = []
        # for a in args:
        #     if a != '=':
        #         stmt.append(f"'{a}'")
        #     else:
        #         stmt.append(f"{a}")

        # Model.query += f"INNER JOIN {table} ON {' '.join(stmt)} "
        Model.query += f"INNER JOIN {table} ON {' '.join(args)} "
        return cls

    @classmethod
    def where(cls,*args):
        stmt = []
        for a in args:
            if a != '=':
                stmt.append(f"'{a}'")
            else:
                stmt.append(f"{a}")

        Model.query += f"WHERE {' '.join(stmt)} "
        return cls

    @classmethod
    def AND(cls, *args):
        Model.query += f"AND {' '.join(args)}"
        return cls

    def go():
        # print(Model.query)
        print(Model.db.cursor)
        Model.db.cursor.execute(Model.query)
        return Model.db.cursor.fetchall()

# Model().select().go()
