#!/usr/bin/env python
# coding: utf-8

# In[113]:


import time
from pandas import*
from numpy import*

CITY_DATA = { 'chicago':       'E:\\Data Analysis\\projects\\python nanodegree\\chicago.csv',
              'new_york_city': 'E:\\Data Analysis\\projects\\python nanodegree\\new_york_city.csv',
              'washington':    'E:\\Data Analysis\\projects\\python nanodegree\\washington.csv' }


# In[114]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new_york_city','washington']
    city=''
    while(True):
        city=input("Please Enter a valid city from {}".format(cities)).lower()
        if(city in cities):
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june']
    month=''
    while(True):
        month=input("Please Enter a valid month from {} or all to apply no month filter ".format(months)).lower()
        if((month in months) or (month=='all')):
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day=''
    while(True):
        day=input("Please Enter a valid day from {} or all to apply no day filter ".format(days)).lower()
        if((day in days) or (day=='all')):
            break


    print('-'*40)
    return city, month, day


# In[123]:


#x,y,z=get_filters()


# In[135]:

# loading data
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


# In[136]:


# print(x,y,z)
# df=load_data(x,y,z)
# print(df)


# In[137]:


def time_stats(df): 
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is :{}".format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print("The most common day is :{}".format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print("The most common hour is :{}".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[138]:


# time_stats(df)
# print(df)


# In[139]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station is ",df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("most commonly used End station is ",df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip is",intersect1d(df['Start Station'],df['End Station'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[140]:


#station_stats(df)


# In[141]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(sum(df['Trip Duration']))


    # TO DO: display mean travel time
    print(mean(df['Trip Duration']))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[142]:


#trip_duration_stats(df)


# In[143]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:\n",df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if('Gender' not in df):
        print("there is no gender type in this data fram")
    else:
        print("counts of gender:\n",df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' not in df):
        print("there is no Birth Year in this data fram")
    else:
        print("earliest, most recent, and most common year of birth are:")
        print(df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[144]:


#user_stats(df)


# In[154]:


def Display_Data():
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while(view_data=='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: Enter yes or no\n").lower()
        


# In[155]:


def main():
    while True:
        city, month, day = get_filters()
        print(city,month,day)   
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Display_Data()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
       



# In[156]:


if __name__ == "__main__":
	main()


# In[ ]:




