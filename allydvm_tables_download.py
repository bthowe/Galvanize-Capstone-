# source activate py3
# source deactivate
import mysql.connector
import os
import csv

def clients():
    print("Clients database scraper:")
    filename = open('../clients.csv', 'w')
    c = csv.writer(filename)
    c.writerow(('client_id', 'practice_id', 'address', 'city', 'state', 'zip'))

    config = {
      'user': os.getenv('ALLYDVM_USER_NAME'),
      'password': os.getenv('ALLYDVM_USER_PASSWORD'),
      'host': os.getenv('ALLYDVM_HOST'),
      'database': 'pulsar',
      'port': '3306'
    }

    conn = mysql.connector.connect(**config)
    crsr = conn.cursor()
    print("Performing query now...\n")
    query = ("SELECT client_id, practice_id, address, city, state, postal_code FROM clients")
    crsr.execute(query)

    print("Fetching rows now...\n")
    row = crsr.fetchone()
    while row is not None:
        c.writerow(row)
        # try:
        #     c.writerow(row)
        # except:
        #     print(row)
        row = crsr.fetchone()

    crsr.close()
    filename.close()
    conn.close()


def invoice():
    print("Clients merged invoice scraper\n\n\n")
    filename = open('../invoice_data.csv', 'w')
    c = csv.writer(filename)
    c.writerow(('source_id', 'invoice_item_id', 'practice_id', 'transaction_id', 'patient_id', 'product_id', 'last_synced_at', 'quantity', 'price', 'description', 'practice_address', 'practice_city', 'practice_state', 'practice_postal_code', 'client_address', 'client_city', 'client_state', 'client_postal_code'))

    config = {
      'user': os.getenv('ALLYDVM_USER_NAME'),
      'password': os.getenv('ALLYDVM_USER_PASSWORD'),
      'host': os.getenv('ALLYDVM_HOST'),
      'database': 'pulsar',
      'port': '3306'
    }

    conn = mysql.connector.connect(**config)
    crsr = conn.cursor()
    query = ("SELECT ii.source_id, ii.invoice_item_id, ii.practice_id, ii.transaction_id, ii.patient_id, ii.product_id, ii.last_synced_at, ii.quantity, ii.price, p.description, pr.address, pr.city, pr.state, pr.postal_code, c.address, c.city, c.state, c.postal_code FROM invoice_items ii JOIN products p ON ii.product_id=p.product_id JOIN practices pr ON ii.practice_id=pr.id JOIN transactions t ON t.transaction_id=ii.transaction_id JOIN clients c ON t.client_id=c.client_id WHERE p.description rlike 'heartgard|heartguard|hartgard|hartguard' 'Sentinel|Sentinal' 'Proheart|prohart' 'Trifexis' 'trihart|triheart' 'iverhart|iverheart' 'interceptor|intercepter' 'revolution|revoluton' 'advantage Multi|advantagemulti'")
    crsr.execute(query)

    row = crsr.fetchone()
    while row is not None:
        c.writerow(row)
        # try:
        #     c.writerow(row)
        # except:
        #     print(row)
        row = crsr.fetchone()

    crsr.close()
    filename.close()
    conn.close()


if __name__=="__main__":
    clients()
    # invoice()
