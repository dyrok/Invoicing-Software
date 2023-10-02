import mysql.connector

# Establishing MySQL Connection
def create_connection():
    host = "localhost"
    user = "root"
    password = "Neel@10062006"
    database = "IP_proj"
    print(f"Connecting to MySQL server at {host}...")
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# Function to add a new invoice
def add_invoice(cursor):
    invoice_number = input("Enter invoice number: ")
    buyer_name = input("Enter Buyer Name: ")
    buyer_phone = input("Enter buyer phone number: ")
    invoice_amount = float(input("Enter invoice amount: "))
    invoice_remark = input("Enter invoice remark: ")
    billing_address = input("Enter billing address: ")

    # Inserting data into the database
    query = "INSERT INTO invoices (invoice_number, buyer_name, buyer_phone, invoice_amount, invoice_remark, billing_address) VALUES (%s, %s, %s, %s, %s)"
    values = (invoice_number, buyer_name, buyer_phone, invoice_amount, invoice_remark, billing_address)
    cursor.execute(query, values)

    print("Invoice added successfully!")

# Function to display details of a specific invoice
def display_invoice_details(cursor):
    invoice_number = input("Enter the invoice number you want to see details for: ")

    # Retrieving data from the database
    query = "SELECT invoice_number, buyer_name, buyer_phone, invoice_amount, invoice_remark, billing_address FROM invoices WHERE invoice_number = %s"
    cursor.execute(query, (invoice_number,))
    result = cursor.fetchone()

    if result:
        print("=========================================================")
        print("Invoice Details:")
        print(f"0. Invoice Number: {result[0]}")
        print(f"1. Buyer Name: {result[1]}")
        print(f"2. Buyer Phone Number: {result[2]}")
        print(f"3. Invoice Amount: {result[3]}")
        print(f"4. Invoice Remark: {result[4]}")
        print(f"5. Billing Address: {result[5]}")
        print("=========================================================")
    else:
        print(f"No invoice found with invoice number {invoice_number}")

#ALL INVOICE DETAILS
def display_all_invoices(cursor):
    # Retrieving data from the database
    query = "SELECT invoice_number, buyer_name, invoice_remark FROM invoices"
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("=========================================================")
        print("All Invoices:")
        for result in results:
            print(f"1. Invoice Number: {result[0]}")
            print(f"2. Buyer Name: {result[1]}")
            print(f"3. Invoice Remark: {result[2]}")
            print("---------------------------------------------------------")
        print("=========================================================")
    else:
        print("No invoices found.")


#listing all employee function

def list_all_employees(cursor):
    # Retrieving distinct data from the database
    query = "SELECT DISTINCT buyer_name, buyer_phone FROM invoices"
    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        print("=========================================================")
        print("All Employees:")
        for result in results:
            print(f"Buyer Name: {result[0]}")
            print(f"Buyer Phone Number: {result[1]}")
            print("---------------------------------------------------------")
        print("=========================================================")
    else:
        print("No employees found.")

# Main function
def main():
    # Creating a MySQL connection and cursor
    connection = create_connection()
    cursor = connection.cursor()

    while True:
        print("\n1. Inv Add\n2. Inv Detail\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_invoice(cursor)
        elif choice == "2":
            display_all_invoices(cursor)
            display_invoice_details(cursor)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Closing the cursor and connection
    cursor.close()
    connection.close()

main()
