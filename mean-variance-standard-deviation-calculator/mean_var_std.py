import numpy as np

def calculate(lists):
    try:
      convertList = np.reshape(lists,(3,3))
      calculations = {
        'mean': [np.mean(convertList,axis=0).tolist(),np.mean(convertList,axis=1).tolist(),np.mean(convertList)],
        'variance':[np.var(convertList,axis=0).tolist(),np.var(convertList,axis=1).tolist(),np.var(convertList)],
        'standard deviation':[np.std(convertList,axis=0).tolist(),np.std(convertList,axis=1).tolist(),np.std(convertList)],
        'max':[np.max(convertList,axis=0).tolist(),np.max(convertList,axis=1).tolist(),np.max(convertList)],
        'min':[np.min(convertList,axis=0).tolist(),np.min(convertList,axis=1).tolist(),np.min(convertList)],
        'sum':[np.sum(convertList,axis=0).tolist(),np.sum(convertList,axis=1).tolist(),np.sum(convertList)],
      }
    except ValueError:
      raise ValueError("List must contain nine numbers.")
    return calculations