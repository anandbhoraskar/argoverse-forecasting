# In[ ]
import numpy as np
import pickle as pkl
from typing import Any, Dict, List, Tuple
import os
# In[ ]

def save_traj_as_pkl(loadDir, saveDir, start_ind=0):
    print("Loading data from: "+loadDir)
    ls_fnames = os.listdir(loadDir)
    # print(len(ls_fnames))
    print(ls_fnames[:10])
    dic_data = dict()
    print("Total files: %d"%(len(ls_fnames)))
    for fname in ls_fnames:
        with open(loadDir+fname) as fp:
            dt = fp.readlines()
            dt = [np.array([float(s) for s in f[:-1].split(",")[3:5]]) for f in dt if "AGENT" in f]
            dt_np = np.array(dt)[start_ind:]
            dic_data[int(fname[:-4])] = dt_np
        # d2 = Dict(dic_data)
    print("np array sizes: ", dt_np.shape)
    with open(saveDir,"wb") as fp:
        pkl.dump(dic_data, fp)
        print("Saved to: "+saveDir)

# In[ ]

#test
# testDir = "../data/forecasting_test_v1.1/test_obs/data/"
# testsaveDir = "../features/test_traj.pkl"
# save_traj_as_pkl(testDir, testsaveDir, 0)

#val
valDir = "../data/forecasting_val_v1.1/val/data/"
valsaveDir = "../features/val_traj.pkl"
save_traj_as_pkl(valDir, valsaveDir, 20)

#train
# trainDir = "../data/forecasting_train_v1.1/train/data/"
# trainsaveDir = "../features/train_traj.pkl"
# save_traj_as_pkl(trainDir, trainsaveDir, 20)

