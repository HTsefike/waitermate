class Order:
    def __init__(self, table_number, items, waiter_id):
        self.table_number = table_number
        self.items = items
        self.status = "Pending"
        self.notes = None
        self.waiter_id = waiter_id
        self.cook_id = None  # Assigned when the order is prepared

    def assign_cook(self, cook_id):
        self.cook_id = cook_id

    
    def mark_ready(self):
        self.status = "Ready"

orders = []  # Shared order queue

# Example staff database
staff_db = {
    "waiter1": {"password": "waiterpass1", "role": "waiter"},
    "cook1": {"password": "cookpass1", "role": "cook"},
    "admin": {"password": "admin", "role": "admin"},
}

def login():
    staff_id = input("Enter staff-ID: ")
    password = input("Enter password: ")
    if staff_id in staff_db and staff_db[staff_id]["password"] == password:
        print(f"Login successful! Welcome, {staff_id}.")
        return {"id": staff_id, "role": staff_db[staff_id]["role"]}
    else:
        print("Login failed. Please try again.")
        return None

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

def view_order_summary():
    print("\n--- Order Summary ---")
    for order in orders:
        print(f"Table {order.table_number} - {order.items}")
        print(f"Waiter: {order.waiter_id} | Cook: {order.cook_id or 'Not Assigned'} | Status: {order.status}")
        print("-" * 40)

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
                view_order_summary()
                break
            elif choice == '5':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
