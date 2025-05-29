class RequisitionSystem:
    def __init__(self):
        # Initialize all values
        self.requisition_id = 10000
        self.total_cost = 0
        self.total_requests = 0
        self.approved_requests = 0
        self.not_approved_requests = 0
        self.status = "Pending"
        self.reference_number = "Not Available"

    def staff_info(self):
        # Get staff information
        self.date = input("Enter the date (YYYY-MM-DD): ")
        self.staff_id = input("Enter staff ID: ")
        self.staff_name = input("Enter staff name: ")
        self.requisition_id += 1  # Increase ID
        self.total_requests += 1  # Count the request
        self.status = "Pending"  # Reset status
        self.reference_number = "Not Available"  # Reset reference
        self.total_cost = 0  # Reset cost for new request

    def requisition_details(self):
        # Add item prices
        while True:
            item = input("Enter item name or type 'done' to finish: ")
            if item.lower() == "done":
                break
            try:
                price = float(input("Enter item price: $"))
                if price <= 0:
                    print("Price must be more than 0.")
                else:
                    self.total_cost += price
            except ValueError:
                print("Please enter a valid number.")

    def requisition_approval(self):
        # Decide approval based on cost
        if self.total_cost == 0:
            print("No items added. Cannot approve.")
            return

        if self.total_cost < 500:
            self.status = "Approved"
            self.approved_requests += 1
            self.reference_number = self.staff_id.upper() + str(self.requisition_id)[-3:]
        else:
            print("This request needs manual approval.")
            response = input("Type 'approve' or 'not approve': ").lower()
            if response == "approve":
                self.status = "Approved"
                self.approved_requests += 1
                self.reference_number = self.staff_id.upper() + str(self.requisition_id)[-3:]
            elif response == "not approve":
                self.status = "Not Approved"
                self.not_approved_requests += 1
                self.reference_number = "Not Available"
            else:
                print("Invalid response. Status remains Pending.")
                self.status = "Pending"

        print("Requisition Status:", self.status)
        print("Reference Number:", self.reference_number)

    def display_requisition(self):
        # Show requisition information
        print("\n--- Requisition Details ---")
        print("Date:", self.date)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Requisition ID:", self.requisition_id)
        print("Total Cost: $", format(self.total_cost, ".2f"))
        print("Status:", self.status)
        print("Reference Number:", self.reference_number)

    def requisition_statistics(self):
        # Show totals
        print("\n--- Requisition Statistics ---")
        print("Total Requests:", self.total_requests)
        print("Approved Requests:", self.approved_requests)
        print("Not Approved Requests:", self.not_approved_requests)
        pending = self.total_requests - self.approved_requests - self.not_approved_requests
        print("Pending Requests:", pending)

    def main_menu(self):
        # Menu for user
        while True:
            print("\n--- MENU ---")
            print("1. Enter Requisition")
            print("2. Approve/Reject Requisition")
            print("3. Display Requisition")
            print("4. Show Statistics")
            print("0. Exit")
            choice = input("Choose an option (0-4): ")

            if choice == "1":
                self.staff_info()
                self.requisition_details()
            elif choice == "2":
                self.requisition_approval()
            elif choice == "3":
                self.display_requisition()
            elif choice == "4":
                self.requisition_statistics()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    app = RequisitionSystem()
    app.main_menu()
