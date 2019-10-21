import sqlite3

con = sqlite3.connect("Database.db")

c = con.cursor()

c.execute("SELECT * FROM DMART")

minimum_support = int(input("Enter minimum support required: "))

item = input("Choose product name to find product support: Mention data to retrieve:"
          "biscuits\nmilk\nbutter\nwashing powder\ndiaper\nbooks\npen\npencil")


c.execute("SELECT * FROM DMART")
r = c.fetchall()
total_number_of_records = 0

for x in r:
    total_number_of_records +=1


query = "SELECT * FROM DMART WHERE ITEM = " + "'" + item + "'"
print(query)
c.execute(query)
r = c.fetchall()

print("----------------------------------------------------")

supporting_records =0

for c in r:
    print(c)
    supporting_records +=1



print("Support recieved for ", item, end=" ")


support_acquired = (supporting_records/total_number_of_records)*100

print("is ", support_acquired)

if support_acquired > minimum_support:
    print(item, "Satisfies the given minimum support criteria")
else:
    print(item, "Does not satisfy the support criteria")

"""
Mention data to retrieve:"
          "CUST_ID, TRAN_ID, ITEM, ITEM_ID, QUANTITY, PRICE
"""