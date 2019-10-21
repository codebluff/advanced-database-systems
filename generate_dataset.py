import sqlite3
import random

con = sqlite3.connect("Database.db")

c = con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS DMART(CUST_ID INT PRIMARY KEY, TRAN_ID INT, ITEM VARCHAR(10), ITEM_ID INT, "
          "QUANTITY INT, "
          "PRICE DOUBLE)")


def show_database():
    con = sqlite3.connect("Database.db")

    c = con.cursor()

    c.execute("SELECT * FROM DMART")
    r = c.fetchall()

    print("----------------------------------------------------")

    for c in r:
        print(c)

def generate_data():
        cust_id = 2019000
        tran_id = 0
        item = {
            101 : 'biscuits',
            102 : 'milk',
            103 : 'butter',
            104 : 'washing powder',
            105 : 'diaper',
            106 : 'books',
            107 : 'pen',
            108 : 'pencil'
            }
        quantity3 = [
            1, 2, 3, 4, 5
        ]

        price = {
            10 : 'biscuits',
            22 : 'milk',
            20 : 'butter',
            10 : 'washing powder',
            500 : 'diaper',
            55 : 'books',
            25 : 'pen',
            3 : 'pencil'
                 }


        number_of_queries = int(input("Input number of records you want to generate"))
        for i in range(number_of_queries):
            cust_id += 1
            tran_id += 1
            itemchoice = random.choice(list(item))
            itemid = item.get(itemchoice)
            quantity = random.randrange(1, 9)
            rate = item.get(itemchoice)
            print(cust_id, tran_id, itemchoice, quantity, rate)
            c.execute("INSERT INTO DMART VALUES(?, ?, ?, ?, ?, ?)", (cust_id, tran_id,itemid,  itemchoice,  quantity, rate))
            c.execute("COMMIT")



choice = int(input("1. Generate dataset"
      "2. Show Database"
      "3. Exit"))

if choice == 1:
    generate_data()
if choice==2:
    show_database()
if choice==3:
    exit(0)