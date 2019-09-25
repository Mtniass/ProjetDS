import pandas as pd
donnees = pd.read_excel("ProjetDATASCIENCE.xlsx")
moyennes = donnees[donnees["Moyenne"] >=10]
moyennes.to_excel("moyennes.xlsx")