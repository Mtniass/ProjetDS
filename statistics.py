import pandas as pd
donnees = pd.read_excel("ProjetDATASCIENCE.xlsx")
moyenneEcole = donnees["Moyenne"].sum()/(len(donnees))
pourcentageFille = (len(donnees[donnees["Sexe"]=="F"])/len(donnees))*100
pourcentageGarcon = (len(donnees[donnees["Sexe"]=="M"])/len(donnees))*100
regionPlusforte = donnees[donnees["Moyenne"]==donnees["Moyenne"].max()]
regionPlusforteM = regionPlusforte["Region"]
data=[[moyenneEcole,pourcentageFille,pourcentageGarcon,regionPlusforteM]]
statistics = pd.DataFrame(data,columns=["moyenneEcole","pourcentageFille","pourcentageGarcon","regionPlusforte"])
statistics.to_excel("statistics.xlsx")