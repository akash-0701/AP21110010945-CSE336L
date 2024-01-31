#1-
import pandas as pd
import numpy as np
a=pd.Series([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a)
a=a.apply(pd.Series).stack().reset_index(drop=True)
print(a)