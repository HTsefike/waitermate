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

    def add_notes(self, notes):
        self.notes = notes

# Sample shared queue of orders (simulating waiter input)
orders = [
    Order("1", ["Burger", "Fries"], "waiter1"),
    Order("2", ["Pizza", "Coke"], "waiter1"),
    Order("3", ["Pasta", "Salad"], "waiter1"),
]

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


def view_pending_orders(cook_id):
    print("\n--- Pending Orders ---")
    pending_orders = [order for order in orders if order.status == "Pending"]
    if not pending_orders:
        print("No pending orders.")
    for idx, order in enumerate(pending_orders):
        print(f"{idx + 1}. Table {order.table_number} - {order.items} (Status: {order.status})")

def mark_order_ready(cook_id):
    view_pending_orders(cook_id)
    if not any(order.status == "Pending" for order in orders):
        return
    try:
        order_index = int(input("\nEnter the order number to mark as Ready: ")) - 1
        if 0 <= order_index < len(orders):
            orders[order_index].mark_ready()
            print(f"Order for Table {orders[order_index].table_number} has been marked as Ready!")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a valid number.")

def add_order_notes(cook_id):
    view_pending_orders(cook_id)
    if not any(order.status == "Pending" for order in orders):
        return
    try:
        order_index = int(input("\nEnter the order number to add notes: ")) - 1
        if 0 <= order_index < len(orders):
            notes = input("Enter notes for the order: ")
            orders[order_index].add_notes(notes)
            print(f"Notes added to order for Table {orders[order_index].table_number}.")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a valid number.")

def view_completed_orders(cook_id):
    print("\n--- Completed Orders ---")
    completed_orders = [order for order in orders if order.status == "Ready"]
    if not completed_orders:
        print("No completed orders yet.")
    for order in completed_orders:
        print(f"Table {order.table_number} - {order.items} (Notes: {order.notes or 'None'})")

def mark_order_ready(cook_id):
    view_pending_orders(cook_id)
    if not any(order.status == "Pending" for order in orders):
        return
    try:
        order_index = int(input("\nEnter the order number to mark as Ready: ")) - 1
        if 0 <= order_index < len(orders):
            orders[order_index].mark_ready()
            orders[order_index].assign_cook(cook_id)
            print(f"Order for Table {orders[order_index].table_number} marked as Ready by Cook {cook_id}!")
        else:
            print("Invalid order number.")
    except ValueError:
        print("Please enter a valid number.")
        
def view_order_summary(cook_id):
    print("\n--- Order Summary ---")
    for order in orders:
        print(f"Table {order.table_number} - {order.items}")
        print(f"Waiter: {order.waiter_id} | Cook: {order.cook_id or 'Not Assigned'} | Status: {order.status}")
        print("-" * 40)

# Main menu for kitchen program
def kitchen_program(cook_id):
    print("Welcome to WaiterMate!")
    if not login():
        print("Please login to continue.")
        for _ in range(5):
            if login():
                break
    else :
        while True:
            print("\n--- Kitchen Program ---")
            print("1. View Pending Orders")
            print("2. Mark Order as Ready")
            print("3. Add Notes to Order")
            print("4. View Completed Orders")
            print("5. Order Summary")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                view_pending_orders(cook_id)
            elif choice == '2':
                mark_order_ready(cook_id)
            elif choice == '3':
                add_order_notes(cook_id)
            elif choice == '4':
                view_completed_orders(cook_id)
            elif choice == '5':
                view_order_summary(cook_id)
            elif choice == '6':
                print("Exiting Kitchen Program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

logged_in_user = login()
if logged_in_user and logged_in_user["role"] == "cook":
    cook_id = logged_in_user["id"]
    kitchen_program(cook_id)


if __name__ == "__main__":
    kitchen_program()
