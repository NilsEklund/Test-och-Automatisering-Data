import numpy as np
import matplotlib.pyplot as plt
import os

def open_file():
    selection = input('Open latest file [y/n]: ')
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
        if most_recent_file is not None:
            file_path = 'data/' + most_recent_file
        else:
            print('No files found in the directory.')
            exit()
    elif selection == 'n':
        file_path = input('Enter filename: ')
    else:
        print('Unknown selection')
        exit()
    
    try:
        with open(file_path, mode='r') as file:
            raw_data = file.read()
        file_path = file_path.split('/')
        file_name = file_path[(len(file_path) - 1)]
    except FileNotFoundError:
        print('File not found. Incorrect file name or path')
        exit()
    return raw_data, file_name


def plot(raw_data, file_name):
    raw_data = raw_data.split(',')
    time_scale = float(raw_data[0])
    raw_data.pop(0)
    data = [float(data_point) for data_point in raw_data]

    plt.figure(figsize=(12, 8))

    # Tidssignal
    amount_of_values = len(data)
    time_datapoint = time_scale / amount_of_values
    x_label = [time_datapoint * i for i in range(amount_of_values)]
    
    plt.subplot(2, 1, 1)
    plt.plot(x_label, data, color='blue')
    plt.title(f'Time Domain Signal - {file_name}')
    plt.xlabel('Time [ms]')
    plt.ylabel('Amplitude [V]')
    plt.grid(True)

    # FFT och frekvensspektrum
    fft_and_plot(data, time_datapoint)

    plt.tight_layout()
    plt.show()

def fft_and_plot(data, time_datapoint):
    # FFT
    fft_result = np.fft.fft(data)
    fft_magnitude = np.abs(fft_result) / len(data)  # Normalisera magnituden
    frequencies = np.fft.fftfreq(len(data), d=time_datapoint / 1000)  # Omvandlar ms till sekunder för frekvensen

    # Bara positiva frekvenser
    positive_freqs = frequencies[:len(frequencies) // 2]
    positive_magnitude = fft_magnitude[:len(frequencies) // 2]

    plt.subplot(2, 1, 2)
    plt.plot(positive_freqs, positive_magnitude, color='red')
    plt.title('Frequency Domain (FFT)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [V]')
    #plt.xlim(0, 250)  # Begränsa X-axeln till 0-250 Hz
    plt.grid(True)

def main():
    data = open_file()
    plot(data[0], data[1])

if __name__ == "__main__":
    main()