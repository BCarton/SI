#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

from isu import Density


class Iron():
  density = Density(kilogrammes_per_meter3 = 7874)


class Water():
  density = Density(kilogrammes_per_meter3 = 1000)


class WaterIce():
  density = Density(kilogrammes_per_meter3 = 900)


class Rock():
  density = Density(kilogrammes_per_meter3 = 3000)


class Uranium_238():
  symbol = 'U₂₃₈' # also 'U₂₃₅'
  decay_rate_lambda = 0.155 # per_Gyr
  energy_production_Edot = 9.46e-5 # W/kg
