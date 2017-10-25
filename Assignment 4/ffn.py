from pybrain.datasets import SupervisedDataSet
from pybrain.structure import TanhLayer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

# Dataset for training
ds = SupervisedDataSet(1, 1) # One variable, one desired output
for i in range(1, 9):        # Add numbers 1-8
  ds.addSample(i, i)

# Dataset for testing 
ds2 = SupervisedDataSet(1, 1)
ds2.addSample(-1, -1)
ds2.addSample(-40, -40)
ds2.addSample(20, 20)
ds2.addSample(3.4, 3.4)
ds2.addSample(6.2, 6.2)
ds2.addSample(54, 54)
ds2.addSample(500, 500)

net = buildNetwork(1, 8, 1, hiddenclass=TanhLayer)
trainer = BackpropTrainer(net, ds)

trainer.trainUntilConvergence(verbose=False, validationProportion=0.15, maxEpochs=1000, continueEpochs=10)

print(net.activateOnDataset(ds))    # Print results from training set
print(net.activateOnDataset(ds2))   # Print results from testing set
