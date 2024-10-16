# Plots the data from a selected data file from the data folder.

import numpy as np
import matplotlib.pyplot as plt
import os

# Ask if the user want to open the latest file or a specific file
def open_file():
        
    selection = input('Open latest test file [y/n]: ')
    if selection == 'y':
        directory_path = 'data/'
        most_recent_file = None
        most_recent_time = 0
        for entry in os.scandir(directory_path):
            if entry.is_file():
                mod_time = entry.stat().st_mtime_ns
                if mod_time > most_recent_time:
                    most_recent_file = entry.name
                    most_recent_time = mod_time
            file_path = 'data/' + most_recent_file
    elif selection == 'n':
        file_path = input('Enter filename: ')
    else:
        print('Unknown selection')
        exit()
    
    # Opens the requested file and returns the data and file name
    try:
        file = open(file_path, mode = 'r')
        raw_data = file.read()
        file.close()
        file_path = file_path.split('/')
        file_name = file_path[(len(file_path) - 1)]
    except FileNotFoundError:
        print('File not found. Incorrect file name or path')
        exit()
    return raw_data, file_name

# Processes the data from the file and plots it line diagram
def plot(raw_data,file_name):
    raw_data = raw_data.split(',')
    time_scale = raw_data[0]
    raw_data.pop(0)
    data = []
    for data_point in raw_data:
        data.append(float(data_point))

    plt.figure(figsize=(10, 6))
    amount_of_values = len(raw_data)
    time_datapoint = float(time_scale) / amount_of_values
    x_label = []
    for i in range (0,amount_of_values):
        x_label.append(time_datapoint * i)
    plt.plot(x_label, data, color='blue')
    plt.title(file_name)
    plt.xlabel('Time [ms]')
    plt.ylabel('Amplitud [V]')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    data = open_file()
    plot(data[0],data[1])


if __name__ == "__main__":
    main()