import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']

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
    
    while True:
        try:
            city = input('Which city would you like to analyze? (Chicago, New York City, or Washington): ').lower()
            if city not in city_list:
                raise NameError
            else:
                break
        except:
            print('That\'s not a valid input')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            global month
            month = input('Which month(s) would you like to analyze? (All, January, February, ..., June): ').lower()
            
            if month not in months and month != 'all':
                raise NameError
            else:
                break
        except:
            print('That\'s not a valid input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            global day
            day = input('Which day(s) of week would you like to analyze? (All, Monday, Tuesday, ... Sunday): ').lower()
            
            if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                raise NameError
            else:
                break
        except:
            print('That\'s not a valid input')

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
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['Month'] == month]
   
    if day != 'all':
        day = day.title()
        df = df[df['Day of Week'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month != 'all':
        print('The most common month: ', month)
    else:
        print('The most common month: ', df['Month'].mode()[0], '\n')

    # TO DO: display the most common day of week
    if day != 'all':
        print('The most common day of week: ', day)
    else:
        print('The most common day of week: ', df['Day of Week'].mode()[0], '\n')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    print('The most common hour: ', df['hour'].mode()[0], '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ', df['Start Station'].mode()[0], '\n')

    # TO DO: display most commonly used end station
    print('The most commonly used end station: ', df['End Station'].mode()[0], '\n')

    # TO DO: display most frequent combination of start station and end station trip
    #df['Station Combination'] = df[['Start Station', 'End Station']].itertuples(index=False, name=None)
    combo = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    ss, es = combo.index[0]
    print('The most commonly frequent combination of start station and end station trip: {} and {}'.format(ss, es), '\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total trip duration: {} seconds.'.format(df['Trip Duration'].sum()), '\n')

    # TO DO: display mean travel time
    print('Mean travel time: {} seconds.'.format(df['Trip Duration'].mean()), '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Bikeshare user type statistics:\n', user_types, '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print('Bikeshare user gender statistics:\n', user_gender, '\n')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        print('Earliest, most recent, and most common year of birth: {}, {}, {}.'.format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    while True:
        try:
            x = input('Do you want to see raw data? ').lower()
            if x == 'yes':
                i = 5
                print(df.iloc[:i])
                while True:
                    try:
                        y = input('Do you want to see more 5 lines of raw data? ').lower()
                        if y == 'yes':
                            i += 5
                            print(df.iloc[i-5:i])
                        elif y == 'no':
                            break
                        else:
                            raise NameError
                    except:
                        print('That\'s not a valid input')
                break
            elif x == 'no':
                break
            else:
                raise NameError
        except:
            print('That\'s not a valid input')   
                    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
