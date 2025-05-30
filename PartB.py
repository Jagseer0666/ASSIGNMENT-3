def get_valid_date():
    while True:
        date = input("Date (dd/mm/yyyy): ")
        parts = date.split('/')
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            day, month, year = parts
            if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and len(year) == 4:
                return date
        print("Invalid date format. Please try again.")

def create_requisition(requisition_id_counter):
    date = get_valid_date()
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")
    requisition_id_counter += 1
    requisition_id = str(requisition_id_counter)
    print(f"Requisition ID: {requisition_id}")
    
    return {
        "date": date,
        "staff_id": staff_id,
        "staff_name": staff_name,
        "requisition_id": requisition_id,
        "products": [],
        "total_price": 0,
        "status": "",
        "approval_ref": None
    }, requisition_id_counter

def add_products_to_requisition(req):
    total = 0
    print(f"\nRequisition ID: {req['requisition_id']} (Staff: {req['staff_name']})")
    while True:
        product = input("Enter product name (or 'done' to finish): ")
        if product.lower() == "done":
            break
        try:
            price = float(input(f"Enter price for {product}: $"))
            total += price
            req["products"].append((product, price))
        except ValueError:
            print("Invalid price. Skipping.")
    req["total_price"] = total
    print(f"Requisition total = ${total:.2f}")

def evaluate_requisition(req):
    total = req["total_price"]
    if total <= 500:
        req["status"] = "Approved"
        req["approval_ref"] = req["staff_id"] + req["requisition_id"][-3:]
    elif total >= 501:
        req["status"] = "Pending"
    else:
        req["status"] = "Not approved"

def print_requisition_summary(req):
    print(f"\nRequisition ID: {req['requisition_id']}")
    print(f"Total: ${req['total_price']:.2f} → Status: {req['status']}")
    if req["approval_ref"]:
        print(f"Approval Reference Number: {req['approval_ref']}")
    else:
        print("Approval reference number is not available.")

def main():
    requisitions = []
    requisition_id_counter = 10000

    print("\n--- Enter Staff and Requisition Info ---")
    while True:
        req, requisition_id_counter = create_requisition(requisition_id_counter)
        requisitions.append(req)
        if input("Do you want to enter another? (yes/no): ").lower() != "yes":
            break

    print("\n--- Enter Products for Each Requisition ---")
    for req in requisitions:
        add_products_to_requisition(req)

    print("\n--- Checking Approval Status ---")
    approved = pending = not_approved = 0
    for req in requisitions:
        evaluate_requisition(req)
        print_requisition_summary(req)
        if req["status"] == "Approved":
            approved += 1
        elif req["status"] == "Pending":
            pending += 1
        else:
            not_approved += 1

    print("\n--- Summary Statistics ---")
    print(f"Total Requisitions: {len(requisitions)}")
    print(f"Approved: {approved}")
    print(f"Pending: {pending}")
    print(f"Not Approved: {not_approved}")

# Run the program
main()
