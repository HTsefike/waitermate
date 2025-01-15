class Order:


    def __init__(self, table_number, items):
        self.table_number = table_number
        self.items = items
        self.status = "Pending"
    
    def mark_ready(self):
        self.status = "Ready"

orders = []  # Shared order queue

def login():
    staff_id = input("Enter staff-ID: ")
    password = input("Enter password: ")
    if staff_id == "admin" and password == "admin":
        print("Login successful!")
        return True
    else:
        print("Login failed. Please try again.")
        return False

def take_order():
    table_number = input("Enter table number: ")
    items = input("Enter order items (comma-separated): ").split(',')
    order = Order(table_number, items)
    orders.append(order)
    print(f"Order for Table {table_number} has been sent to the kitchen.")

def view_orders():
    if not orders:
        print("No orders in the queue.")
        return
    for idx, order in enumerate(orders):
        print(f"{idx + 1}. Table {order.table_number} - {order.items} (Status: {order.status})")

def update_order():
    view_orders()
    order_index = int(input("Enter order number to update: ")) - 1
    if 0 <= order_index < len(orders):
        orders[order_index].mark_ready()
        print(f"Order for Table {orders[order_index].table_number} is marked as Ready!")
    else:
        print("Invalid order number.")

# Main menu
def main():
    print("Welcome to WaiterMate!")
    if not login():
        print("Please login to continue.")
        for _ in range(5):
            if login():
                break
    else :
        while True:
            print("\n1. Take Order\n2. View Orders\n3. Update Order Status\n4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                take_order()
            elif choice == '2':
                view_orders()
            elif choice == '3':
                update_order()
            elif choice == '4':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
