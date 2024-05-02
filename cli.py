def main():
    print("Electronic Vendor Management System")
    print("1. Check Inventory")
    print("2. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        product_id = input("Enter product ID: ")
        check_inventory(product_id)
    elif choice == '2':
        return

def check_inventory(product_id):
    print(f"Checking inventory for Product ID: {product_id}")
    # This would interact with the database in a real scenario.

if __name__ == "__main__":
    main()

