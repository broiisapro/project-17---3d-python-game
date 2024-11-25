import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ELECTRON_COLOR = (0, 255, 255)  # Cyan color for electrons
FPS = 60

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Atom Simulator")

# Atomic data for elements up to atomic number 100
atomic_data = {
    "Hydrogen": {"symbol": "H", "atomic_number": 1, "mass_number": 1.01, "neutrons": 0, "electrons": "1s1"},
    "Helium": {"symbol": "He", "atomic_number": 2, "mass_number": 4.00, "neutrons": 2, "electrons": "1s2"},
    "Lithium": {"symbol": "Li", "atomic_number": 3, "mass_number": 6.94, "neutrons": 4, "electrons": "1s2 2s1"},
    "Beryllium": {"symbol": "Be", "atomic_number": 4, "mass_number": 9.01, "neutrons": 5, "electrons": "1s2 2s2"},
    "Boron": {"symbol": "B", "atomic_number": 5, "mass_number": 10.81, "neutrons": 6, "electrons": "1s2 2s2 2p1"},
    "Carbon": {"symbol": "C", "atomic_number": 6, "mass_number": 12.01, "neutrons": 6, "electrons": "1s2 2s2 2p2"},
    "Nitrogen": {"symbol": "N", "atomic_number": 7, "mass_number": 14.01, "neutrons": 7, "electrons": "1s2 2s2 2p3"},
    "Oxygen": {"symbol": "O", "atomic_number": 8, "mass_number": 16.00, "neutrons": 8, "electrons": "1s2 2s2 2p4"},
    "Fluorine": {"symbol": "F", "atomic_number": 9, "mass_number": 19.00, "neutrons": 10, "electrons": "1s2 2s2 2p5"},
    "Neon": {"symbol": "Ne", "atomic_number": 10, "mass_number": 20.18, "neutrons": 10, "electrons": "1s2 2s2 2p6"},
    "Sodium": {"symbol": "Na", "atomic_number": 11, "mass_number": 22.99, "neutrons": 12, "electrons": "1s2 2s2 2p6 3s1"},
    "Magnesium": {"symbol": "Mg", "atomic_number": 12, "mass_number": 24.31, "neutrons": 12, "electrons": "1s2 2s2 2p6 3s2"},
    "Aluminium": {"symbol": "Al", "atomic_number": 13, "mass_number": 26.98, "neutrons": 14, "electrons": "1s2 2s2 2p6 3s2 3p1"},
    "Silicon": {"symbol": "Si", "atomic_number": 14, "mass_number": 28.09, "neutrons": 14, "electrons": "1s2 2s2 2p6 3s2 3p2"},
    "Phosphorus": {"symbol": "P", "atomic_number": 15, "mass_number": 30.97, "neutrons": 16, "electrons": "1s2 2s2 2p6 3s2 3p3"},
    "Sulfur": {"symbol": "S", "atomic_number": 16, "mass_number": 32.07, "neutrons": 16, "electrons": "1s2 2s2 2p6 3s2 3p4"},
    "Chlorine": {"symbol": "Cl", "atomic_number": 17, "mass_number": 35.45, "neutrons": 18, "electrons": "1s2 2s2 2p6 3s2 3p5"},
    "Argon": {"symbol": "Ar", "atomic_number": 18, "mass_number": 39.95, "neutrons": 22, "electrons": "1s2 2s2 2p6 3s2 3p6"},
    "Potassium": {"symbol": "K", "atomic_number": 19, "mass_number": 39.10, "neutrons": 20, "electrons": "1s2 2s2 2p6 3s2 3p6 4s1"},
    "Calcium": {"symbol": "Ca", "atomic_number": 20, "mass_number": 40.08, "neutrons": 20, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2"},
    "Scandium": {"symbol": "Sc", "atomic_number": 21, "mass_number": 44.96, "neutrons": 24, "electrons": "1s2 2s2 2p6 3s2 3p6 3d1"},
    "Titanium": {"symbol": "Ti", "atomic_number": 22, "mass_number": 47.87, "neutrons": 26, "electrons": "1s2 2s2 2p6 3s2 3p6 3d2"},
    "Vanadium": {"symbol": "V", "atomic_number": 23, "mass_number": 50.94, "neutrons": 28, "electrons": "1s2 2s2 2p6 3s2 3p6 3d3"},
    "Chromium": {"symbol": "Cr", "atomic_number": 24, "mass_number": 51.99, "neutrons": 28, "electrons": "1s2 2s2 2p6 3s2 3p6 3d5"},
    "Manganese": {"symbol": "Mn", "atomic_number": 25, "mass_number": 54.94, "neutrons": 30, "electrons": "1s2 2s2 2p6 3s2 3p6 3d5 4s2"},
    "Iron": {"symbol": "Fe", "atomic_number": 26, "mass_number": 55.85, "neutrons": 30, "electrons": "1s2 2s2 2p6 3s2 3p6 3d6 4s2"},
    "Cobalt": {"symbol": "Co", "atomic_number": 27, "mass_number": 58.93, "neutrons": 32, "electrons": "1s2 2s2 2p6 3s2 3p6 3d7 4s2"},
    "Nickel": {"symbol": "Ni", "atomic_number": 28, "mass_number": 58.69, "neutrons": 31, "electrons": "1s2 2s2 2p6 3s2 3p6 3d8 4s2"},
    "Copper": {"symbol": "Cu", "atomic_number": 29, "mass_number": 63.55, "neutrons": 35, "electrons": "1s2 2s2 2p6 3s2 3p6 3d10 4s1"},
    "Zinc": {"symbol": "Zn", "atomic_number": 30, "mass_number": 65.38, "neutrons": 35, "electrons": "1s2 2s2 2p6 3s2 3p6 3d10 4s2"},
    "Gallium": {"symbol": "Ga", "atomic_number": 31, "mass_number": 69.72, "neutrons": 39, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p1"},
    "Germanium": {"symbol": "Ge", "atomic_number": 32, "mass_number": 72.63, "neutrons": 41, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p2"},
    "Arsenic": {"symbol": "As", "atomic_number": 33, "mass_number": 74.92, "neutrons": 42, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p3"},
    "Selenium": {"symbol": "Se", "atomic_number": 34, "mass_number": 78.96, "neutrons": 45, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p4"},
    "Bromine": {"symbol": "Br", "atomic_number": 35, "mass_number": 79.90, "neutrons": 45, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p5"},
    "Krypton": {"symbol": "Kr", "atomic_number": 36, "mass_number": 83.80, "neutrons": 48, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6"},
    "Rubidium": {"symbol": "Rb", "atomic_number": 37, "mass_number": 85.47, "neutrons": 48, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1"},
    "Strontium": {"symbol": "Sr", "atomic_number": 38, "mass_number": 87.62, "neutrons": 50, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2"},
    "Yttrium": {"symbol": "Y", "atomic_number": 39, "mass_number": 88.91, "neutrons": 50, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d1"},
    "Zirconium": {"symbol": "Zr", "atomic_number": 40, "mass_number": 91.22, "neutrons": 51, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d2"},
    "Niobium": {"symbol": "Nb", "atomic_number": 41, "mass_number": 92.91, "neutrons": 52, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d3"},
    "Molybdenum": {"symbol": "Mo", "atomic_number": 42, "mass_number": 95.95, "neutrons": 54, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d4"},
    "Technetium": {"symbol": "Tc", "atomic_number": 43, "mass_number": 98.00, "neutrons": 55, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d5"},
    "Ruthenium": {"symbol": "Ru", "atomic_number": 44, "mass_number": 101.07, "neutrons": 57, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d6"},
    "Rhodium": {"symbol": "Rh", "atomic_number": 45, "mass_number": 102.91, "neutrons": 58, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d7"},
    "Palladium": {"symbol": "Pd", "atomic_number": 46, "mass_number": 106.42, "neutrons": 60, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d8"},
    "Silver": {"symbol": "Ag", "atomic_number": 47, "mass_number": 107.87, "neutrons": 61, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s1 4d10"},
    "Cadmium": {"symbol": "Cd", "atomic_number": 48, "mass_number": 112.41, "neutrons": 64, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10"},
    "Indium": {"symbol": "In", "atomic_number": 49, "mass_number": 114.82, "neutrons": 66, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p1"},
    "Tin": {"symbol": "Sn", "atomic_number": 50, "mass_number": 118.71, "neutrons": 69, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p2"},
    "Antimony": {"symbol": "Sb", "atomic_number": 51, "mass_number": 121.76, "neutrons": 71, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p3"},
    "Tellurium": {"symbol": "Te", "atomic_number": 52, "mass_number": 127.60, "neutrons": 76, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p4"},
    "Iodine": {"symbol": "I", "atomic_number": 53, "mass_number": 126.90, "neutrons": 74, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p5"},
    "Xenon": {"symbol": "Xe", "atomic_number": 54, "mass_number": 131.29, "neutrons": 77, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6"},
    "Cesium": {"symbol": "Cs", "atomic_number": 55, "mass_number": 132.91, "neutrons": 78, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s1"},
    "Barium": {"symbol": "Ba", "atomic_number": 56, "mass_number": 137.33, "neutrons": 81, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2"},
    "Lanthanum": {"symbol": "La", "atomic_number": 57, "mass_number": 138.91, "neutrons": 82, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 5d1"},
    "Cerium": {"symbol": "Ce", "atomic_number": 58, "mass_number": 140.12, "neutrons": 82, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f1"},
    "Praseodymium": {"symbol": "Pr", "atomic_number": 59, "mass_number": 140.91, "neutrons": 82, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f3"},
    "Neodymium": {"symbol": "Nd", "atomic_number": 60, "mass_number": 144.24, "neutrons": 84, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f4"},
    "Promethium": {"symbol": "Pm", "atomic_number": 61, "mass_number": 145.00, "neutrons": 84, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f5"},
    "Samarium": {"symbol": "Sm", "atomic_number": 62, "mass_number": 150.36, "neutrons": 88, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f6"},
    "Europium": {"symbol": "Eu", "atomic_number": 63, "mass_number": 151.98, "neutrons": 89, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7"},
    "Gadolinium": {"symbol": "Gd", "atomic_number": 64, "mass_number": 157.25, "neutrons": 93, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f7 5d1"},
    "Terbium": {"symbol": "Tb", "atomic_number": 65, "mass_number": 158.93, "neutrons": 94, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f9"},
    "Dysprosium": {"symbol": "Dy", "atomic_number": 66, "mass_number": 162.50, "neutrons": 96, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f10"},
    "Holmium": {"symbol": "Ho", "atomic_number": 67, "mass_number": 164.93, "neutrons": 98, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f11"},
    "Erbium": {"symbol": "Er", "atomic_number": 68, "mass_number": 167.26, "neutrons": 99, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f12"},
    "Thulium": {"symbol": "Tm", "atomic_number": 69, "mass_number": 168.93, "neutrons": 100, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f13"},
    "Ytterbium": {"symbol": "Yb", "atomic_number": 70, "mass_number": 173.04, "neutrons": 103, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14"},
    "Lutetium": {"symbol": "Lu", "atomic_number": 71, "mass_number": 175.00, "neutrons": 104, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d1"},
    "Hafnium": {"symbol": "Hf", "atomic_number": 72, "mass_number": 178.49, "neutrons": 106, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d2"},
    "Tantalum": {"symbol": "Ta", "atomic_number": 73, "mass_number": 180.95, "neutrons": 108, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d3"},
    "Tungsten": {"symbol": "W", "atomic_number": 74, "mass_number": 183.84, "neutrons": 110, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d4"},
    "Rhenium": {"symbol": "Re", "atomic_number": 75, "mass_number": 186.21, "neutrons": 111, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d5"},
    "Osmium": {"symbol": "Os", "atomic_number": 76, "mass_number": 190.23, "neutrons": 114, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d6"},
    "Iridium": {"symbol": "Ir", "atomic_number": 77, "mass_number": 192.22, "neutrons": 115, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d7"},
    "Platinum": {"symbol": "Pt", "atomic_number": 78, "mass_number": 195.08, "neutrons": 117, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d8"},
    "Gold": {"symbol": "Au", "atomic_number": 79, "mass_number": 196.97, "neutrons": 118, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10"},
    "Mercury": {"symbol": "Hg", "atomic_number": 80, "mass_number": 200.59, "neutrons": 121, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2"},
    "Thallium": {"symbol": "Tl", "atomic_number": 81, "mass_number": 204.38, "neutrons": 123, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p1"},
    "Lead": {"symbol": "Pb", "atomic_number": 82, "mass_number": 207.2, "neutrons": 125, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p2"},
    "Bismuth": {"symbol": "Bi", "atomic_number": 83, "mass_number": 208.98, "neutrons": 126, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p3"},
    "Polonium": {"symbol": "Po", "atomic_number": 84, "mass_number": 209.98, "neutrons": 126, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p4"},
    "Astatine": {"symbol": "At", "atomic_number": 85, "mass_number": 210.00, "neutrons": 125, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p5"},
    "Radon": {"symbol": "Rn", "atomic_number": 86, "mass_number": 222.00, "neutrons": 136, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p6"},
    "Francium": {"symbol": "Fr", "atomic_number": 87, "mass_number": 223.00, "neutrons": 136, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p7"},
    "Radium": {"symbol": "Ra", "atomic_number": 88, "mass_number": 226.00, "neutrons": 138, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p8"},
    "Actinium": {"symbol": "Ac", "atomic_number": 89, "mass_number": 227.00, "neutrons": 138, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p9"},
    "Thorium": {"symbol": "Th", "atomic_number": 90, "mass_number": 232.04, "neutrons": 142, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p10"},
    "Protactinium": {"symbol": "Pa", "atomic_number": 91, "mass_number": 231.04, "neutrons": 140, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p11"},
    "Uranium": {"symbol": "U", "atomic_number": 92, "mass_number": 238.03, "neutrons": 146, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p12"},
    "Neptunium": {"symbol": "Np", "atomic_number": 93, "mass_number": 237.00, "neutrons": 144, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p13"},
    "Plutonium": {"symbol": "Pu", "atomic_number": 94, "mass_number": 244.00, "neutrons": 150, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p14"},
    "Americium": {"symbol": "Am", "atomic_number": 95, "mass_number": 243.00, "neutrons": 148, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p15"},
    "Curium": {"symbol": "Cm", "atomic_number": 96, "mass_number": 247.00, "neutrons": 151, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p16"},
    "Berkelium": {"symbol": "Bk", "atomic_number": 97, "mass_number": 247.00, "neutrons": 150, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p17"},
    "Californium": {"symbol": "Cf", "atomic_number": 98, "mass_number": 251.00, "neutrons": 153, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p18"},
    "Einsteinium": {"symbol": "Es", "atomic_number": 99, "mass_number": 252.00, "neutrons": 153, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p19"},
    "Fermium": {"symbol": "Fm", "atomic_number": 100, "mass_number": 257.00, "neutrons": 157, "electrons": "1s2 2s2 2p6 3s2 3p6 4s2 3d10 4p6 5s2 4d10 5p6 6s2 4f14 5d10 6s2 6p20"}
}


def draw_atom(nucleus_x, nucleus_y, element_name, time):
    element = atomic_data[element_name]
    num_electrons = element["atomic_number"]
    
    # Draw the nucleus
    pygame.draw.circle(screen, WHITE, (nucleus_x, nucleus_y), 10)
    
    # Electron shells
    electrons_remaining = num_electrons
    shell_electrons = []

    for capacity in [2, 8, 18, 32, 50, 72, 98]:  # Typical shell capacities
        electrons_in_shell = min(electrons_remaining, capacity)
        shell_electrons.append(electrons_in_shell)
        electrons_remaining -= electrons_in_shell
        if electrons_remaining <= 0:
            break

    # Draw electrons in shells
    for shell_index, electron_count in enumerate(shell_electrons):
        radius = 50 + shell_index * 30  # Increase radius for each shell
        for i in range(electron_count):
            angle = (i * (360 / electron_count) + time) % 360  # Rotate electrons
            rad_angle = math.radians(angle)
            electron_x = nucleus_x + int(radius * math.cos(rad_angle))
            electron_y = nucleus_y + int(radius * math.sin(rad_angle))
            pygame.draw.circle(screen, ELECTRON_COLOR, (electron_x, electron_y), 5)

    # Draw element details
    font = pygame.font.SysFont(None, 24)
    details_texts = [
        f"Element: {element_name}",
        f"Symbol: {element['symbol']}",
        f"Atomic Number: {element['atomic_number']}",
        f"Mass Number: {element['mass_number']}",
        f"Protons: {element['atomic_number']}",
        f"Neutrons: {element['neutrons']}",
        f"Electrons: {num_electrons}",
        f"Charge: Neutral"
    ]
    
    for idx, text in enumerate(details_texts):
        rendered_text = font.render(text, True, WHITE)
        screen.blit(rendered_text, (nucleus_x + 150, nucleus_y - 100 + idx * 20))

def draw_buttons():
    increase_button = pygame.Rect(850, 100, 100, 50)
    decrease_button = pygame.Rect(850, 200, 100, 50)

    pygame.draw.rect(screen, WHITE, increase_button)
    pygame.draw.rect(screen, WHITE, decrease_button)

    font = pygame.font.SysFont(None, 36)
    inc_text = font.render('+', True, BLACK)
    dec_text = font.render('-', True, BLACK)

    screen.blit(inc_text, (880, 110))
    screen.blit(dec_text, (880, 210))

    return increase_button, decrease_button

running = True
clock = pygame.time.Clock()

elements_list = list(atomic_data.keys())
current_element_index = 0
time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            increase_button, decrease_button = draw_buttons()
            if increase_button.collidepoint(mouse_pos):
                current_element_index = (current_element_index + 1) % len(elements_list)
            elif decrease_button.collidepoint(mouse_pos):
                current_element_index = (current_element_index - 1) % len(elements_list)

    screen.fill(BLACK)

    # Increment time for animation
    time += 1

    # Get the current element's name and draw it
    current_element_name = elements_list[current_element_index]
    draw_atom(WIDTH // 2 - 100, HEIGHT // 2, current_element_name, time)

    # Draw buttons
    draw_buttons()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
