data = {'AND':  [([0,0], 0), ([0,1], 0), ([1,0], 0), ([1,1], 1)],
        'OR':   [([0,0], 0), ([0,1], 1), ([1,0], 1), ([1,1], 1)]}

def learn(data):
  # Initialization
  w = [-.4, .1]       # Start weights
  t = .2              # Theta - Threshold
  a = .1              # Alpha - Learning rate

  # Training loop
  errors = 1
  while errors:                     # Train until there are no errors
    errors = 0
    for p, dy in data:              # Iterate inputs
      # Activation
      s = 0
      for i, j in zip(p, w):        # Calculate sum of weights * inputs
        s += i * j
      y = 0 if (s - t) < 0 else 1   # Output for each input (Step activation)
      error = dy - y                # Calculate error each input

      if error:                     # Count errors
        errors += 1

      # Weight training
      for i, v in enumerate(p):
        w[i] += a * v * error       # New weights from learning rate and error

  print('Final weights:', w, '\n')  # Print the result

print('Training using AND-dataset:')
learn(data['AND'])

print('Training using OR-dataset:')
learn(data['OR'])
