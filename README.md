# Orbit-simulation
Simulation of planetary orbit around a central point mass.
Planet position, velocity and acceleration are updated using real orbital.gravitational behavior.

Parameters:

(planet.py)
- M_CENTRE : mass of the central point mass

(main.py)
- REFRESH_RATE : planet parameters refresh rate (in number of days)
- TOTAL_TIME : the simulated time after which the program stops (in number of years)
- D_TO_CENTRE_INITIAL : initial distance of the planet to the central point mass
- DISTANCE_SCALE : distances are scaled down by this factor (DISTANCE_SCALE == 1 => 1 pixel = 1 meter)
- V_MAGN_INITIAL : initial speed of the planet in the positive x direction

