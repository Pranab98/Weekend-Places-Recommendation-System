# Weekend Places Recommendation System

It's a recommendation model using machine learning approach that recommends 5 most must visit places based on a city.

This python program ranks weekend places in a city based on various criteria such as time needed to visit , google review rating , entrance fee , weekly off day and number of google reviews.



## Installation

1. It is required to have Python installed on the system. Python can be downloaded from [python.org](https://www.python.org/downloads/). Even jupyter notebook in anaconda distributions can also be used. It can be downloaded it from [anaconda distributions](https://www.anaconda.com/download)
2. After the above step , we need to install numpy and pandas libraries from the command prompt or terminal.
```
pip install numpy
pip install pandas
```
3. It is needed to install Git. Download git from [Git](https://git-scm.com/)

4. Clone this repository to  local machine using Git:
```
git clone https://github.com/Pranab98/WeekendPlaces-Recommendation-System.git
``` 

## Execution

1. Navigate to the project directory
```
cd WeekendPlaces-Recommendation-System 
```
2. Run the code on terminal
```
python Code.py
```
You will be prompted to enter the city name. After entering the city name, the script will rank weekend places based on various criteria and display the results.

## Approaches Used

Main approach is that we can go to any city irrespective of type,significance on a weekend and top cities are those cities where 
1. time needed to visit should be atleast 1 hr(since weekend; we want to spend time)
2. rating greater than 4.1 (Considered better)
3. number of google review in lakhs should be atleast 0.2
4. entrance fee <= 1000
5. weekly off should not be sunday (Since weekend; it is recommended not to be closed on atleast sunday. Saturday may not necessarily be holiday in many organisations)

## Steps

1. We will first filter the dataset based on given city and sort it on descending order based on **New rating and Google review rating**.
    a) *New Rating = Google review rating + Number of google review in lakhs.
    Reason being suppose 0.2 laks people rated 4.5 to a city and 1laks people rated 4.3 to some other ; it is intuitive to say that the later is better that the former.*

    b) *Now (0.2+4.5 < 1+4.3); so the later city is more recommended than the former city.*

2. Now we would filter a dataset based on our 5 above criteria from approach section.

3. One point to be noted that there are some cities which have only one place or less than 5. *In such a case, we will recommend all places corresponding to the given city irrespective of being satisfied the above criteria from approach section.But will be based on the descending order format above.*
**But since it is for weekend, we will stick Weekly Off not to be sunday even in this case.*
 


