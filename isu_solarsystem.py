# -*- coding: utf-8 -*-

from isu import Radius, Mass, Time, Speed, Distance


class Sun():
  radius = Radius(meters = 6.955e8)
  mass = Mass(kilograms = 1.988435e30)
  

class Orbit():
  def __init__(self, a, e=1.0):
    self.semimajor_axis = a
    self.eccentricity = e

  
class Earth():
  radius = Radius(meters = 6.3674447e6)
  equatorial_radius = Radius(6.378137e6)
  polar_radius = Radius(6.3567523142e6)
  year = Time(365.25 * 24 * 60 * 60)
  mass = Mass(kilograms = 6e24)
  orbit =  Orbit(a = Distance(meters = 1.496e11))
  #
  initial_fraction_Uranium_238 = 6e-8


class Jupiter():
  mass = Mass(kilograms = 1.89813e27)
  

# Masses:

class SolarMasses(Mass):
  def __init__(self, sols):
    Mass.__init__(self, kilograms = sols * Sun.mass.kilograms)
    self.sols = float(sols)
  #
  def __str__(self):
    return "{0} M_S".format(self.sols)


class JupiterMasses(Mass):
  def __init__(self, jupiters):
    Mass.__init__(self, kilograms = jupiters * Jupiter.mass.kilograms)
    self.jupiters = float(jupiters)
  #
  def __str__(self):
    return "{0} M_J".format(self.jupiters)


class EarthMasses(Mass):
  def __init__(self, earths):
    Mass.__init__(self, kilograms = earths * Earth.mass.kilograms)
    self.earths = float(earths)
  #
  def __str__(self):
    return "{0} M_E".format(self.earths)


# Years:

class EarthYears(Time):
  def __init__(self, years):
    Time.__init__(self, seconds = years * Earth.year.seconds)
    self.years = float(years)
  #
  def __str__(self):
    return "{0} years".format(self.years)
    
    
# Distances:

class AstronomicalUnits(Distance):
  def __init__(self, astronomical_units):
    Distance.__init__(self, meters = astronomical_units * 1.496e11)
    self.astronomical_units = float(astronomical_units)
  #
  def __str__(self):
    return "{0} AU".format(self.astronomical_units)

