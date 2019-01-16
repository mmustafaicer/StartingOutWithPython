# kinetic energy

def main():
    mass=float(input("Please enter the object's mass in kg: "))
    velocity=float(input("Please enter the object's velocity in meters per second: "))
    kin_energy=kinetic_energy(mass,velocity)
    print("The total kinetic energy is", format(kin_energy, ",.2f"), "joule")

def kinetic_energy(m,v):
    kin_energy=(1/2)*m*v**2
    return kin_energy

main()

    