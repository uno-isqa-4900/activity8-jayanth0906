import csv


def Title():
    print("Customer viewer program ")
    print()


class CustomerData:
    def __init__(self, custid="0", first_name="", last_name="", company_name="", address="", city="", state="", zip=""):
        self.custid = custid
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.full_address = address + "\n" + city + ", " + state + " " + zip

    def get_customerdata(self):
        customers = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                customer = CustomerData((row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                customers.append(customer)
        return customers


FILENAME = 'customers.csv'


def main():
    Title()
    customer = CustomerData()
    customers = customer.get_customerdata()
    choice = "y"
    while choice.lower() == "y":

        custid = input("Enter customer ID: ")

        for i in range(len(customers)):

            if customers[i].custid == custid:
                print(customers[i].full_name)
                if customers[i].company_name != '':
                    print(customers[i].company_name)
                print(customers[i].full_address)

        cus = []
        for i in range(len(customers)):
            cus.append(customers[i].custid)

        if custid not in cus:
            print("\n No customer with this ID")

        choice = input("Continue (y/n) : ")

    print("bye!")


main()












