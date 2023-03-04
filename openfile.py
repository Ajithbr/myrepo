import pandas as pd
xl = pd.ExcelFile(path + filename)
xl.sheet_names

>>> [u'Sheet1', u'Sheet2', u'Sheet3']

df = xl.parse("Sheet1")
df.head()
print ("git pull master")
