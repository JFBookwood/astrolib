# AstroLib Dokumentation

## Installation

```bash
pip install -e .
```

## Hauptkomponenten

### 1. Void-Finding (voidfinder.py)
- Implementiert verschiedene Void-Finding Algorithmen
- ZOBOV und Watershed-Methoden
- Optimiert für große Datensätze

### 2. N-Body Simulationen (nbody.py)
- Barnes-Hut Algorithmus für effiziente Kraftberechnung
- Leapfrog Integration
- Adaptive Zeitschritte

### 3. Neutrino-Physik (neutrino.py)
- Neutrino-Oszillationen
- PMNS-Matrix Berechnungen
- Materie-Effekte

## Beispiele

```python
import astrolib

# Void-Finding Beispiel
finder = astrolib.voidfinder.WatershedVoidFinder()
voids = finder.find_voids(density_field)

# N-Body Simulation
sim = astrolib.nbody.NBodySimulation(positions, velocities, masses)
sim.step(dt=0.01)

# Neutrino-Oszillationen
osc = astrolib.neutrino.NeutrinoOscillation(energy=1.0, baseline=295.0)
prob = osc.calculate_oscillation_probability('e', 'mu')
```
