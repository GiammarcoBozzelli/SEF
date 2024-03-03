import pandas as pd

#Monthly_reurn include 278 months and 2051 firms (rows)
monthly_return_index_path = '/Users/balthazarduc/Desktop/Github/SEF/ESG_Scores/DS_RI_T_USD_M.xlsx'  # Replace with your Excel file name
df_monthly_return = pd.read_excel(monthly_return_index_path)



#Monthly_capitalization include 278 months and 2051 firms 
monthly_capitalization_path = '/Users/balthazarduc/Desktop/Github/SEF/ESG_Scores/DS_MV_USD_M.xlsx'  # Replace with your Excel file name
df_monthly_capitalization = pd.read_excel(monthly_capitalization_path)



#M ountry to region data
region_path = '/Users/balthazarduc/Desktop/Github/SEF/CountriesToRegions.xlsx'  # Replace with your Excel file name
df_region = pd.read_excel(region_path)


#let's  keep only the EUR contries

df_region.drop(index=[0,1,2,3], inplace= True )

df_EUR = df_region[df_region['Unnamed: 2'] == 'EUR']

#Rename the column so we can merge later
df_EUR = df_EUR.rename(columns={'% AMER: Cnada + USA' : 'ISIN_First2'})

print(df_EUR)


#Now merged with the two dataset 
#First step we need to create a new columns with only the 2 first caracters of the columns ISIN

#First with the return data 

df_monthly_return['ISIN_First2'] = df_monthly_return ['ISIN'].str[:2]
print(df_monthly_return)

#With the capitlization now
df_monthly_capitalization['ISIN_First2'] = df_monthly_capitalization ['ISIN'].str[:2]
print(df_monthly_capitalization )

#Second step we merge the data set with the region, keeping only the one watching the EUR countries
df_EUR_monthly_capitalization = pd.merge(df_EUR,  df_monthly_capitalization, on='ISIN_First2', how='inner')
df_EUR_monthly_return = pd.merge(df_EUR,  df_monthly_return, on='ISIN_First2', how='inner')

print(df_EUR_monthly_capitalization)
print(df_EUR_monthly_return)

df_EUR_monthly_capitalization.to_csv('/Users/balthazarduc/Desktop/Finance/df_EUR_monthly_capitalization.csv', index=False)
df_EUR_monthly_return.to_csv('/Users/balthazarduc/Desktop/Finance/df_EUR_monthly_return.csv', index=False)
#We have now 508 firms with the data for 281 months