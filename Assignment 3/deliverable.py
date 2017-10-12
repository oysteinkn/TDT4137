### Task a ###

# From the graph we read Small: 0.6, Perfect: 0.1, Growing: 0.4, Stable: 0.3.
#
# Rules: AND = min(v0, v1), OR = max(v0, v1), NOT = 1-v
#
# Rule Evaluations:
# Small AND Growing then None = 0.4
# Small AND Stable then SlowDown = 0.3
# Perfect AND Growing then SpeedUp = 0.1
# VeryBig  AND (NOT Growing OR NOT GrowingFast) THEN FloorIt = 0.0
# VerySmall then BrakeHard = 0.0
#
# (0.3(-6-5-4-3)+0.4(-2-1+0+1+2)+0.1(3+4+5+6)) / (4*0.3+5*0.4+4*0.1) = -1
# 
# From the graph we see that the action 'None' has the highest value at -1.
# Hence the action taken is None.


### Task b ###

from math import *

# Container function
def reason(x, y):
  # Intervals on the graph for different actions:
  actions = {'BrakeHard': (-10, -5), 'SlowDown': (-7, -1), 'None':  (-3, 3), 'SpeedUp': (1, 7), 'FloorIt': (5, 10)}
  
  variables = fuzzification(x, y)
  rule_results = rule_evaluation(variables[0], variables[1])
  aggregated_results = aggregate(actions, rule_results)
  center_of_gravity = cog(aggregated_results, actions)
  action = decide(floor(center_of_gravity), actions)

  print("Center of gravity: %.2f" % center_of_gravity)
  print("Action:", action)

#Fuzzification
def fuzzification(x, y):
  distance = {'vs': reverse_grade(x, 0.0, 2.5, 1.0),
              's':  triangle(x, 1.5, 3.0, 4.5, 1.0),
              'p':  triangle(x, 3.5, 5.0, 6.5, 1.0),
              'b':  triangle(x, 5.5, 7.0, 8.5, 1.0),
              'vb': grade(x, 7.5, 10.0, 1.0)}
  delta = { 'sf': reverse_grade(y, -4.0, -2.5, 1.0),
            's':  triangle(y, -3.5, -2, -0.5, 1.0),
            'st': triangle(y, -1.5, 0, 1.5, 1.0),
            'g':  triangle(y, 0.5, 2, 3.5, 1.0),
            'gf': grade(y, 2.5, 4, 1.0)}
  return [distance, delta]

#Rule evaluation
def rule_evaluation(dist, delta):
  results = { 'BrakeHard': dist['vs'],
              'SlowDown': min(dist['s'], delta['st']),
              'None':  min(dist['s'], delta['g']),
              'SpeedUp': min(dist['p'], delta['g']),
              'FloorIt': min (dist['vb'], max(1-delta['g'], 1-delta['gf']))}
  return results

#Aggregation of results from rules
def aggregate(actions, rule_results):
  # Dictionary to store aggregated results
  aggregated_results = {'bh': 0, 'sd': 0, 'n': 0, 'su': 0, 'fi': 0}
  for a in actions.keys():
    v = 0
    for i in range(actions[a][0], actions[a][1]):
      v = v + i
    aggregated_results[a] = v * rule_results[a]
  return aggregated_results

#Calculate center of gravity
def cog(agg, actions):
  numerator = sum(agg.values())
  denominator = 0
  for k in actions.keys():
    denominator = denominator + agg[k] * abs(actions[k][0] - actions[k][1])
  return numerator / denominator

# Choose action from CoG
def decide(z, actions):
  for a in actions.keys():
    if z in range(actions[a][0], actions[a][1]):
      return a

#Helper functions to calculate fuzzy values:
def triangle(pos, x0, x1, x2, clip):
  val = 0.0
  if (pos >= x0 and pos <= x1): val = (pos - x0)/(x1-x0)
  elif (pos >= x1 and pos <= x2): val = (x2-pos)/(x1-x0)
  if val > clip: val = clip
  return val

def grade(pos, x0, x1, clip):
  val = 0.0
  if pos >= x1: val = 1.0
  elif pos <= x0: val = 0.0
  else: val = (pos-x0)/(x1-x0)
  if val > clip: val = clip
  return val

def reverse_grade(pos, x0, x1, clip):
  val = 0.0
  if pos <= x0: val = 1.0
  elif pos >= x1: val = 0.0
  else: val = (pos-x0)/(x1-x0)
  return val

# Reason for the inputs in the assignment:
reason(3.7, 1.2)