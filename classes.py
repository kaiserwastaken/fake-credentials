import random, os
from rich.console import Console
from datetime import datetime


#local imports
import config as cfg
import get_faces as face

#declarations
console = Console()


class FakeIdentity:
    
    def __init__(self, fullname=None, age=None, gender=None, phone_number=None, email=None, adress=None):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.adress = adress
    
    def generate_all(self):
        self.generate_name()
        self.generate_age()
        self.generate_email()
        self.generate_phone_number()   
        self.generate_adress()
        self.generate_misc()
        self.generate_credit_card()

    def generate_name(self, forcegender=None):
        if cfg.config["language"] == "en":
            """
            This part determines the first name and wheter the identity is
            male or female.
            """


            def female_name():
                global namelist
                self.gender = "Female"
                self.title = random.choice(["Ms.", "Mrs.", "Miss", "Dr.", "Prof."])
                with open("assets/namelists/en/female_names.txt", "r") as f:
                    namelist = []
                    for i in f.readlines():
                        namelist.append(i[:-1])
                return f"{random.choice(namelist)}"
            
            def male_name():
                global namelist
                self.gender = "Male"
                self.title = random.choice(["Mr.", "Dr.", "Prof.", "Sir."])
                with open("assets/namelists/en/male_names.txt", "r") as f:
                    namelist = []
                    for i in f.readlines():
                        namelist.append(i[:-1])
                return f"{random.choice(namelist)}"
            if random.randint(0, 1) == 0 or forcegender == 0:
                male_name()
            else:
                female_name()

            """
            This part determines the last name of the identity.
            """
            with open("assets/namelists/en/surnames.txt", "r") as f:
                surnamelist = []
                for i in f.readlines():
                    surnamelist.append((i[:-1]).lower().title())
            
            #Mothers Maiden Name
            with open("assets/namelists/en/female_names.txt", "r") as f:
                maidenlist = []
                for i in f.readlines():
                    maidenlist.append(i[:-1]) 
                self.maiden_name = random.choice(maidenlist)

            self.mothers_name = female_name()
            self.fathers_name = male_name()
            self.fullname = f"{random.choice(namelist)} {random.choice(surnamelist)}"

    def generate_age(self):
        self.age = random.randint(18, 80)
        self.birthday = f"{(random.randint(0,30))}.{(random.randint(1,12))}.{datetime.now().year - self.age}"
    
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
            self.zipcode = f"{random.randint(10000, 99999)}"

    def generate_misc(self):
        """
        This generates a bunch of misc. data like weight, age, birthday etc.
        """

        self.blood_type = random.choice(["A-", "B-", "AB-", "O-", "A+", "B+", "AB+", "O+"])
        self.weight = f"{random.randint(50, 110)} KG"
        self.height = f"{random.randint(160, 200)} CM"
        self.marital_status = random.choice(["Single", "Married", "Divorced", "Widowed"])
        self.race = random.choice(["White", "Black", "Asian", "Hispanic", "Middle-Eastern", "Other"])
        self.ssn = f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
        monthlyincome = random.randint(2000, 10000)
        self.income = f"Monthly:{monthlyincome}$, Hourly: {int(monthlyincome/(8*30) + 1)}$"
        with open("assets/namelists/en/music_groups.txt", "r") as f:
            groupslist = []
            for i in f.readlines():
                groupslist.append(i[:-1])
            self.favorite_music_group = random.choice(groupslist)
    def generate_credit_card(self): #This card can bypass credit card validation algorithms
        self.credit_card =f"NUM: 4007000000027 CVV: {random.randint(100, 999)} EXP: {random.randint(1, 12)}/{random.randint(21, 30)}"      
    
    def prettyprint(self):
        console.print(f"""
        [bold yellow]Random Data Generated[/]
        [black]---------------------[/]
        [red italic]Fullname:[/] [bold cyan]{self.fullname} ({self.title})[/] 
        [red italic]Gender:[/] [bold cyan]{self.gender}[/] 
        [red italic]Age:[/] [bold cyan]{self.age}[/]
        [red italic]Birthday:[/] [bold cyan]{self.birthday}[/]
        [red italic]Phone Number:[/] [bold gray]{str(self.phone_number)}[/]
        [red italic]Email:[/] [bold cyan]{self.email}[/]
        [red italic]Adress:[/] [bold cyan]{self.adress}, ZIP: {self.zipcode}[/]

        [red italic]Social Security No:[/] [bold cyan]{self.ssn}[/]
        [red italic]Marital Status:[/] [bold cyan]{self.marital_status}[/]
        [red italic]Blood Type:[/] [bold cyan]{self.blood_type}[/]
        [red italic]Race:[/] [bold cyan]{self.race}[/]
        [red italic]Weight:[/] [bold cyan]{self.weight}[/]
        [red italic]Height:[/] [bold cyan]{self.height}[/]
        [red italic]CreditCard:[/] [bold cyan]{self.credit_card}[/]
        [red italic]Mother's Name:[/] [bold cyan]{self.mothers_name}[/]
        [red italic]Father's Name:[/] [bold cyan]{self.fathers_name}[/]
        [red italic]Mother's Maiden Name:[/] [bold cyan]{self.maiden_name}[/]
        [red italic]Income:[/] [bold cyan]{self.income}[/]
        [red italic]Favorite Musical Artist:[/] [bold cyan]{self.favorite_music_group}[/]
        
        [red italic]Image:[/] [bold cyan italic]Type "i" to generate a random face.[/]
        """)

    def return_dict(self):
        return {
            "fullname": self.fullname,
            "gender": self.gender,
            "age": self.age,
            "birthday": self.birthday,
            "phone_number": self.phone_number,
            "email": self.email,
            "adress": self.adress,
            "zipcode": self.zipcode,
            "ssn": self.ssn,
            "marital_status": self.marital_status,
            "blood_type": self.blood_type,
            "credit_card": self.credit_card,
            "height": self.height,
            "weight": self.weight,
            "father_name": self.fathers_name,
            "mother_name": self.mothers_name,
            "maiden_name": self.maiden_name,
            "income": self.income,
            "favorite_music_group": self.favorite_music_group,
            "race": self.race,
            "adress": self.adress,
        }
#Made by Kãiser
