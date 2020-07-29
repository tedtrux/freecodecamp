import numpy as np
def calculate(list):

  list = np.array(list) 

  try:
    list = np.reshape(list, (3,3))
  except:
    raise ValueError("List must contain nine numbers.") 
    
 
  calculations = {
    'mean' : [list.mean(axis=0).tolist(),list.mean(axis=1).tolist(),list.mean()],
    'variance' : [np.var(list, axis=0).tolist(),np.var(list, axis=1).tolist(),np.var(list)] ,
    'standard deviation' : [np.std(list, axis=0).tolist(),np.std(list, axis=1).tolist(),np.std(list)],
    'max' : [np.max(list, axis=0).tolist(),np.max(list, axis=1).tolist(),np.max(list)] ,
    'min' : [np.min(list, axis=0).tolist(),np.min(list, axis=1).tolist(),np.min(list)] ,
    'sum' : [np.sum(list, axis=0).tolist(),np.sum(list, axis=1).tolist(),np.sum(list)] ,
  }

  return calculations



  