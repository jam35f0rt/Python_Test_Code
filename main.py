data ={}
data['medicament'] , data['client']=[] ,[]
class medicament():

    def __init__(self,nom_med,quantite):
        self.nom_medicament = nom_med
        self.quantite_medicament = quantite
    @staticmethod
    def add_med(nom_med,qt_med):
        data['medicament'].append([nom_med,qt_med])
class client():
    def __init__(self,nom_client,)       

def main():
    print("1 : Achat de medicament \n\
2 : Approvisionnement en  medicaments\n\
3 : Etats des stocks et des credits\n\
4 : Quitter\n")
    print(data)
    user = input("\nEntrer votre choix : ")
    while len(user) != 1 or user not in "1234":
        user = input("Entrer un choix valide : ")

    user = int(user)
    
    
    if user == 1:
        print(str(user))
    if user == 2:
        pos =0
        done = False
        nom_medicament = input("\nNom du medicament? ")
        qt_medicament = int(input("Donner la quantite : "))
        donne = medicament(nom_medicament,qt_medicament)
        for drug in data['medicament']:
            
            if donne.nom_medicament in drug:
                data['medicament'][pos][1] = data['medicament'][pos][1] + donne.quantite_medicament
                done = True
            pos +=1
        if not done:
            data['medicament'].append([donne.nom_medicament,donne.quantite_medicament])
        main()
    if user == 3:
        print("Affichage des stocks\n")
        pos=0
        for drug in data["medicament"]:
            anydrug = data["medicament"][pos]
            print("Stock du medicament {} : {}".format(anydrug[0],anydrug[1]))
            pos +=1
        pos=0
        print("\nAffichage des credits\n")
        for client in data["client"]:
            anyclient = data["client"][pos]
            print("Credit du client {} : {}".format(anyclient[0],anyclient[1]))
            pos +=1
        main()
    if user == 4:
        print(str(user))
    print("\n")
main()

