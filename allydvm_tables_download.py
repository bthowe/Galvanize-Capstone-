# source activate py3
# source deactivate
import pandas as pd
import mysql.connector
import os
import csv

def clients():
    print("Clients database scraper:")
    filename = open('../data/clients.csv', 'w')
    c = csv.writer(filename)
    c.writerow(('source_id', 'client_id', 'practice_id', 'address', 'city', 'state', 'zip'))

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
    query = ("SELECT source_id, client_id, practice_id, address, city, state, postal_code FROM clients")
    crsr.execute(query)

    print("Fetching rows now...\n")
    row = crsr.fetchone()
    while row is not None:
        c.writerow(row)
        row = crsr.fetchone()

    crsr.close()
    filename.close()
    conn.close()


def employees():
    print("Employees database scraper:")
    filename = open('../data/employees.csv', 'w')
    c = csv.writer(filename)
    c.writerow(('source_id', 'employee_id', 'practice_id', 'first_synced_at', 'last_synced_at', 'first_name', 'last_name', 'title'))

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
    query = ("SELECT source_id, employee_id, practice_id, first_synced_at, last_synced_at, first_name, last_name, title FROM employees")
    crsr.execute(query)

    print("Fetching rows now...\n")
    row = crsr.fetchone()
    while row is not None:
        c.writerow(row)
        row = crsr.fetchone()

    crsr.close()
    filename.close()
    conn.close()

def invoice():
    print("Merged invoice scraper:")
    filename = open('../data/invoice_data.csv', 'w')
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
    print("Performing query now...\n")
    query = ("SELECT ii.source_id, ii.invoice_item_id, ii.practice_id, ii.transaction_id, ii.patient_id, ii.product_id, ii.last_synced_at, ii.quantity, ii.price, p.description, pr.address, pr.city, pr.state, pr.postal_code, c.address, c.city, c.state, c.postal_code FROM invoice_items ii JOIN products p ON ii.product_id=p.product_id AND ii.source_id=p.source_id JOIN practices pr ON ii.practice_id=pr.id AND ii.source_id=pr.source_id JOIN transactions t ON ii.transaction_id=t.transaction_id AND ii.source_id=t.source_id JOIN clients c ON t.client_id=c.client_id AND t.source_id=c.source_id WHERE p.description rlike 'heartgard|heartguard|hartgard|hartguard|Sentinel|Sentinal|Proheart|prohart|Trifexis|trihart|triheart|iverhart|iverheart|interceptor|intercepter|revolution|revoluton|advantage Multi|advantagemulti'")
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

def load_data_client():
    df = pd.read_csv('../data/clients.csv')
    df.to_pickle('../data/clients_pickle')
    print(df.info())
    print(df.head())

def load_data_employees():
    df = pd.read_csv('../data/employees.csv')
    df.to_pickle('../data/employees_pickle')
    print(df.info())
    print(df.head())

def load_data_invoice():
    df = pd.read_csv('../data/invoice_data.csv')
    df.to_pickle('../data/invoice_pickle')
    print(df.info())
    print(df.head())

if __name__=="__main__":
    # clients()
    load_data_employees()
    # invoice()
