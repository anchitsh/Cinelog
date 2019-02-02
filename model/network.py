import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as pl
from new import temp_function

#movie = pd.read_csv('./ml-20m/movies.csv', sep=",", header=1)
#ratings = pd.read_csv('./ml-20m/ratings.csv', sep=",", header=1)

week = pd.read_csv('./ml-20m/moviedaily.dat.txt', sep="\t")

#create unique list of names
UniqueNames = week.MOVIE.unique()

#create a data frame dictionary to store your data frames
DataFrameDict = {elem : pd.DataFrame for elem in UniqueNames}

for key in DataFrameDict.keys():
	DataFrameDict[key] = week[:][week.MOVIE == key]

keys = []

for key in DataFrameDict.keys():
	keys.append(key)

net = [DataFrameDict[keys[1]].DAILY_PER_THEATER]

net = pd.concat(net, axis = 1).reset_index(drop=True)

temp_function(net)


#for g in range(0, len(key)):
	#DataFrameDict[keys[g]]

	#pl.plot(DataFrameDict[keys[g]].DAY_NUM , DataFrameDict[keys[g]].DAILY_PER_THEATER)

	#pl.show()
