import pandas as pd
import numpy as np
import shutil
import os

i = 1 #選擇部位
t = 1 #選擇左右

db =['ankle','elbow','foot','knee','wrist']
data = db[i]
turn = ['left','right']
LR = turn[t]

#path ="/home/mio/image/limbXray/"+ LR + "_" + data + "_deid/"
path = "/Users/mio/Documents/YM_ciflab/Image/Xray/"+LR+"_"+data+"_deid/"
count = 0
for fn in os.listdir(path):  #查看底下有幾層資料夾
        count = count+1

df = pd.read_csv('imgdb_limb_deid.csv',encoding='big5') 
df['bol'] = df["急診最後診斷"].str.lower().str.contains("fracture")
for x in range(len(db)):
    imt = df.loc[(df['label'] == str(db[x])) & (df['bol'] == True) , ['imageID','bol','年齡','急診最後診斷']]
    imt.to_csv(str(db[x])+'_out'+'.csv')

img = pd.read_csv(data + '_out.csv',encoding='big5')
lenIMG = len(img.imageID)
cou = (count)
print(cou)

for m in range(1,int(cou)):
    adr = "/Users/mio/Documents/YM_ciflab/Image/Xray/"+LR+"_"+data+"_deid/"+LR+"_"+data+"_deid_part"+str(m)+"/"
    ##print(adr)
    dd = os.path.exists( adr + "True")####
    ##print(dd)
    if dd == False:###
        os.mkdir(adr + 'True')#

for y in range(1,int(cou)):###這裡要查看資料夾有多少個資料夾###
    adrr = "/Users/mio/Documents/YM_ciflab/Image/Xray/"+LR+"_"+data+"_deid/"+LR+"_"+data+"_deid_part"+str(y)+"/" 
    ##print(adrr)
    for i in range(lenIMG):
        #///查看是否有＝True的Image存在;///
        for g in range(1,3):
            tt = os.path.exists( adrr + LR +data+"_"+str(img.imageID[i])+"_0"+str(g)+".png")
            #///如果＝True 代表資料夾有這筆檔案存在 並移動到我要的資料夾內;///
            #print(tt)
            if tt == True:
            #/// d 為資料存放的位置;///
                d = adrr + LR +data+"_"+str(img.imageID[i])+"_0"+str(g)+".png"
                #/// b 為要移動到的地方;///
                b =  adrr + "True"
                shutil.copy( d , b )
