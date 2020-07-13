import numpy as np
import sgdml.train as train

dataset_path = '/Users/elilipsman/Eli_Project/sGDML/sgdml-debug/4H2O-2mer-dataset.npz'
dataset = np.load(dataset_path)
dataset_dict = dict(dataset)

#print(dataset_dict['R'].shape[0])
print(dataset.files)
#print(dataset.f.z)


test = train.GDMLTrain()
task = test.create_task(dataset_dict, 100, dataset_dict, 100, 30)
#print(task['R_train'].reshape(100,-1).shape)
model = test.train(task)

#print(model['R_desc'][0].shape)

print(model)





pass