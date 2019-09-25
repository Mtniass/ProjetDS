import pandas as pd
donnees = pd.read_excel("ProjetDATASCIENCE.xlsx")
ages = donnees["Age"].apply(pd.to_numeric)
donnees.Age = ages
agesplus20ans = donnees[donnees["Age"] >20]
agesplus20ans.to_excel("agesplus20ans.xlsx")