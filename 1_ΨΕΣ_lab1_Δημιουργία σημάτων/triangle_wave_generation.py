import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Χρήση του backend Agg για αποθήκευση γραφημάτων
matplotlib.use('Agg')

# Τριγωνικό σήμα
t = np.linspace(0, 2, 200)
y = np.abs(1 - np.mod(t, 2))

# Απεικόνιση τριγωνικού σήματος
plt.plot(t, y)
plt.title("Τριγωνικό σήμα")
plt.savefig("triangular_signal.png")  # Αποθήκευση γραφήματος
plt.close()  # Κλείσιμο του γραφήματος

print("Το τριγωνικό σήμα αποθηκεύτηκε ως 'triangular_signal.png'.")
