import matplotlib.pyplot as plt

def rz(data):
    time = []
    voltage = []
    t = 0
    for bit in data:
        time.extend([t, t + 0.5, t + 0.5, t + 1])
        if bit == '1':
            voltage.extend([1, 1, 0, 0])
        else:
            voltage.extend([-1, -1, 0, 0])
        t += 1
    return time, voltage


binary_data = "0100110"
time, voltage = rz(binary_data)

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
