# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:13:15 2020

@author: Sardor Mirzaev
"""
import os
import pyodbc
import pandas as pd

username1 = '006'
password1 = 'Vrl'
                     
#  Databank Connection  
#s = 'Driver={SQL Server};DSN=ZDA;Description=ZDA;UID='+username1+';PWD='+password1
s = 'DSN=ZDA;UID='+username1+';PWD='+password1

cnxn2 = pyodbc.connect(s)#+';DATABASE=ZDA_006000;SCHEMA=dbo')
cursor = cnxn2.cursor()


#%%  

t2 = pd.read_sql("select CAST(RAT_CREATION_DATE as DATE) xxNEU, * from dbo.RATING where RATING_ID = '7990007800'", cnxn2)   
t2.to_clipboard(decimal =',')
# %%
t2 = pd.read_sql("select CAST(RAT_CREATION_DATE as DATE) RAT_CREATION_DATE from dbo.RATING where RATING_ID = '7990007827'", cnxn2)   
t2.to_clipboard(decimal =',')

# %%
sZDA = """SELECT 
'6000'            as X01_Mandant_ID ,
CUST_ID           as X02_CUST_ID,
MODUL_ID          as X03a_MODUL_ID,
MODUL_ID_FUNC     as X03b_MODUL_ID_FUNC,
SUBMODUL          as X03c_SUBMODUL,
RAT_BUS_ID        as X04_RAT_BUS_ID,
'2017_12'         as X05_Stichtag,
RAT_SCORE_INT     as X07_FCR_Stufe_ST1,	
RAT_APPROVE_DATE  as X08_ST1_RAT_APPROVE_DATE, 
OVERRIDE_FLAG     as X14_Overrides, 
RAT_APPROVE_DATE  as Y01_RAT_APPROVE_DATE,
RAT_CLEAR_DATE    as Y02_RAT_CLEAR_DATE,
TECH_RATING_ID    as Y03_TECH_RATING_ID,
RAT_MAN_INAKTIV   as Y04_RAT_MAN_INAKTIV
FROM dbo.RATING 
where MODUL_ID in (10298, 10299, 10303, 10304, 10305, 10306, 10307, 17596, 48342, 58703, 65911, 66170, 70596, 72216, 76249, 79042)
""" + \
"order by RAT_APPROVE_DATE"  


t3 = pd.read_sql(sZDA, cnxn2)

# %%

diff1 = set( t2.Y03_TECH_RATING_ID ).difference( t3.Y03_TECH_RATING_ID  )

t2.Y03_TECH_RATING_ID.min()
t3.Y03_TECH_RATING_ID.min()


t2.Y03_TECH_RATING_ID.max()
t3.Y03_TECH_RATING_ID.max()


# %%
merged1 = pd.merge(t2[['Y03_TECH_RATING_ID', 'X02_CUST_ID', 'Y01_RAT_APPROVE_DATE']], 
                   t3[['Y03_TECH_RATING_ID', 'X02_CUST_ID', 'Y01_RAT_APPROVE_DATE']], how = 'outer', 
                      left_on = 'Y03_TECH_RATING_ID', right_on = 'Y03_TECH_RATING_ID')
merged1.to_clipboard(decimal =',')


# => The not-approved Ratings left out in ZDA