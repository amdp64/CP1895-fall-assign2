# Business
from dataclasses import dataclass
import csv

file_path = "customers1.csv"

@dataclass
class Customer:
    id:int = 0
    firstName:str = ""
    lastName:str = ""
    company:str = ""
    address:str = ""
    city:str = ""
    state:str = ""
    zip:int = 0

    def getFullName(self):
        return self.firstName + " " + self.lastName
    
    def getFullAddress(self):
        if (self.company == ""):
            line1 = self.address
            line2 = self.city + ", " + self.state + " " + str(self.zip)
            return line1 + "\n" + line2
        else:
            line1 = self.company
            line2 = self.address
            line3 = self.city + ", " + self.state + " " + str(self.zip)
            return line1 + "\n" + line2 + "\n" + line3

def create_objects_from_csv(file_path):
    objects = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer = Customer(
                id=int(row['cust_id']),
                firstName=row['first_name'],
                lastName=row['last_name'],
                company=row['company_name'],
                address=row['address'],
                city=row['city'],
                state=row['state'],
                zip=int(row['zip']),
            )
            objects.append(customer)
    return objects

def findCustomer(customer_id):
    match_found = False
    customers = create_objects_from_csv(file_path)
    for customer in customers:
        if (customer.id == customer_id):
            print()
            print(customer.getFullName())
            print(customer.getFullAddress())
            match_found = True
    if (match_found == False):
        print()
        print("No customer with that ID.")

def display_welcome():
    print("Customer Viewer")

def main():
    display_welcome()
    get_customer_id = int(input("\nEnter customer ID: "))
    findCustomer(get_customer_id)
    while True:
        command = input("\nContinue? (y/n): ")
        if command == "n":
            break
        else:
            get_customer_id = int(input("\nEnter customer ID: "))
            findCustomer(get_customer_id)
    print("\nBye!")

if __name__ == "__main__":
    main()