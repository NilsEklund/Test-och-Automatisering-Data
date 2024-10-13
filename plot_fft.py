# Plots the FFT from the data that is imported from the data folder
# The FFT calculations do not work as intended

import numpy as np
import matplotlib.pyplot as plt
import os

def open_file():
        
    selection = input('Open lastest file [y/n]: ')
    if selection == 'y':
        directory_path = 'data/'
        most_recent_file = None
        most_recent_time = 0
        # iterate over the files in the directory using os.scandir
        for entry in os.scandir(directory_path):
            if entry.is_file():
                # get the modification time of the file using entry.stat().st_mtime_ns
                mod_time = entry.stat().st_mtime_ns
                if mod_time > most_recent_time:
                    # update the most recent file and its modification time
                    most_recent_file = entry.name
                    most_recent_time = mod_time
            file_path = 'data/' + most_recent_file
    elif selection == 'n':
        file_path = input('Enter filename: ')
    else:
        print('Unknown selection')
        exit()
    
    try:
        file = open(file_path, mode = 'r')
        raw_data = file.read()
        file.close()
        file_path = file_path.split('/')
        file_name = file_path[(len(file_path) - 1)]
    except FileNotFoundError:
        print('File not found. Incorrect file name or path')
        exit()
    return raw_data

# Function to compute and plot the FFT
def plot_fft(raw_data):

    raw_data = raw_data.split(',')
    time_scale = raw_data[0]
    raw_data.pop(0)
    amplitude = []
    for data_point in raw_data:
        amplitude.append(float(data_point))

    amount_of_values = len(raw_data)
    time_datapoint = float(time_scale) / amount_of_values
    time = []
    for i in range (0,amount_of_values):
        time.append(time_datapoint * i)

    # Compute the time step (sampling interval)
    dt = np.mean(np.diff(time))
    
    # Perform FFT
    fft_values = np.fft.fft(amplitude)
    
    # Compute the corresponding frequencies
    n = len(amplitude)
    freqs = np.fft.fftfreq(n, dt)
    
    # Compute the magnitude of the FFT
    fft_magnitude = np.abs(fft_values) / n
    
    # Plot the FFT (magnitude vs frequency)
    plt.figure(figsize=(10, 6))

    # Set frequency limit to 0 - 1000 Hz
    plt.xlim(0, 1000)
    
    # Plot only the positive half of the frequency spectrum
    plt.plot(freqs[:n//2], fft_magnitude[:n//2])
    
    plt.title('FFT of the Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()


def main():
    data = open_file()
    plot_fft(data)


if __name__ == "__main__":
    main()