from unidecode import unidecode
import mysql.connector
import os
import csv


filename = open('clients.csv', 'w')
c = csv.writer(filename)

config = {
  'user': os.getenv('ALLYDVM_USER_NAME'),
  'password': os.getenv('ALLYDVM_USER_PASSWORD'),
  'host': 'db.allydvm.com',
  'database': 'pulsar',
  'port': '3306'
}

conn = mysql.connector.connect(**config)
crsr = conn.cursor()
# query = ("SELECT * FROM invoice_items ii JOIN products p ON ii.product_id=p.product_id LIMIT 10")
query = ("(SELECT 'source_id', 'invoice_item_id', 'practice_id', 'transaction_id', 'patient_id', 'product_id', 'last_synced_at', 'quantity', 'price', 'description', 'address', 'city', 'state', 'postal_code') UNION (SELECT ii.source_id, ii.invoice_item_id, ii.practice_id, ii.transaction_id, ii.patient_id, ii.product_id, ii.last_synced_at, ii.quantity, ii.price, p.description, pr.address, pr.city, pr.state, pr.postal_code FROM invoice_items ii JOIN products p ON ii.product_id=p.product_id JOIN practices pr ON ii.practice_id=pr.id LIMIT 10)")

crsr.execute(query)

row = crsr.fetchone()
while row is not None:
    # print row
    try:
        c.writerow(row)
    except:
        print row
    row = crsr.fetchone()

crsr.close()
filename.close()
conn.close()





# maybe I also need the tax? is this why jason uses the transaction database?
# (SELECT 'source_id', 'invoice_item_id', 'practice_id', 'transaction_id', 'patient_id', 'product_id', 'last_synced_at', 'quantity', 'price', 'description', 'address', 'city', 'state', 'postal_code') UNION (SELECT ii.source_id, ii.invoice_item_id, ii.practice_id, ii.transaction_id, ii.patient_id, ii.product_id, ii.last_synced_at, ii.quantity, ii.price, p.description, pr.address, pr.city, pr.state, pr.postal_code FROM invoice_items ii JOIN products p ON ii.product_id=p.product_id JOIN practices pr ON ii.practice_id=pr.id LIMIT 10)
