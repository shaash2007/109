import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()
height_mean=statistics.mean(height_list)
height_median=statistics.median(height_list)
height_mode=statistics.mode(height_list)
height_std=statistics.stdev(height_list)
print("mean,median,mode of height is {},{} and {} respectively".format(height_mean,height_median,height_mode))

first_std_deviation_start,first_std_deviation_end=height_mean-height_std,height_mean+height_std
second_std_deviation_start,second_std_deviation_end=height_mean-(2*height_std),height_mean+(2*height_std)
third_std_deviation_start,third_std_deviation_end=height_mean-(3*height_std),height_mean+(3*height_std)

listOfData_withind_first_std_deviation=[result for result in height_list if result>first_std_deviation_start and result<first_std_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(listOfData_withind_first_std_deviation)*100.0/len(height_list)))

listOfData_withind_second_std_deviation=[result for result in height_list if result>second_std_deviation_start and result<second_std_deviation_end]
print("{}% of data lies within 2 standard deviation".format(len(listOfData_withind_second_std_deviation)*100.0/len(height_list)))

listOfData_withind_third_std_deviation=[result for result in height_list if result>third_std_deviation_start and result<third_std_deviation_end]
print("{}% of data lies within 3 standard deviation".format(len(listOfData_withind_third_std_deviation)*100.0/len(height_list)))





#fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["weight"],show_hist=False)
#fig=ff.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist=False)
#fig.show()