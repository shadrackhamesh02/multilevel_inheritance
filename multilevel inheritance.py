# Multilevel inheritance

class parent:
    def getparentdetials(self):
        self.name = input("Enter name: ")
        self.number = input("Enter number:")

class educational(parent):
    def geteducationaldetials(self):
        self.passedoutyear = input('Enter passed out year: ')

class professional(educational):
    def getprofessionaldetials(self):
        self.companyname = input('Enter company name: ')
        self.designation = input("Enter designation: ")

class records(professional):
    def displaydetials(self):
        print("---------Records--------")
        print("Name              :", self.name)
        print("Number            :", self.number)
        print("Passed out year   :", self.passedoutyear)
        print("Company name      :", self.companyname)
        print("Designation       :", self.designation)
        print("---------Thank you--------")


obj = records()
obj.getparentdetials()
obj.geteducationaldetials()
obj.getprofessionaldetials()
obj.displaydetials()