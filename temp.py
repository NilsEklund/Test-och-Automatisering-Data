import numpy as np
import matplotlib.pyplot as plt

# Function to compute and plot the FFT
def plot_fft(amplitude, time):
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
    
    # Plot only the positive half of the frequency spectrum
    plt.plot(freqs[:n//2], fft_magnitude[:n//2])
    
    plt.title('FFT of the Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

# Example usage
# Amplitude data and corresponding time data
amplitude_data = [1, 0.5, 0.3, 0.1, 0.05]  # Replace with your amplitude data
time_data = [0, 1, 2, 3, 4]  # Replace with your time data

plot_fft(amplitude_data, time_data)
