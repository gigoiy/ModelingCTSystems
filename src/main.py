import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Numerator and denominator coefficients calculated from given values
num = [.01]
den = [.005, .06, .1001] 

system = signal.TransferFunction(num, den) # Create the system

t, y = signal.step(system) # Get the time axis and the step response of the system

final_value = y[-1] # Get final step response point

# Calculate when the step response is 2% within bounds of the final step response value
within_bounds = np.where(np.abs(y - final_value) <= .02 * np.abs(final_value))[0]

if len(within_bounds) > 0:
    Ts = t[within_bounds[0]]
else:
    Ts = None

print("Estimated Settling Time:", Ts, "seconds")

# Plot the step response
plt.plot(t, y)
plt.title("Step Response of DC Motor")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.grid(True)
plt.savefig('img/step_response.png')
plt.show()

w, mag, phase = signal.bode(system) #Calculate frequency, magnitude, and phase of the system

# Plot the frequency response

# Magnitude
plt.semilogx(w, mag)
plt.title("Bode Plot of DC Motor")
plt.ylabel("Magnitude (dB)")
plt.grid(True, which="both")
plt.savefig('img/magnitude_response.png')
plt.show()

# Phase
plt.semilogx(w, phase)
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (deg)")
plt.grid(True, which="both")
plt.savefig('img/phase_response.png')
plt.show()


