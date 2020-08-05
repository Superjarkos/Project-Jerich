import pandas as pd
import interface

data = interface.df
#data = pd.ExcelFile(r'C:\Users\us\Desktop\grauation project\Deliveries 12-3-2017.xlsx') 
#data = pd.concat(pd.read_excel('Todays sheet.xlsx', sheet_name=None), ignore_index=True)
#data1 drops all dublicates from sheet 
data1 = data.drop_duplicates(subset=["Ref/Lic Nr"], keep="first")
#data = interface.df 
cr = pd.DataFrame(data1,columns= ['Carrier'])
rf = pd.DataFrame(data1,columns= ['Ref/Lic Nr'])
rsting ='Good morning,\nCan we get updates for: \n'

#Locks data from column 
amtg = data1.loc[data1.Carrier=='AMTG', 'Ref/Lic Nr']
bgxp = data1.loc[data1.Carrier=='BGXP', 'Ref/Lic Nr']
dtcv = data1.loc[data1.Carrier=='DTCV', 'Ref/Lic Nr']
ceeg = data1.loc[data1.Carrier=='CEEG', 'Ref/Lic Nr']
echs = data1.loc[data1.Carrier=='ECHS', 'Ref/Lic Nr']
krlg = data1.loc[data1.Carrier=='KRLG', 'Ref/Lic Nr']
luac = data1.loc[data1.Carrier=='LUAC', 'Ref/Lic Nr']
mode = data1.loc[data1.Carrier=='MODE', 'Ref/Lic Nr']
ntgo = data1.loc[data1.Carrier=='NTGO', 'Ref/Lic Nr']
prcn = data1.loc[data1.Carrier=='PRCN', 'Ref/Lic Nr']
scnn = data1.loc[data1.Carrier=='SCNN', 'Ref/Lic Nr']
tcfp = data1.loc[data1.Carrier=='TCFP', 'Ref/Lic Nr']
todl = data1.loc[data1.Carrier=='TODL', 'Ref/Lic Nr']
wfli = data1.loc[data1.Carrier=='WFLI', 'Ref/Lic Nr']
bthd = data1.loc[data1.Carrier=='BTHD', 'Ref/Lic Nr']
btth = data1.loc[data1.Carrier=='BTTH', 'Ref/Lic Nr']
satn = data1.loc[data1.Carrier=='SATN', 'Ref/Lic Nr']

#  without index
amtg1=(amtg.to_string(index=False, header=False))
bgxp1=(bgxp.to_string(index=False, header=False))
dtcv1=(dtcv.to_string(index=False, header=False))
ceeg1=(ceeg.to_string(index=False, header=False))
echs1=(echs.to_string(index=False, header=False))
krlg1=(krlg.to_string(index=False, header=False))
luac1=(luac.to_string(index=False, header=False))
mode1=(mode.to_string(index=False, header=False))
ntgo1=(ntgo.to_string(index=False, header=False))
prcn1=(prcn.to_string(index=False, header=False))
scnn1=(scnn.to_string(index=False, header=False))
tcfp1=(tcfp.to_string(index=False, header=False))
todl1=(todl.to_string(index=False, header=False))
wfli1=(wfli.to_string(index=False, header=False))
bthd1=(bthd.to_string(index=False, header=False))
btth1=(btth.to_string(index=False, header=False))
satn1=(satn.to_string(index=False, header=False))


