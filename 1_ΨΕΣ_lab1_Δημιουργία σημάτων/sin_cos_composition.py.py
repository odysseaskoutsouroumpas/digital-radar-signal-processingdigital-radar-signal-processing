import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Χρήση του backend Agg για αποθήκευση γραφημάτων
matplotlib.use('Agg')

# Ορισμός χρονικού διαστήματος
t = np.linspace(0, 2, 200)

# Δημιουργία σημάτων
y1 = np.sin(t)  # Συνάρτηση ημιτόνου
y2 = np.cos(2 * t)  # Συνάρτηση συνημιτόνου με διπλάσια συχνότητα
y3 = y1 + y2  # Άθροισμα σημάτων
y4 = y1 - 2 * y2  # Συνδυασμός σημάτων

# Απεικόνιση των σημάτων
plt.plot(t, y1, label="y1 = sin(t)")
plt.plot(t, y2, label="y2 = cos(2t)")
plt.plot(t, y3, label="y3 = y1 + y2")
plt.plot(t, y4, label="y4 = y1 - 2*y2")
plt.legend()
plt.title("Συνδυασμός σημάτων")
plt.savefig("signal_combination.png")  # Αποθήκευση γραφήματος
plt.close()  # Κλείσιμο του γραφήματος

print("Το γράφημα αποθηκεύτηκε ως 'signal_combination.png'.")
