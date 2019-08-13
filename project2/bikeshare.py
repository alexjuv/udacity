import time
import pandas as pd
import numpy as np
import calendar
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = { 
    "all": 0, 
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December ": 12
}

DAY_DATA = { "all", "Monday", "Tuesday", "Eednesday", "Thursday", "Friday", "Saturday", "Sunday" }

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
    city = input('City(chicago, new york city or washington):')
    city = 'chicago'
    while True:        
        if (CITY_DATA.__contains__(city)):
            break;
        else :
            city = input('Incorrect Input. Try again.\nCity (chicago, new york city or washington):')


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Month (all, january, february, ... , june):')
    month = 'all'
    while True:        
        if (month in MONTH_DATA):
            month = MONTH_DATA[month]
            break;
        else :
            month = input('Incorrect Input. Try again.\nMonth (all, january, february, ... , june):')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Day (all, monday, tuesday, ... sunday):')
    day = 'all'
    while True:        
        if (day in DAY_DATA):
            break;
        else :
            day = input('Incorrect Input. Try again.\nDay (all, monday, tuesday, ... sunday):')

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if (month != 0):        
        filter = df['Start Time'].dt.month == month
        df.where(filter, inplace = True)
    if (day.lower() != "all"):  
        filter = df['Start Time'].dt.weekday_name == day
        df.where(filter, inplace = True)
    #print (df.head(10))
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # https://www.jianshu.com/p/41039996d867
    # https://www.jianshu.com/p/b91e3ae940ec
    # https://www.jianshu.com/p/00a61efc187b
    
    df = df.set_index('Start Time')#.dropna(axis = 0)
    #print (df.count())

    
    #df_period.dropna(axis = 0)
    #df['number'] = 0
    #s = pd.Series(df['number'], index=df.index)
    #print (df.head())

    #df_period = df.to_period('M')
    # print (df_period)
    # print(df.resample('M').sum().head())
    print(df.resample('M').count().to_period('M').head())
    #s = pd.Series(df_period['number'], index=df_period.index)
    #print (s)
    #print (df_period.index.asfreq('M'))
    #print (df_period.index.asfreq('M'))
    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df['Start Time'])
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
