class Physics:
    def __init__(self):
        # Gravitational constant in N·m²/kg²
        self.G = 6.67430e-11
        # Acceleration due to gravity in m/s²
        self.g = 9.81

    def gravitational_force(self, m1, m2, r):
        if r == 0:
            raise ValueError("Distance cannot be zero.")
        force = self.G * m1 * m2 / (r ** 2)
        return force

    def kinetic_energy(self, m, v):
        return 0.5 * m * v ** 2

    def potential_energy(self, m, h):
        return m * self.g * h


if __name__ == "__main__":

    physics = Physics()

    earth_mass = 5.972e24 
    moon_mass = 7.348e22  
    distance = 3.84e8   
    
    try:
        force = physics.gravitational_force(earth_mass, moon_mass, distance)
        print(f"Gravitational Force between Earth and Moon: {force:.2e} N")
    except Exception as e:
        print("Error calculating gravitational force:", e)
    
    mass_object = 5         
    velocity = 10           
    ke = physics.kinetic_energy(mass_object, velocity)
    print(f"Kinetic Energy of a 5 kg object moving at 10 m/s: {ke:.2f} J")

    height = 10             
    pe = physics.potential_energy(mass_object, height)
    print(f"Potential Energy of a 5 kg object at 10 m height: {pe:.2f} J")
