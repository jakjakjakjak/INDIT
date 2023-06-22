import numpy as np
import matplotlib.pyplot as plt

# Eingabe der Genauigkeit durch den Benutzer
genauigkeit = float(input("Bitte geben Sie die Genauigkeit ein: "))

# Erzeugung der x-Werte von 0 bis 360 Grad mit der eingegebenen Genauigkeit
x = np.arange(0, 360, genauigkeit)

# Berechnung der Sinuswerte
y = np.sin(np.deg2rad(x))

# Erzeugung des Plots
plt.plot(x, y)

# Achsenbeschriftungen
plt.xlabel('Grad')
plt.ylabel('Sinus')

# Titel des Plots
plt.title('Sinuskurve')

# Anzeige des Plots
plt.show()