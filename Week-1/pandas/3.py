#3-
a=pd.Series(np.random.randint(1,5,[15]))
print(a)
print(a.value_counts())
res=a[~a.isin(a.value_counts().index[:1])]='other'
print(a)