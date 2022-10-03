import random, os

import config as cfg
from rich.console import Console

console = Console()


class FakeIdentity:
    
    def __init__(self, fullname=None, age=None, gender=None, phone_number=None, email=None, adress=None):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.adress = adress
    
    def generate_name(self, forcegender=None):
        if cfg.config["language"] == "en":
            """
            This part determines the first name and wheter the identity is
            male or female.
            """
            if random.randint(0, 1) == 0 or forcegender == 0:
                self.gender = "Male"
                with open("assets/namelists/en/male_names.txt", "r") as f:
                    namelist = []
                    for i in f.readlines():
                        namelist.append(i[:-1])
            else:
                self.gender = "Female"
                with open("assets/namelists/en/female_names.txt", "r") as f:
                    namelist = []
                    for i in f.readlines():
                        namelist.append(i[:-1])

            """
            This part determines the last name of the identity.
            """
            with open("assets/namelists/en/surnames.txt", "r") as f:
                surnamelist = []
                for i in f.readlines():
                    surnamelist.append((i[:-1]).lower().title())

            self.fullname = f"{random.choice(namelist)} {random.choice(surnamelist)}"

    def generate_age(self):
        self.age = random.randint(18, 80)
    
    def generate_email(self):
        if self.fullname != None:
            connector = ["-", "_", "."]
            self.email = f"{self.fullname.lower().replace(' ', f'{random.choice(connector)}')}{random.randint(0, 99)}@gmail.com"
        else:
            self.generate_name()
            self.generate_email()
    
    def generate_phone_number(self):
        if cfg.config["language"] == "en":
            self.phone_number = f"+1 {random.randint(100, 999)} {random.randint(100, 999)} {random.randint(1000, 9999)}"

    def generate_adress(self):
        with open("assets/namelists/en/adresses.txt", "r") as f:
            adresslist = []
            for i in f.readlines():
                adresslist.append(i[:-1])    
            self.adress = random.choice(adresslist)    


    def prettify(self):
        console.print(f"""
        [bold yellow]Random Data Generated[/]
        [black]---------------------[/]
        [red italic]Fullname:[/] [bold cyan]{self.fullname}[/] 
        [red italic]Age:[/] [bold cyan]{self.age}[/]
        [red italic]Phone Number:[/] [bold gray]{str(self.phone_number)}[/]
        [red italic]Email:[/] [bold cyan]{self.email}[/]
        [red italic]Adress:[/] [bold cyan]{self.adress}[/]

        """)

    def __str__(self):
        return (f'''
Fullname: {self.fullname}
Age: {self.age}
Gender: {self.gender}
Phone Number: {self.phone_number}
Email: {self.email}
Adress: {self.adress}
        ''')

a = FakeIdentity()
a.generate_name()
a.generate_age()
a.generate_email()
a.generate_phone_number()   
a.generate_adress()  
a.prettify()