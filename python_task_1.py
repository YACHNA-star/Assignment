# -*- coding: utf-8 -*-
"""python_task_1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T-dxhIAttm8M1pvYwFtnrRLTQqBu8-Yk
"""

#1
import pandas as pd
def generate_car_matrix(df)->pd.DataFrame:
#def generate_car_matrix(df):
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values,
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Pivot the DataFrame to create the matrix
    pivot_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for i in range(min(pivot_df.shape)):
        pivot_df.iloc[i, i] = 0

    return pivot_df

# Read dataset-1.csv as a DataFrame
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
dataset_df = pd.read_csv(url)

# Call the function with the DataFrame
df = generate_car_matrix(dataset_df)
print(df)

#2
import pandas as pd

def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    # Add a new categorical column 'car_type' based on values in the 'car' column

    car_type_counts = {'low': 0, 'medium': 0, 'high': 0}

    for car_value in df['car']:
        if car_value <= 15:
            car_type_counts['low'] += 1
        elif car_value <= 25:
            car_type_counts['medium'] += 1
        else:
            car_type_counts['high'] += 1

    return dict(sorted(car_type_counts.items()))


# Read dataset-1.csv as a DataFrame
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
dataset_df = pd.read_csv(url)
# Call the function with the DataFrame
result_dict = get_type_count(dataset_df)
print(result_dict)

#4
import pandas as pd
def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # Initialize an empty list to store indices
    bus_indexes = []

    # Loop through the 'bus' column and find indices where value > 2 * mean_bus
    for index, value in enumerate(df['bus']):
        if value > 2 * mean_bus:
            bus_indexes.append(index)

    # Sort indices in ascending order
    bus_indexes.sort()

    return bus_indexes
    # Read dataset-1.csv as a DataFrame
    url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
    dataset_df = pd.read_csv(url)

   # Call the function with the DataFrame
    result_list = get_bus_indexes(dataset_df)
    print(result_list)

#4
import pandas as pd
def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    # Group by 'route' column and calculate the mean of 'truck' column for each route
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' column is greater than 7
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the routes in ascending order
    filtered_routes.sort()

    return filtered_routes

# Read dataset-1.csv as a DataFrame
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
dataset_df = pd.read_csv(url)

# Call the function with the DataFrame
result_list = filter_routes(dataset_df)
print(result_list)

#5
import pandas as pd

def multiply_matrix(input_df):
    # Copy the DataFrame to avoid modifying the original DataFrame
    modified_df = input_df.copy()

    # Apply the logic to modify the values in the DataFrame
    modified_df = modified_df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the modified values to 1 decimal place
    modified_df = modified_df.round(1)

    return modified_df

"""def generate_car_matrix(df)->pd.DataFrame:

    # Pivot the DataFrame to create the matrix
    pivot_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for i in range(min(pivot_df.shape)):
        pivot_df.iloc[i, i] = 0

    return pivot_df """

# Read dataset-1.csv as a DataFrame
url = 'https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-1.csv'
dataset_df = pd.read_csv(url)

# Call the function with the DataFrame
df = generate_car_matrix(dataset_df)


# DataFrame (Replace this with the resulting DataFrame from Question 1)
result_df = df

# Call the function with the resulting DataFrame from Question 1
modified_result_df = multiply_matrix(result_df)
print(modified_result_df)

def time_check(data)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here



    # Convert 'timestamp' columns to datetime format
    data['startTimestamp'] = pd.to_datetime(data['startDay'] + ' ' + data['startTime'])
    data['endTimestamp'] = pd.to_datetime(data['endDay'] + ' ' + data['endTime'])

    # Extract day of the week (0: Monday, 6: Sunday) and hour of the day for start and end timestamps
    data['start_day_of_week'] = data['startTimestamp'].dt.dayofweek
    data['start_hour_of_day'] = data['startTimestamp'].dt.hour
    data['end_day_of_week'] = data['endTimestamp'].dt.dayofweek
    data['end_hour_of_day'] = data['endTimestamp'].dt.hour

    # Function to check completeness for each (id, id_2) pair
    def check_completeness(group):
        # Check if all 7 days are covered and a full 24-hour period exists for each (id, id_2) pair
        return ((group['start_day_of_week'].nunique() == 7) and (group['end_day_of_week'].nunique() == 7) and
                (group['start_hour_of_day'].nunique() == 24) and (group['end_hour_of_day'].nunique() == 24))

    # Apply the check_completeness function and create a boolean series with a multi-index (id, id_2)
    completeness_series = data.groupby(['id', 'id_2']).apply(check_completeness)

    return completeness_series

# Read the dataset-2.csv file into a DataFrame

df = pd.read_csv('https://raw.githubusercontent.com/mapup/MapUp-Data-Assessment-F/main/datasets/dataset-2.csv')

# Call the function with the DataFrame
completeness_result = time_check(df)
print(completeness_result)


# Assuming 'dataset-2.csv' is read into a DataFrame named 'df'