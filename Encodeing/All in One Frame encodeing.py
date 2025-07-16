import matplotlib.pyplot as plt

# Unipolar NRZ
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

# NRZ-L
def nrz_l(binary_data):
    time = []
    voltage = []
    t = 0
    for bit in binary_data:
        time.extend([t, t + 1])
        if bit == '0':
            voltage.extend([1, 1])
        else:
            voltage.extend([-1, -1])
        t += 1
    return time, voltage

# NRZ-I
def nrz_i(binary_data):
    time = []
    voltage = []
    t = 0
    current_voltage = 1
    for bit in binary_data:
        time.extend([t, t + 1])
        if bit == '1':
            current_voltage *= -1
        voltage.extend([current_voltage, current_voltage])
        t += 1
    return time, voltage

# RZ
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

# Manchester
def manchester_encoding(data):
    time = []
    voltage = []
    t = 0
    for bit in data:
        time.extend([t, t + 0.5, t + 0.5, t + 1])
        if bit == '1':
            voltage.extend([-1, -1, 1, 1])
        else:
            voltage.extend([1, 1, -1, -1])
        t += 1
    return time, voltage

# Plot all
binary_data = "0100110"
encodings = {
    "Unipolar NRZ": unipolar_nrz,
    "NRZ-L": nrz_l,
    "NRZ-I": nrz_i,
    "RZ": rz,
    "Manchester": manchester_encoding
}

plt.figure(figsize=(12, 10))

for i, (name, func) in enumerate(encodings.items(), 1):
    time, voltage = func(binary_data)
    plt.subplot(len(encodings), 1, i)
    plt.title(name)
    plt.plot(time, voltage, drawstyle='steps-post')
    plt.ylim(-2, 2)
    plt.grid(True)
    for j, bit in enumerate(binary_data):
        plt.text(j + 0.3, 1.2, bit, fontsize=10)
    plt.ylabel("Voltage")
    if i == len(encodings):
        plt.xlabel("Time")

plt.tight_layout()
plt.show()
