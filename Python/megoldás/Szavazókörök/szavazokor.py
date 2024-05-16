class Szavazokor:
    def __init__(self, row):
        data = row.strip().split(';') #Vármegye;Település;Cím;Típus;Akadálymentesség;Választópolgárok száma
        self.varmegye = data[0]
        self.telepules = data[1]
        self.cim = data[2]
        self.tipus = data[3]
        self.akadalymentesseg = data[4]
        self.valasztokszama = int(data[5])
