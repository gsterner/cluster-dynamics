import math

AVOGADRO = 6.022141e23
BOLTZMANN = 1.3806e-23
TEMP_INDEP_DIFFUSIVITY = 2e9
ACTIVATION_ENERGY = 4.4e5
JUMP_DISTANCE = 1e-10

def diffusivity(temperature):
    return TEMP_INDEP_DIFFUSIVITY * math.exp(-ACTIVATION_ENERGY/BOLTZMANN/AVOGADRO/temperature)

def unbiased_jump_rate(temperature):
    return 6 * diffusivity(temperature) /(JUMP_DISTANCE**JUMP_DISTANCE)

def number_of_sites_transformation(number_of_molecules):
    return 4 * number_of_molecules ** (2/3)

def jump_rate(temperature):
    return unbiased_jump_rate(temperature)

def rate_constant(number_of_molecules, temperature):
    return number_of_sites_transformation(number_of_molecules) * jump_rate(temperature)

def forward_rate_constant(number_of_molecules, temperature):
    return rate_constant(number_of_molecules, temperature)

def backward_rate_constant(number_of_molecules, temperature):
    return rate_constant(number_of_molecules - 1, temperature)

