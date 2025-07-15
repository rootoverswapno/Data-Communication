import matplotlib.pyplot as plt


def differential_manchester_encoding(data):
    time = []
    voltage = []
    current_level = 1  # Start with high level

    for i, bit in enumerate(data):
        # Start of bit period
        if bit == '0':
            current_level *= -1  # Invert for '0'

        # First half (before mid-bit transition)
        time.extend([i, i + 0.5])
        voltage.extend([current_level, current_level])

        # Mid-bit transition (always occurs)
        current_level *= -1

        # Second half (after mid-bit transition)
        time.extend([i + 0.5, i + 1])
        voltage.extend([current_level, current_level])

    return time, voltage



binary_data = "10100"
time, voltage = differential_manchester_encoding(binary_data)

# Plotting
plt.figure(figsize=(10, 2))
plt.title("Unipolar NRZ Encoding")
plt.plot(time, voltage, drawstyle='steps-post')
plt.ylim(-1.5, 2.5)
plt.xlabel("Time")
plt.ylabel("Voltage Level")
plt.grid(True)

# Display binary bits on top of waveform
for i, bit in enumerate(binary_data):
    plt.text(i + 0.4, 1.2, bit, fontsize=12)

plt.show()
