import numpy as np
from astrolib.optimized_voids import StreamingVoidFinder
from astrolib.resource_manager import ResourceManager

# Create sample data
np.random.seed(42)
positions = np.random.rand(1000, 3) * 100  # Random positions in 100 Mpc box
box_size = 100.0

# Initialize resource manager
resource_manager = ResourceManager()
resource_manager.start_monitoring()

# Initialize void finder
finder = StreamingVoidFinder(chunk_size=100)

# Create data iterator
def data_iterator():
    chunk_size = 100
    for i in range(0, len(positions), chunk_size):
        yield positions[i:i+chunk_size]

# Find voids
print("Starting void finding...")
for i, void in enumerate(finder.find_voids_streaming(data_iterator(), box_size)):
    print(f"Found void {i+1}: radius = {void['radius']:.2f} Mpc")
    if i >= 4:  # Just show first 5 voids
        break

resource_manager.stop_monitoring()
