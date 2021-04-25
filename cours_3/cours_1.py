annuaire = {
    "Alice": {
                "e":"alice@gmail.com" ,
                "t" : "093883273"
    }  ,
    "Bob" :  {
                "e":"bob@gmail.com" ,
                "t" : "073899273"
    } ,
    "Franck" :  {
                "e":"Franck@gmail.com" ,
                "t" : "073899273"
    } ,
    "Mael" :  {
                "e":"mael@gmail.com" ,
                "t" : "073899273"
    }
}
nom = input("Nom: ")
if nom in annuaire:
    req = input("Email (e) ou le numéro de telephone (t)")
    if req in annuaire[nom]:#["e","t"]:
        print(annuaire[nom][req])
    else:
        print("Requete invalide")
else:
    print("Aucun contact!")