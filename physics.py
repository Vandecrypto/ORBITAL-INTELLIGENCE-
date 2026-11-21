import numpy as np

# ==========================================
# ORBITAL MECHANICS ENGINE
# ==========================================

# Earth's physical constants (SI units)

EARTH_MASS = 5.97219e24       # kg
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³ kg⁻¹ s⁻²

EARTH_RADIUS = 6_371_000      # metres

# Earth's standard gravitational parameter
MU = GRAVITATIONAL_CONSTANT * EARTH_MASS


# ==========================================
# 1. ORBITAL RADIUS
# ==========================================

def orbital_radius(altitude_km):

    altitude = altitude_km * 1000

    radius = EARTH_RADIUS + altitude

    return radius


# ==========================================
# 2. CIRCULAR ORBITAL VELOCITY
# ==========================================

def circular_orbital_velocity(altitude_km):

    r = orbital_radius(altitude_km)

    velocity = np.sqrt(MU / r)

    return velocity


# ==========================================
# 3. ORBITAL PERIOD
# ==========================================

def orbital_period(altitude_km):

    r = orbital_radius(altitude_km)

    period = 2 * np.pi * np.sqrt(r**3 / MU)

    return period


# ==========================================
# 4. ORBITAL ALTITUDE
# ==========================================

def altitude_from_radius(radius_m):

    altitude = radius_m - EARTH_RADIUS

    return altitude


# ==========================================
# 5. VIS-VIVA EQUATION
# ==========================================

def orbital_velocity(radius_m, semi_major_axis_m):

    velocity = np.sqrt(
        MU * (2 / radius_m - 1 / semi_major_axis_m)
    )

    return velocity


# ==========================================
# 6. ORBITAL ENERGY
# ==========================================

def specific_orbital_energy(radius_m, velocity):

    energy = (velocity**2 / 2) - (MU / radius_m)

    return energy
