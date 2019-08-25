import time
import pandas as pd
#import numpy as np
#import calendar
#import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = { 
    "all": 0, 
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december ": 12
}

DAY_DATA = { "all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" }

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
    if(len(city.strip()) == 0):
        city = 'chicago'
    while True:        
        if (CITY_DATA.__contains__(city.lower())):
            city = city.lower()
            break;
        else :
            city = input('Incorrect Input. Try again.\nCity (chicago, new york city or washington):')


    # TO DO: get user input for month (all, january, february, ... , december)
    month = input('Month (all, january, february, ... , december):')
    if(len(month.strip()) == 0):
        month = 'all'
    while True:        
        if (month.lower() in MONTH_DATA):
            month = MONTH_DATA[month.lower()]
            break;
        else :
            month = input('Incorrect Input. Try again.\nMonth (all, january, february, ... , december):')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Day (all, monday, tuesday, ..., sunday):')
    if(len(day.strip()) == 0):
        day = 'all'
    while True:        
        if (day.lower() in DAY_DATA):
            day = day.lower()
            break;
        else :
            day = input('Incorrect Input. Try again.\nDay (all, monday, tuesday, ..., sunday):')

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
    
    # pick up criteria
    df['month'] = df['Start Time'].dt.month
    df['dayofweek'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month    

    most_common_month = df['month'].mode()[0]
    print('The most common month is:', most_common_month)
    
    # TO DO: display the most common day of week

    most_common_day = df['dayofweek'].mode()[0]
    print('The most common day of week is:', most_common_day)

    # TO DO: display the most common start hour

    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', most_start)

    # TO DO: display most commonly used end station
    most_end = df['End Station'].mode()[0]
    print('The most commonly used end station is:', most_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip is:', most_station[0], most_station[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    df['timespan'] = pd.to_datetime(df["End Time"]) - df["Start Time"]
    print('The mean travel time is:', df['timespan'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print('The counts of gender:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('The earliest year of birth: ', int(df['Birth Year'].min()))
    print('The most recent year of birth: ', int(df['Birth Year'].max()))
    print('The most recent year of birth: ', int(df['Birth Year'].value_counts().index[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
