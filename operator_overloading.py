class Vault:
    def __init_(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    def __add__(self, other):
        galleons = self


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(100, 50, 25)
print(weasley)
