import math


def calculate_volume_of_sphere(radius):
    """Return the volume of a sphere with the given radius: (4/3) * pi * r^3."""
    return (4 / 3) * math.pi * radius ** 3


# Compute and print the volume of spheres with radii 30 and 40
for r in (30, 40):
    print(f"Volume of sphere with radius {r}: {calculate_volume_of_sphere(r):.2f}")