def reason(x, y):
  variables = fuzzification(x, y)
  actions = rule_evaluation(variables[0], variables[1])


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
  actions = { 'bh': dist['vs'],
              'sd': min(dist['s'], delta['st']),
              'n':  min(dist['s'], delta['g']),
              'su': min(dist['p'], delta['g']),
              'fi': min (dist['vb'], max(1-delta['g'], 1-delta['gf']))}
  return actions

def 

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