

#Admin(campus)
'''
 • Log in to the system with administrator privileges.
 • Add, update, and remove campus resources using appropriate data structures.
 • View all bookings associated with their campus.
 • Monitor resource availability and usage trends.
'''

#Lecturer
'''
 • Register an account and log into the system using a GUI-based login interface.
 • Select a campus and view available resources stored using dictionaries or lists.
 • Create a booking for a selected resource, date, and time.
 • View their personal booking history retrieved from the database.
'''
class Lecturer():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.role = "Lecture"

    def CreateAccount(self):
        self.username = input('Please ENTER your username: \n')
        self.password = input('Enter your password')

    def ViewResources(campus):
        resources = LgetResources(campus.id)#retrieve from database

        for resource in resources:
            print(resource)




#Operator
'''• Log in to the system with full access rights. 
   • View booking and resource data across all campuses.
   • Generate comparative reports across campuses.
   '''