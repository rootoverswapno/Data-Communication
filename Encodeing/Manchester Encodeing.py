import matplotlib.pyplot as plt

def manchester_encoding(data):
    time = []
    voltage = []
    t = 0

    for bit in data:
        # প্রতিটি বিটে ২টি সেগমেন্ট: t → t+0.5 এবং t+0.5 → t+1
        time.extend([t, t + 0.5, t + 0.5, t + 1])

        if bit == '1':
            # Low to High
            voltage.extend([-1, -1, 1, 1])
        else:
            # High to Low
            voltage.extend([1, 1, -1, -1])

        t += 1

    return time, voltage



binary_data = "0100110"
time, voltage = manchester_encoding(binary_data)

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
