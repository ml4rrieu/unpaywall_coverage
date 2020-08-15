import matplotlib.pyplot as plt
import pandas as pd


## print value
df = pd.read_csv("scopus_upw_hal.csv")
print(f"publications {len(df)}")
print(f"publications oa w upw {len(df.loc[df['is_oa'] == 1])}")
oa_upw_plus_hal = len(df.loc[df['is_oa'] == 1]) + len(df.loc[df['notoa_in_upw_but_in_hal'] == 1])

perYear = [ len( df.loc[ df['Year'] == float(y)] ) for y in range(2014, 2018)]
print("total per year", perYear)

largeOA = [len(
df.loc[ (df['Year'] == float(y)) & (df['is_oa'] == 1.0) ]
) for y in range(2014, 2018) ]
print("oa from upw", str(largeOA))

closed = [len(
df.loc[ (df['Year'] == float(y)) & (df['is_oa'] == 0.0) & (pd.isna(df['pb']))]
)for y in range(2014, 2018)]
print("closed pub", closed)

noDois = [len(
df.loc[ (df['Year'] == float(y)) & (pd.isna(df['DOI']) ) ]
) for y in range(2014, 2018) ]
print('no dois', noDois)

doisNotInUpw = [len(
df.loc[ (df['Year'] == float(y)) & (df['pb'] == 'not in upw') ]
) for y in range(2014, 2018) ]
print('dois not in upw', doisNotInUpw)


#verif classification
[print(sum(x)) for x in zip(largeOA, closed, noDois, doisNotInUpw)]

years = [str(y) for y in range(2014,2018)]
plt.figure(figsize=(13,7))
plt.bar(years, largeOA, color='#00bcd4', label="publications are OA from unpaywall") 
plt.bar(years, closed, bottom=largeOA ,color='#F5F5F5', label="publication are closed from unpaywall") 
plt.bar(years, doisNotInUpw, bottom= [sum(x) for x in zip(largeOA,closed)] ,color='#ff5722', label="publications have DOI but isn't in unpaywall")
plt.bar(years, noDois, bottom = [sum(x) for x in zip(largeOA, closed, doisNotInUpw)], color='#ffc622', label="publications have no DOI")

plt.legend(loc = "center")
plt.title("Limits of Unpaywall for the publications of Versailles University identified in Scopus", size=17)
plt.show()
