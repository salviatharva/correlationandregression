import pandas as pd

phy = list(map(int,input().split()))
his = list(map(int,input().split()))

x=pd.Series(phy)
y=pd.Series(his)

r=x.cov(y)/(x.std()*y.std())
print(round(r,3))
