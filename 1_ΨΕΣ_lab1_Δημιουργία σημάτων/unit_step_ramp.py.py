import numpy as np
import matplotlib.pyplot as plt

# Ορισμός backend σε Agg
import matplotlib
matplotlib.use('Agg')

# Ορισμός χρονικού διαστήματος
t = np.linspace(-1, 1, 100)

# Μοναδιαία βηματική συνάρτηση
u = np.where(t >= 0, 1, 0)
plt.plot(t, u)
plt.title("Μοναδιαία βηματική συνάρτηση")
plt.savefig("step_function.png")  #
plt.close()

# Μοναδιαία επικλινής συνάρτηση
r = np.where(t >= 0, t, 0)
plt.plot(t, r)
plt.title("Μοναδιαία επικλινής συνάρτηση")
plt.savefig("ramp_function.png")
plt.close()
