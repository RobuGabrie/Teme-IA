import pandas as pd
import seaborn as sns

tips = sns.load_dataset("tips")

print("Dimensiune dataset:", tips.shape)
print("\nTipuri de date:")
print(tips.dtypes)
print("\nStatistici descriptive:")
print(tips.describe(include="all"))

tip_mediu_zi_sex = tips.groupby(["day", "sex"]).mean(numeric_only=True)["tip"]
print("\nBacsis mediu per zi si sex:")
print(tip_mediu_zi_sex)

tips_copy = tips.copy()
tips_copy["procent_bacsis"] = tips_copy["tip"] / tips_copy["total_bill"] * 100

print("\nPrimele 5 randuri cu coloana procent_bacsis:")
print(tips_copy.head())

cele_mai_generoase_5 = tips_copy.nlargest(5, "procent_bacsis")[
    ["total_bill", "tip", "procent_bacsis", "day", "sex", "smoker", "time"]
]
print("\nCele mai generoase 5 mese (dupa procent_bacsis):")
print(cele_mai_generoase_5)

mese_per_zi_si_fumator = tips.groupby(["day", "smoker"]).size().reset_index(name="numar_mese")
print("\nNumar mese per zi si categorie fumatori:")
print(mese_per_zi_si_fumator)
