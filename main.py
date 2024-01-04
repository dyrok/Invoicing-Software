import mysql.connector

# Establishing MySQL Connection
def create_connection():
    host = "localhost"
    user = "root"
    password = "password"
    database = "ip_inv"
    print(f"Connecting to MySQL server at {host}...")
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def main():
    # Creating a MySQL connection and cursor
    connection = create_connection()
    cursor = connection.cursor()

    while True:
        print("\n1. Inv Add\n2. Inv Detail\n3. Custom Query (For Developers!!!)\n4. Display all Customers\n5. Delete Invoice\n6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_invoice(connection, cursor)
        elif choice == "2":
            display_all_invoices(cursor)
            display_invoice_details(cursor)
        elif choice == "3":
            Custom_query(cursor, connection)
        elif choice == "4":
            list_all_employees(cursor)
        elif choice == "5":
            delete_invoice(cursor, connection)
        elif choice == "6":
            exit_program(connection, cursor)
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

# Function to add a new invoice
def add_invoice(connection, cursor):
    invoice_number = input("Enter invoice number: ")
    buyer_name = input("Enter Buyer Name: ")
    buyer_phone = input("Enter buyer phone number: ")
    invoice_amount = float(input("Enter invoice amount: "))
    invoice_remark = input("Enter invoice remark: ")
    billing_address = input("Enter billing address: ")
    invoice_date = input("Enter invoice date (YYYY-MM-DD): ")

    # Inserting data into the database
    query = "INSERT INTO invoices (invoice_number, buyer_name, buyer_phone, invoice_amount, invoice_remark, billing_address, invoice_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (invoice_number, buyer_name, buyer_phone, invoice_amount, invoice_remark, billing_address, invoice_date)

    cursor.execute(query, values)
    connection.commit()

    print("Invoice added successfully!")

# Function to display details of a specific invoice
def display_invoice_details(cursor):
    invoice_number = input("Enter the invoice number you want to see details for: ")

    # Retrieving data from the database
    query = "SELECT invoice_number, buyer_name, buyer_phone, invoice_amount, invoice_remark, billing_address, invoice_date FROM invoices WHERE invoice_number = %s"
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
        print(f"6. Invoice Date: {result[6]}")
        print("=========================================================")
    else:
        print(f"No invoice found with invoice number {invoice_number}")

# Function to display all invoice details
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

# Function to list all employees
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

# Function to execute a custom query
# Function to execute a custom query
def Custom_query(cursor, connection):
    print("This is for development purposes only. Please confirm if you are the developer.")
    choice = input("Please enter Y if you are the developer. Press any other key to return to the main menu: ")

    if choice == "Y" or choice == "y":
        query = input("Enter your query: ")
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch and print the results
        results = cursor.fetchall()
        if results:
            print("Query Results:")
            for result in results:
                print(result)
        
        # Commit the changes
        connection.commit()

        print("Query executed successfully.")
    else:
        print("Exited / Error Here's the Main Menu")


# Function to delete an invoice
def delete_invoice(cursor, connection):
    invoice_number = input("Enter the invoice number you want to delete: ")

    # Deleting data from the database
    query = "DELETE FROM invoices WHERE invoice_number = %s"
    cursor.execute(query, (invoice_number,))
    connection.commit()

    cursor.execute("SELECT * FROM invoices WHERE invoice_number = %s", (invoice_number,))
    result = cursor.fetchone()

    if result is None:
        print(f"Invoice with invoice number {invoice_number} deleted successfully.")
    else:
        print(f"No invoice found with invoice number {invoice_number}.")

# Function to exit the program and close the connection
def exit_program(connection, cursor):
    cursor.close()
    connection.close()
    exit()

# Main function
main()
