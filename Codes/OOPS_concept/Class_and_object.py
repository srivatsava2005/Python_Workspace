class Shinigami:
   
    def __init__(self, name, division, zanpakuto):
        self.name = name
        self.division = division
        self.zanpakuto = zanpakuto

   
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Division: {self.division}")
        print(f"Zanpakutō: {self.zanpakuto}")

  
    def attack(self):
        print(f"{self.name} attacks using {self.zanpakuto}!")

# Creating objects (characters)
ichigo = Shinigami("Ichigo Kurosaki", "Substitute Shinigami", "Zangetsu")
byakuya = Shinigami("Byakuya Kuchiki", "6th Division", "Senbonzakura")

# Accessing methods using objects
ichigo.display_info()
ichigo.attack()

print()

byakuya.display_info()
byakuya.attack()