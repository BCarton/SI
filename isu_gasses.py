# -*- coding: utf-8 -*-

import math

from isu import Velocity, Temperature


class MolecularMass():
  symbol = 'μ'
  def __init__(self, number):
    self.number = number


class IdealGas():
  def __init__(self, molecular_mass):
    self.molecular_mass = molecular_mass
  
  """
  def get_meankineticenergy(temperature):
    # See: http://en.wikipedia.org/wiki/Kinetic_theory#Temperature_and_kinetic_energy
    return None
  """
  
  def get_averagevelocity(self, temperature):
    return Velocity(meters_per_second = 1e3 * 0.157 * math.sqrt(temperature.kelvin / float(self.molecular_mass.number)))

