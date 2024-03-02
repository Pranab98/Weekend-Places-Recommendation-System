
import numpy as np
import pandas as pd

data_set = pd.read_csv("Top Indian Places to Visit.csv")

#Eliminating columns which are not required for this approach
data_set = data_set.drop(data_set.columns[[0,1,2,5,6,10,12,13,15]],axis = 1)


# filling all NaN values with 'NO' in 'Weekly Off' 
# column denoting there is no weekly off
data_set = data_set.fillna('NO')


# Introducing one new column 'New Rating' having the
# corresponding sum of 'Google review rating'and 'Number of google review in lakhs'
newRatings = []        
for i in range(len(data_set)):
    newRatings.append(data_set['Google review rating'].iloc[i]+data_set['Number of google review in lakhs'].iloc[i])
data_set.insert(7, "New Rating", newRatings, True)


# The actual function which recommends top 5 
# weekend places based on some criteria
def cityName(city):
    #Check whether inputted city exists in the list
    for i in range(len(data_set)):
        f = 0
        if(data_set['City'].iloc[i].lower() == city.lower()):
            city = data_set['City'].iloc[i]
            f = 1
            break
    if(f == 0):
        print(f"There is no city named '{city}' in the list.")
    
    #Contains a new dataset of all rows and col of the given City
    city_data = data_set.loc[data_set['City'] == city]

    #Sorting the 'city_data' in descending order
    sortedCity = city_data.sort_values(by = ['New Rating' , 'Google review rating'],ascending=False) 
    
    #filtering all values satisfying Time-Needed>=1,Review>4.1,
    #No-of-Review>=0.2,fee<=1000,Weekly-Off != Sunday
    topPlaces = sortedCity.loc[(sortedCity["time needed to visit in hrs"]>=1)&(sortedCity["Google review rating"]>4.1)&(sortedCity['Number of google review in lakhs']>=0.2)&(sortedCity['Entrance Fee in INR']<=1000)&(sortedCity["Weekly Off"]!='Sunday')]
    
    #filtering all values satisfying Time-Needed<1,Review<=4.1,
    #No-of-Review<0.2,fee>1000,Weekly-Off != Sunday
    avgPlaces = sortedCity.loc[(sortedCity["time needed to visit in hrs"]<1)|(sortedCity["Google review rating"]<=4.1)|(sortedCity['Number of google review in lakhs']<0.2)|(sortedCity['Entrance Fee in INR']>1000)&(sortedCity["Weekly Off"]!='Sunday')]
    
    #Calculate no of rows for each dataset
    topLen = len(topPlaces) 
    avgLen = len(avgPlaces)
    
    if(topLen >= 5):
        for i in range(1,topLen+1):
            if(i<6):
                print(str(i)+')'+topPlaces['Name'].iloc[i-1])
            else:
                break
    else:
        i = 0
        for j in range(1,topLen+1):
            if(j<6):
                print(str(j)+')'+topPlaces['Name'].iloc[j-1])
                i = j
            else:
                break
        for j in range(1,avgLen+1):
            if(j <= (5-topLen)):
                print(str(i+1)+')'+avgPlaces['Name'].iloc[j-1])
                i+=1
            else:
                break
                
#Take input
city = input("Enter a city: ")                            
cityName(city)  #function call





