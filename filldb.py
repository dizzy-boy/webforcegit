import mysql.connector
from getpass import getpass

maBaseDeDonne = mysql.connector.connect(
    host = "localhost",
    user = "dizzy",
    password = getpass("{0} veuillez entrez votre mot de passe: ".format("dizzy")),
    database = "webforcedb",
    auth_plugin= "mysql_native_password")

curseur = maBaseDeDonne.cursor()

requete = " SELECT * FROM etudiants"
curseur.execute(requete)
resultat = curseur.fetchall()
print("La table etudiant contient les infos suivantes: ")
print(resultat)

######### PARTIE POUR LE REMPLISSAGE DE LA TABLE #######

Nom = input("Entrer un nom: ")
Age = int(input("Entrer un age: "))
Genre = input("Entrer un Genre: ")
Formation = input("Entrer une Formation: ")

requeteAjout = "INSERT INTO etudiants (Nom,Age, Genre, Formation) VALUES (%s, %s,%s, %s)"
valeurs = (Nom, Age, Genre, Formation)


curseur.execute(requeteAjout, valeurs)
maBaseDeDonne.commit()
print("fin")