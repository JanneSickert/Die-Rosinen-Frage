from random import randint
anzahlBrot = 10
print("Wertetabelle wird erstellt.")
class Ofen:
    def __init__(self, anzBrot, anzRosinen):
        self.anzBrot = anzBrot
        self.anzRosinen = anzRosinen
        self.brot = []
    def backeBrot(self):
        i = 0
        while i < self.anzBrot:
            self.brot.append(0)
            i = i + 1
        k = 0
        while k < self.anzRosinen:
            randomNr = randint(0, (self.anzBrot - 1))
            self.brot[randomNr] = self.brot[randomNr] + 1
            k = k + 1
        return self.brot
def jedesBrotHatminEine(brotArr):
    i = 0
    result = 0
    ret = 0
    while i < len(brotArr):
        if brotArr[i] > 0:
            result = result + 1
        i = i + 1
    if result == len(brotArr):
        ret = 1
    return ret
def makeAVG(zeroOrOneArr):
    zz = 0
    erg = 0
    while zz < len(zeroOrOneArr):
        erg = erg + zeroOrOneArr[zz]
        zz = zz + 1
    avg = erg / len(zeroOrOneArr)
    return avg
def derVersuch(x):
    anzVersuche = 10000
    versuche = []
    i = 0
    while i < anzVersuche:
        versuche.append(Ofen(anzahlBrot, x))
        i = i + 1
    zeroOrOne = []
    i = 0
    while i < anzVersuche:
        zeroOrOne.append(jedesBrotHatminEine(versuche[i].backeBrot()))
        i = i + 1
    avg = makeAVG(zeroOrOne)
    return avg
startValue = (20)
resultArr = []
rosinen = 20
anzDurchlaufe = 150
while rosinen <= anzDurchlaufe:
    resultArr.append(derVersuch(rosinen))
    rosinen = rosinen + 1
i = startValue
print("Anzahl Brot : Rosinen : Prozentualer Anteil aller Durchläufe in dem Jedes Brot mindestens eine Rosine hat")
d = " : "
while i <= anzDurchlaufe:
    brote = str(anzahlBrot)
    index = str(i)
    value = str(resultArr[i - startValue] * 100) + "%"
    print(brote + d + index + d + value)
    i = i + 1
un = input("Druecke ENTER um das Programm zu beenden.")