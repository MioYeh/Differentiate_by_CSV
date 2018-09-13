# Differentiate_by_CSV

### To know how to read the csv data in python ###

>>#### Study use Python Pandas ####
```python
import pandas as pd
db =['ankle','elbow','foot','knee','wrist']
data = db[i]
turn = ['left','right']
LR = turn[t]
path = "/Users/mio/Documents/YM_ciflab/Image/Xray/"+LR+"_"+data+"_deid/" #this is where you put your data
count = 0
for fn in os.listdir(path):  #to check how many folders under
        count = count+1
df = pd.read_csv('imgdb_limb_deid.csv',encoding='big5') 
```
