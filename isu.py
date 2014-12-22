#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


class Mass():
  def __init__(self, kilogrammes):
    self.kilogrammes = float(kilogrammes)
  #
  def __str__(self):
    return "{0} kg".format(self.kilogrammes)


class Energy():
  def __init__(self, joules):
    self.joules = joules
  #
  def __str__(self):
    return "{0} J".format(self.joules)


class Distance():
  def __init__(self, meters):
    self.meters = meters
  #
  def __str__(self):
    return "{0} m".format(self.meters)
    
#AstronomicalUnit = Distance(meters = 1.496e11)


class Time():
  def __init__(self, seconds):
    self.seconds = seconds
  #
  def __str__(self):
    return "{0} s".format(self.seconds)


class Radius():
  def __init__(self, meters):
    self.meters = meters
  #
  def __str__(self):
    return "{0} m".format(self.meters)

    
class Velocity():
  def __init__(self, meters_per_second):
    self.meters_per_second = float(meters_per_second)
    # and direction TODO
  #
  def __str__(self):
    return "{0} m/s".format(self.meters_per_second)

class Speed():
  def __init__(self, meters_per_second):
    self.meters_per_second = float(meters_per_second)
  #
  def __str__(self):
    return "{0} m/s".format(self.meters_per_second)

SpeedOfLight = Speed(meters_per_second = 3.0e8)

    
class Acceleration():
  def __init__(self, meters_per_second2):
    self.meters_per_second2 = meters_per_second2
  #
  def __str__(self):
    return "{0} m/s²".format(self.meters_per_second2)
    
    
class Power():
  def __init__(self, watts):
    self.watts = watts
  #
  def __str__(self):
    return "{0} W".format(self.watts)

class Luminosity():
  def __init__(self, watts):
    self.watts = watts
  #
  def __str__(self):
    return "{0} W".format(self.watts)

class StefanBoltzmannConstant():
  watts_per_meter2_per_kelvin4 = 5.67e-8

    
class EnergyFlux():
  def __init__(self, watts_per_meter2):
    self.watts_per_meter2 = watts_per_meter2
  #
  def __str__(self):
    return "{0} W/m²".format(self.watts_per_meter2)


class Force():
  def __init__(self, newtons):
    self.newtons = newtons
  #
  def __str__(self):
    return "{0} N".format(self.newtons)


class Area():
  def __init__(self, meters2):
    self.meters2 = meters2
  #
  def __str__(self):
    return "{0} m²".format(self.meters2)


class Pressure():
  def __init__(self, newtons_per_meter2):
    self.newtons_per_meter2 = newtons_per_meter2
  #
  def __str__(self):
    return "{0} N/m²".format(self.newtons_per_meter2)


class Temperature():
  symbol = 't'
  zero_celsius = 273.15 # ...check this TODO
  
  def __init__(self, kelvin):
    self.kelvin = float(kelvin)
  #
  def __str__(self):
    return "{0} K".format(self.kelvin)


class Density():
  symbol = 'ρ'
  def __init__(self, kilogrammes_per_meter3):
    self.kilogrammes_per_meter3 = float(kilogrammes_per_meter3)
  #
  def __str__(self):
    return "{0} kg/m³".format(self.kilogrammes_per_meter3)
  
  # Static constructor methods...
  
  @staticmethod
  def g_per_cm3(g_per_cm3):
    kg_per_meter3 = g_per_cm3 * 1e3
    return Density(kg_per_meter3)


