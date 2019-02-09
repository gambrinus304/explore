import csv
from peewee import *



db = PostgresqlDatabase(database='test', user='postgres', password='1', host='localhost')


class Coin(Model):
    name = CharField()
    url = TextField()
    price = CharField()

    class Meta:
        database = db


def refined(r):
    row = r.split('Dict')[-1]
    return row
    

def main():

    db.connect()
    db.create_tables([Coin])

    with open ('cmc.csv') as f:
        order = ['name', 'url', 'price']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader)

        # ---test---
        # for row in coins:
            # row = refined(str(r))
            # print(row)


        # ---first method---
        # for row in coins:
        #     coin = Coin(name=row['name'], url=row['url'], price=row['price'])
        #     coin.save()


        # ---run with transactions---
        # with db.atomic():
        #     for row in coins:
        #         Coin.create(**row) # **row == **kwargs

        # ---run with slise and index---
        with db.atomic():
            for index in range(0, len(coins), 100):
                Coin.insert_many(coins[index:index+100]).execute()



if __name__ == "__main__":
    main()