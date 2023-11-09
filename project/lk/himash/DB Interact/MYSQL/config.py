# from mysql import connector
import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='1111',
    database='accessories_db'
)

cursor = db.cursor()

insert_cus = 'insert into customer (id, email, nic) values (%s, %s, %s)'
customer = ('0005', 'test@gmail.com', '985462587v')
cursor.execute(insert_cus, customer)
customers = [('0006', 'test@gmail.com', '985462587v'),('0007', 'test@gmail.com', '985462587v')]
cursor.executemany(insert_cus, customers)
db.commit()

fetch_customers = 'select * from customer'
cursor.execute(fetch_customers)
result = cursor.fetchall()
for c in result:
    print(c)
result = cursor.fetchone()
for c in result:
    print(c)

fetch_customers_con = "select * from customer where email like %s and nic like %s"
params = ("test@%", '98%')
cursor.execute(fetch_customers_con, params)
result = cursor.fetchall()
for c in result:
    print(c)

cursor.execute(fetch_customers_con, params)
result = cursor.fetchone()
for c in result:
    print(c)

update_customer = "update customer set email = 'gayan@gmail.com' where id = %s"
params = ("0007",)
cursor.execute(update_customer, params)
db.commit()

limit_customers = "select * from customer limit %s offset %s"
params = (3, 0)
cursor.execute(limit_customers, params)
result = cursor.fetchall()
for c in result:
    print(c)