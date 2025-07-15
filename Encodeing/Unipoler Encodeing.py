import matplotlib.pyplot as plt

def unipolar_nrz(binary_data):
    time = []
    voltage = []
    t = 0
    for bit in binary_data:
        time.extend([t, t + 1])
        if bit == '1':
            voltage.extend([1, 1])
        else:
            voltage.extend([0, 0])
        t += 1
    return time, voltage


binary_data = "10110"
time, voltage = unipolar_nrz(binary_data)

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
