# Use Pandas to Classification what Data we Want

## To know how to read the csv data in python ##

>>### Study use Python Pandas ###

```python
#this project will use 
import pandas as pd
import numpy as np
import shutil
import os
```

>>### Start to read csv ###

```python
csv = 'imgdb_limb_deid.csv' #your data name

df = pd.read_csv( csv ,encoding='big5') 
#you can try to print it out to see 
print(df)
```
