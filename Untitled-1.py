########Employee########
class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, DOB, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.DOB = DOB
        self.passport_details = passport_details

    def display(self):
        return f"Employee Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, Job Title: {self.job_title}, Salary: {self.basic_salary}, Age: {self.age}, DOB: {self.DOB}, Passport: {self.passport_details}"

########Client########
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def get_id(self):
        return self.client_id

    def display(self):
        return f"Client Name: {self.name}, ID: {self.client_id}, Address: {self.address}, Contact Details: {self.contact_details}, Budget: {self.budget}"

########Guest########
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def get_id(self):
        return self.guest_id
    
    def display(self):
        return f"Guest Name: {self.name}, ID: {self.guest_id}, Address: {self.address}, Contact Details: {self.contact_details}"

########Venue########
class Venue:
    def __init__(self, venue_id, name, address, contact, minimum_number_of_guests, maximum_number_of_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.minimum_number_of_guests = minimum_number_of_guests
        self.maximum_number_of_guests = maximum_number_of_guests

    def get_address(self):
        return self.address

    def display(self):
        return f" Venue Name: {self.name}, Venue ID: {self.venue_id}, Address: {self.address}, Contact: {self.contact}, Mninimum Number of Guests: {self.minimum_number_of_guests}, Maximum Number of Guests: {self.maximum_number_of_guests}"

########Supplier########
class Supplier:
    def __init__(self, id, name, address, contact_details, service_menu, minimum_number_of_guests, maximum_number_of_guests, invoice):
        self.id = id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.service_menu = service_menu
        self.minimum_number_of_guests = minimum_number_of_guests
        self.maximum_number_of_guests = maximum_number_of_guests 
        self.invoice = invoice

    def get_id(self):
        return self.id
    
    def display(self):
        return f" Caterer Name: {self.name}, Venue ID: {self.id}, Address: {self.address}, Contact: {self.contact_details}, Mninimum Number of Guests: {self.minimum_number_of_guests}, Maximum Number of Guests: {self.maximum_number_of_guests}, Invoice: {self.invoice}"

########Event########
class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, 
                 cleaning_company, decorations_company, entertainment_company, furniture_supply_company):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration

        #venue
        self.venue_address = venue_address

        #client
        self.client_id = client_id

        #guests
        self.guest_list = guest_list if guest_list is not None else [] #IDs of guests

        #suppliers
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company

    def display(self):
        return f" Event ID: {self.event_id}, Event Type: {self.event_type}, Theme: {self.theme}, Date: {self.date}, Time: {self.time}, Duration: {self.duration}, Venue Address: {self.venue_address}, Client Id: {self.client_id}, Guest List: {self.guest_list}, Catering Company: {self.catering_company}, Cleaning Company: {self.cleaning_company}, Decorations Company: {self.decorations_company}, Entertainment Company: {self.entertainment_company}, Furniture Supply Company: {self.furniture_supply_company}"

########Company########
class Company:
    def __init__(self):
        self.employees = {}
        self.events = {}
        self.clients = {}
        self.suppliers = {}
        self.guests = {}
        self.venues = {}

    #employee
    def add_employee(self, employee):
        self.employees[employee.employee_id] = employee

    def display_employee(self, id):
        if id in self.employees:
            print(self.employees[id].display())
        else:
            print(f"Error!! No employee with id: {id}")

    def delete_employee(self, id):
        if id in self.employees:
            del self.employees[id]
        else:
            print(f"Error!! No employee with id: {id}")

    def modify_employee(self, id, name=None, department=None, job_title=None, basic_salary=None, age=None, DOB=None, passport_details=None):
        if id in self.employees:
            e = self.employees[id]
            if name:
                e.name = name
            if department:
                e.department = department
            if job_title:
                e.job_title = job_title
            if basic_salary:
                e.basic_salary = basic_salary
            if age:
                e.age = age
            if DOB:
                e.DOB = DOB
            if passport_details:
                e.passport_details = passport_details            
        else:
            print(f"Error!! No employee with id: {id}")

    #event
    def add_event(self, event):
        self.events[event.event_id] = event

    def display_event(self, id):
        if id in self.events:
            print(self.events[id].display())
        else:
            print(f"Error!! No event with id: {id}")

    def delete_event(self, id):
        if id in self.events:
            del self.events[id]
        else:
            print(f"Error!! No event with id: {id}")

    def modify_event(self, id, event_type=None, theme=None, date=None, time=None, duration=None, venue_address=None, 
                     client_id=None, guest_list=None, catering_company=None, cleaning_company=None, 
                     decorations_company=None, entertainment_company=None, furniture_supply_company=None):
        if id in self.events:
            event = self.events[id]

            if event_type:
                event.event_type = event_type
            if theme:
                event.theme = theme
            if date:
                event.date = date
            if time:
                event.time = time
            if duration:
                event.duration = duration
            if venue_address:
                event.venue_address = venue_address
            if client_id:
                event.client_id = client_id
            if guest_list:
                event.guest_list = guest_list
            if catering_company:
                event.catering_company = catering_company
            if cleaning_company:
                event.cleaning_company = cleaning_company
            if decorations_company:
                event.decorations_company = decorations_company
            if entertainment_company:
                event.entertainment_company = entertainment_company
            if furniture_supply_company:
                event.furniture_supply_company = furniture_supply_company

        else:
            print(f"Error!! No event with id: {id}")

    #client
    def add_client(self, client):
        self.clients[client.client_id] = client

    def display_client(self, id):
        if id in self.clients:
            print(self.clients[id].display())
        else:
            print(f"Error!! No client with id: {id}")

    def delete_client(self, id):
        if id in self.clients:
            del self.clients[id]
        else:
            print(f"Error!! No client with id: {id}")

    def modify_client(self, id, name=None, address=None, contact_details=None, budget=None):
        if id in self.clients:
            client = self.clients[id]
            if name:
                client.name = name
            if address:
                client.address = address
            if contact_details:
                client.contact_details = contact_details
            if budget:
                client.budget = budget
        else:
            print(f"Error!! No client with ID: {id}")

    #supplier
    def add_supplier(self, supplier):
        self.suppliers[supplier.id] = supplier

    def display_supplier(self, id):
        if id in self.suppliers:
            print(self.suppliers[id].display())
        else:
            print(f"Error!! No supplier with id: {id}")

    def delete_supplier(self, id):
        if id in self.suppliers:
            del self.suppliers[id]
        else:
            print(f"Error!! No supplier with id: {id}")

    def modify_supplier(self, id, name=None, address=None, contact_details=None, menu=None, 
                        minimum_number_of_guests=None, maximum_number_of_guests=None, invoice=None):
        if id in self.suppliers:
            supplier = self.suppliers[id]    

            if name:
                supplier.name = name
            if address:
                supplier.address = address
            if contact_details:
                supplier.contact_details
            if menu:
                supplier.menu
            if minimum_number_of_guests:
                supplier.minimum_number_of_guests
            if maximum_number_of_guests:
                supplier.maximum_number_of_guests
            if invoice:
                supplier.invoice
        else:
            print(f"Error!! No supplier with id: {id}")

    #guest
    def add_guest(self, guest):
        self.guests[guest.guest_id] = guest

    def display_guest(self, id):
        if id in self.guests:
            print(self.guests[id].display())
        else:
            print(f"Error!! No guest with id: {id}")

    def delete_guest(self, id):
        if id in self.guests:
            del self.guests[id]
        else:
            print(f"Error!! No guest with id: {id}")

    def modify_guest(self, id, name=None, address=None, contact_details=None):
        if id in self.guests:
            guest = self.guests[id]
            if name:
                guest.name = name
            if address:
                guest.address = address
            if contact_details:
                guest.contact_details = contact_details
        else:
            print(f"Error!! No guest with ID: {id}")

    #venue
    def add_venue(self, venue):
        self.venues[venue.venue_id] = venue

    def display_venue(self, id):
        if id in self.venues:
            print(self.venues[id].display())
        else:
            print(f"Error!! No venue with id: {id}")

    def delete_venue(self, id):
        if id in self.venues:
            del self.venues[id]
        else:
            print(f"Error!! No venue with id: {id}")

    def modify_venue(self, id, name=None, address=None, contact=None, minimum_number_of_guests=None, maximum_number_of_guests=None):
        if id in self.venues:
            venue = self.venues[id]
            if name:
                venue.name = name
            if address:
                venue.address = address
            if contact:
                venue.contact = contact
            if minimum_number_of_guests:
                venue.minimum_number_of_guests = minimum_number_of_guests
            if maximum_number_of_guests:
                venue.maximum_number_of_guests = maximum_number_of_guests
        else:
            print(f"Error!! No venue with id: {id}")

    #displays
    def display_employees(self):
        print("Employees:")
        for emp_id, employee in self.employees.items():
            print(employee.display())

    def display_clients(self):
        print("Clients:")
        for client_id, client in self.clients.items():
            print(client.display())

    def display_guests(self):
        print("Guests:")
        for guest_id, guest in self.guests.items():
            print(guest.display())

    def display_suppliers(self):
        print("Suppliers:")
        for supplier_id, supplier in self.suppliers.items():
            print(supplier.display())

    def display_events(self):
        print("Events:")
        for event_id, event in self.events.items():
            print(event.display())

    def display_venues(self):
        print("Venues:")
        for venue_id, venue in self.venues.items():
            print(venue.display())



########Test Cases########
#class instances
emp1 = Employee("Ali Ahmad", 1, "HR", "Manager", 50000, 35, "1990-01-01", "ABCD1234")
emp2 = Employee("Jane Smith", 2, "Finance", "Financial Analyst", 50000, 30, "1994-10-20", "EFGH5678")
emp3 = Employee("Hassan Abbasi", 3, "IT", "Software Engineer", 65000, 28, "1996-03-25", "IJKL91011")

client1 = Client(1, "ABC Company", "123 Main St", "123-456-7890", 100000)
client2 = Client(2, "XYZ Corporation", "456 Elm St", "987-654-3210", 75000)

guest1 = Guest(1, "Ahmad Raza", "456 Park Ave", "987-654-3210")
guest2 = Guest(2, "Emily Brown", "321 Pine St", "456-789-0123")
guest3 = Guest(3, "David Lee", "654 Birch St", "789-012-3456")
guest4 = Guest(4, "Sarah Willy", "987 Cedar St", "012-345-6789")

venue1 = Venue(1, "Marquee X", "789 Broadway", "555-444-4565", 90, 100)
venue2 = Venue(2, "Grand Ballroom", "65 Maple Ave", "555-123-4567", 50, 200)

caterer = Supplier(1, "Delicious Caterers", "123 Main Street", "111-222-3333", "Service Menu", 50, 200, "INV001")
cleaner = Supplier(2, "Clean Sweep Services", "456 Park Avenue", "111-222-3333", "Service Menu", 50, 200, "INV002")
decorator = Supplier(3, "Creative Decorators", "789 Elm Road", "111-222-3333", "Service Menu", 50, 200, "INV003")
entertainer = Supplier(4, "Entertainment Galore", "101 Oak Lane", "111-222-3333", "Service Menu", 50, 200, "INV004")
furniture = Supplier(5, "Furniture Plus", "202 Maple Drive", "111-222-3333", "Service Menu", 50, 200, "INV005")

event1 = Event(1, "Wedding", "Romantic", "2024-06-15", "18:00", "4 hours", venue1.get_address(), client1.get_id(), 
               [guest1.get_id(), guest2.get_id(), guest3.get_id(), guest4.get_id()], caterer.get_id(), cleaner.get_id(), 
               decorator.get_id(), entertainer.get_id(), furniture.get_id())

# Create Company instance
company = Company()

#adding everything to the company
company.add_employee(emp1)
company.add_employee(emp2)
company.add_employee(emp3)
company.add_client(client1)
company.add_client(client2)
company.add_guest(guest1)
company.add_guest(guest2)
company.add_guest(guest3)
company.add_guest(guest4)
company.add_venue(venue1)
company.add_venue(venue2)
company.add_supplier(caterer)
company.add_supplier(cleaner)
company.add_supplier(decorator)
company.add_supplier(entertainer)
company.add_supplier(furniture)
company.add_event(event1)

#displaying dictionaries
company.display_employees()
print()
company.display_clients()
print()
company.display_guests()
print()
company.display_venues()
print()
company.display_suppliers()
print()
company.display_events()
print()

#modifying
company.modify_venue(1, name="Marquee Z", maximum_number_of_guests=300)
company.display_venue(1)
print()
company.display_venues()
print()
company.modify_event(1, time="11:00")
company.display_event(1)
print()

#deleting
company.delete_employee(1)
company.display_employees()
print()

#accessing  employee that does not exist
company.display_employee(1)
print()
