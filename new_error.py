#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('error1.csv')

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataset['label'] = le.fit_transform(dataset['label'])

from sklearn.metrics import mean_absolute_percentage_error


f_error_max = list()
f_error_min = list()
f_error_avg = list()
f_error_std = list()
f_error_max_piat = list()
f_error_min_piat = list()
f_error_avg_piat = list()
f_error_std_piat = list()
b_error_max = list()
b_error_min = list()
b_error_avg = list()
b_error_std = list()
b_error_max_piat = list()
b_error_min_piat = list()
b_error_avg_piat = list()
b_error_std_piat = list()

for i in range(141):
    fapp = dataset.loc[dataset['label'] == i, 
                         ['orig_f_min_ps', 'orig_f_max_ps','orig_f_avg_ps',
                          'orig_f_std_dev_ps', 'orig_f_min_piat', 'orig_f_max_piat',
                          'orig_f_avg_piat', 'orig_f_std_dev_piat', 'gen_f_min_ps',
                          'gen_f_max_ps', 'gen_f_avg_ps', 'gen_f_std_dev_ps','gen_f_min_piat',
                          'gen_f_max_piat', 'gen_f_avg_piat', 'gen_f_std_dev_piat']]
    
    bapp = dataset.loc[dataset['label'] == i, 
                         ['orig_b_min_ps', 'orig_b_max_ps','orig_b_avg_ps',
                          'orig_b_std_dev_ps', 'orig_b_min_piat', 'orig_b_max_piat',
                          'orig_b_avg_piat', 'orig_b_std_dev_piat', 'gen_b_min_ps',
                          'gen_b_max_ps', 'gen_b_avg_ps', 'gen_b_std_dev_ps','gen_b_min_piat',
                          'gen_b_max_piat', 'gen_b_avg_piat', 'gen_b_std_dev_piat']]
    
    ferror_min = mean_absolute_percentage_error(fapp.iloc[:, 0:1].values, fapp.iloc[:, 8:9].values)
    ferror_max = mean_absolute_percentage_error(fapp.iloc[:, 1:2].values, fapp.iloc[:, 9:10].values)
    ferror_avg = mean_absolute_percentage_error(fapp.iloc[:, 2:3].values, fapp.iloc[:, 10:11].values)
    ferror_std = mean_absolute_percentage_error(fapp.iloc[:, 3:4].values, fapp.iloc[:, 11:12].values)
    ferror_min_piat = mean_absolute_percentage_error(fapp.iloc[:, 4:5].values, fapp.iloc[:, 12:13].values)
    ferror_max_piat = mean_absolute_percentage_error(fapp.iloc[:, 5:6].values, fapp.iloc[:, 13:14].values)
    ferror_avg_piat = mean_absolute_percentage_error(fapp.iloc[:, 6:7].values, fapp.iloc[:, 14:15].values)
    ferror_std_piat = mean_absolute_percentage_error(fapp.iloc[:, 7:8].values, fapp.iloc[:, -1].values)
    f_error_min.append(ferror_min)
    f_error_max.append(ferror_max)
    f_error_avg.append(ferror_avg)
    f_error_std.append(ferror_std)
    f_error_min_piat.append(ferror_min_piat)
    f_error_max_piat.append(ferror_max_piat)
    f_error_avg_piat.append(ferror_avg_piat)
    f_error_std_piat.append(ferror_std_piat)
    
    berror_min = mean_absolute_percentage_error(bapp.iloc[:, 0:1].values, bapp.iloc[:, 8:9].values)
    berror_max = mean_absolute_percentage_error(bapp.iloc[:, 1:2].values, bapp.iloc[:, 9:10].values)
    berror_avg = mean_absolute_percentage_error(bapp.iloc[:, 2:3].values, bapp.iloc[:, 10:11].values)
    berror_std = mean_absolute_percentage_error(bapp.iloc[:, 3:4].values, bapp.iloc[:, 11:12].values)
    berror_min_piat = mean_absolute_percentage_error(bapp.iloc[:, 4:5].values, bapp.iloc[:, 12:13].values)
    berror_max_piat = mean_absolute_percentage_error(bapp.iloc[:, 5:6].values, bapp.iloc[:, 13:14].values)
    berror_avg_piat = mean_absolute_percentage_error(bapp.iloc[:, 6:7].values, bapp.iloc[:, 14:15].values)
    berror_std_piat = mean_absolute_percentage_error(bapp.iloc[:, 7:8].values, bapp.iloc[:, -1].values)
    b_error_min.append(berror_min)
    b_error_max.append(berror_max)
    b_error_avg.append(berror_avg)
    b_error_std.append(berror_std)
    b_error_min_piat.append(berror_min_piat)
    b_error_max_piat.append(berror_max_piat)
    b_error_avg_piat.append(berror_avg_piat)
    b_error_std_piat.append(berror_std_piat)
    
#--------------------------------------------------------------------------------------
x = list(range(141))    
plt.plot(x, f_error_min, label = "forward minimum packet size")
plt.plot(x, f_error_max, label = "forward maximum packet size")
plt.plot(x, b_error_min, label = "backward minimum packet size")
plt.plot(x, b_error_max, label = "backward maximum packet size")


# naming the x axis
plt.xlabel('Application Label (0-140)')
# naming the y axis
plt.ylabel('Mean Absolute Percentage Error')
# giving a title to my graph
plt.title('Estimated Error')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()

#----------------------------------------------------------------------------------------
plt.plot(x, f_error_avg, label = "forward average packet size")
plt.plot(x, f_error_std, label = "forward standard deviation packet size")
plt.plot(x, b_error_avg, label = "backward average packet size")
plt.plot(x, b_error_std, label = "backward standard deviation packet size")

# naming the x axis
plt.xlabel('Application Label (0-140)')
# naming the y axis
plt.ylabel('Mean Absolute Percentage Error')
# giving a title to my graph
plt.title('Estimated Error')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()

#----------------------------------------------------------------------------------------
plt.plot(x, f_error_avg_piat, label = "forward average packet interarrival time")
plt.plot(x, f_error_std_piat, label = "forward standard deviation packet interarrival time")
plt.plot(x, b_error_avg_piat, label = "backward average packet interarrival time")
plt.plot(x, b_error_std_piat, label = "backward standard deviation packet interarrival time")

# naming the x axis
plt.xlabel('Application Label (0-140)')
# naming the y axis
plt.ylabel('Mean Absolute Percentage Error')
# giving a title to my graph
plt.title('Estimated Error')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()

#----------------------------------------------------------------------------------------
plt.plot(x, f_error_min_piat, label = "forward minimum packet interarrival time")
plt.plot(x, f_error_max_piat, label = "forward maximum deviation packet interarrival time")
plt.plot(x, b_error_min_piat, label = "backward minimum packet interarrival time")
plt.plot(x, b_error_max_piat, label = "backward maximum packet interarrival time")

# naming the x axis
plt.xlabel('Application Label (0-140)')
# naming the y axis
plt.ylabel('Mean Absolute Percentage Error')
# giving a title to my graph
plt.title('Estimated Error')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()