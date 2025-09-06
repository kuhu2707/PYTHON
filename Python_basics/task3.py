#TASK 3 - LOAD A CSV FILE WITH PANDAS , CLEAN IT(HANDLE MISSING VALUES ) AND EXPORT A SUMMARY

#%%
import pandas as pd

# %%
housing = pd.read_csv(r"C:\Users\ASUS\Downloads\archive (5)\housing.csv")

# %%
housing
# %%
housing.head()
# %%
housing.info()

housing.tail()
# %%
housing.describe
# %%
house = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\book.csv")
# %%
house
# %%
import math
# %%
median_bedroom = math.floor(house.bedrooms.median())
# %%
median_bedroom
# %%
house.bedrooms.fillna(median_bedroom)
# %%
summary=house.describe()
# %%
summary.to_csv("summary.csv")
# %%
summary
# %%

# %%
