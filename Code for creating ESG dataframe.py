import pandas as pd
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
#ESG
ESG_index_path = 'https://raw.githubusercontent.com/GiammarcoBozzelli/SEF/baltha/ESG_Scores/DS_ESGScore_Y.xlsx'  # Replace with your Excel file name
df_ESG = pd.read_excel(ESG_index_path)

#Country to region data
region_path = 'https://raw.githubusercontent.com/GiammarcoBozzelli/SEF/baltha/CountriesToRegions.xlsx'  # Replace with your Excel file name
df_region = pd.read_excel(region_path)


#let's  keep only the EUR contries

df_region.drop(index=[0,1,2,3], inplace= True )

df_EUR = df_region[df_region['Unnamed: 2'] == 'EUR']

#Rename the column so we can merge later
df_EUR = df_EUR.rename(columns={'% AMER: Cnada + USA' : 'ISIN_First2'})

print(df_EUR)
print(df_ESG)

#Now merged with the two dataset 
#First step we need to create a new columns with only the 2 first caracters of the columns ISIN

df_ESG['ISIN_First2'] = df_ESG['ISIN'].str[:2]
print(df_ESG)


#Second step we merge the data set with the region, keeping only the one watching the EUR countries
df_ESG_Y = pd.merge(df_EUR,  df_ESG, on='ISIN_First2', how='inner')


print(df_ESG_Y)

