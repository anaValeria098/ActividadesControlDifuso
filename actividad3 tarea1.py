import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Configuración de las variables difusas
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Generación automática de funciones de pertenencia (triangulares)
quality.automf(3)  # poor, average, good
service.automf(3)  # poor, average, good

# Funciones GAUSSIANAS CORRECTAS para la propina (parámetros separados)
tip['low'] = fuzz.gaussmf(tip.universe, 0.0, 3.0)     # mean, sigma
tip['medium'] = fuzz.gaussmf(tip.universe, 12.5, 3.0) # mean, sigma 
tip['high'] = fuzz.gaussmf(tip.universe, 25.0, 3.0)   # mean, sigma

# Visualización MEJORADA de las funciones gaussianas
fig, ax = plt.subplots(figsize=(8, 4))

# Graficar cada función gaussiana manualmente
ax.plot(tip.universe, fuzz.gaussmf(tip.universe, 0.0, 3.0), 'b', label='Low')
ax.plot(tip.universe, fuzz.gaussmf(tip.universe, 12.5, 3.0), 'g', label='Medium')
ax.plot(tip.universe, fuzz.gaussmf(tip.universe, 25.0, 3.0), 'r', label='High')

ax.set_title('Funciones Gaussianas para la Propina')
ax.legend()
ax.set_xlabel('Porcentaje de propina')
ax.set_ylabel('Pertenencia')
plt.grid(True)
plt.show()
