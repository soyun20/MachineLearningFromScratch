####################################################################################
# File Name : hw#1                                                                 #  
# Date  : 2020/07/22                                                               #  
# OS : Windows 10                                                                  #  
# Author : 최소윤                                                                  # 
# -------------------------------------------------------------------------------  #  
# requirements : python 3.7                                                        #
#                                                                                  #
####################################################################################   


#import random                      

#import numpy as np                 

import pandas as pd                 

import matplotlib.pyplot as plt    

#import warnings                     



try:

    from sklearn.cluster import KMeans  # check installation of sklearn

except:

    print("Not installed scikit-learn.") 

    pass





if __name__ == '__main__': # Start from main

    data = pd.read_csv('data.csv')
    plt.scatter(data['Sepal length'], data['Sepal width'],alpha=0.5)
    plt.xlabel('sepal length (cm)')
    plt.ylabel('sepal width (cm)')
    plt.title('from scikit-learn library')
    plt.show() # show plot