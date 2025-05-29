import numpy as np
import matplotlib.pyplot as plt

def f(t, freq = 2):
    return 1.5 * np.sin(2*np.pi*freq*t/1000)

plt.figure(10); plt.clf();
t = np.arange(30000) * 0.1 
plt.plot(t, f(t))
plt.title("Target function")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.show()