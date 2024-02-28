# SEF
Sustainable and entrepreneurial finance

Data information:

To find the list of firms that you will study, download the Data_Excel folder and either in the ESG_scores folder if your group studies ESG scores and in the Carbon_Emissions folder if your group studies CO2 emissions. Then you can restrict to the list of firms based on the country of interest of your group (using the ISIN you can identify the firm’s country) or sector (information related to the sector of each firm is available in the Static_Score or Static_Carbon excel files)

Datastream (Refinitiv): Financial data
-	DS_RI_T_USD_M: Total return index (price including dividends) from 31/12/1999 to 31/12/2022 at the monthly frequency in USD
-	DS_MV_USD_M: Market capitalization from 31/12/1999 to 31/12/2022 at the monthly frequency in million USD (can be used to compute value weights for the value-weighted benchmark)
-	DS_RI_T_USD_Y: Total return index (price including dividends) from 31/12/1999 to 31/12/2022 at the annual frequency in USD
-	DS_MV_USD_Y Market capitalization from 31/12/1999 to 31/12/2022 at the annua frequency in million USD (can be used to compute value weights for the value-weighted benchmark)

Trucost: Carbon emissions data
-	Static: Company name, ISIN, Sector Country, Region
-	TC_Scope1, TC_Scope2, TC_Scope3, TC_Scope1Intensity, TC_Scope2Intensity, TC_Scope3Intensity, TC_Revenue

Carbon intensity: measure of carbon emissions (Scope1, Scope2, Scope3) normalized by revenues. 

Refinitiv: ESG data
-	Static: Company name, ISIN, Sector Country, Region

-	ESG scores : DS_ESGScore_Y, DS_EScore_Y, DS_SScore_Y, DS_GScore_Y 
