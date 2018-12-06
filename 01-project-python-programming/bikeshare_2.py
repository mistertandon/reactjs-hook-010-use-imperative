import time
import pandas as pd
import numpy as np
import helper
import sys
from datetime import datetime

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    month = day = 'all'
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = helper.get_user_city()
    print('Selected city is: ', city)

    # get user input for filetr type input
    filter_val = helper.get_user_filter()
    print('Selected filter is: ', filter_val)

    # get user input for month (all, january, february, ... , june)
    if filter_val =='both' or filter_val =='month':
        month = helper.get_month()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_val =='both' or filter_val =='day':    
        day = helper.get_day()
        print('Selected Day is: ', day)

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
    df = pd.read_csv(city + ".csv")

    df['Start Time'], df['End Time'] = pd.to_datetime(df['Start Time']), pd.to_datetime(df['End Time'])

    if month != 'all':
        df['start_time_month'], df['end_time_month'] = df['Start Time'].dt.month, df['End Time'].dt.month
        df = df[(df['start_time_month'] == month) & (df['end_time_month'] == month)]
    
    if day != 'all':
        df['start_time_weekday'], df['end_time_weekday'].dt.weekday = df['Start Time'].dt.weekday, df['End Time'].dt.weekday
        df = df[(df['start_time_weekday'] == day) & (df['start_time_weekday'] == day)]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

        #city, month, day = get_filters()
        #df = load_data(city, month, day)
        df = load_data("chicago", 6, 'all')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()