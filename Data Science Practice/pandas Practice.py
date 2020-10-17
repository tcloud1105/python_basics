import pandas as pd
import numpy as np

df1 = pd.DataFrame([[1,2,3],[10,20,30]], columns=['Price','Age','Value'], index=['First','Second'])
df2 = pd.DataFrame([{"Name":"jean","Surname":"cedric"},{"Name":"Jacobs"}])

# numpy array
n = np.arange(27)
n.reshape(3, 9) # n.reshape(3,3,3)
np.asarray([1,2,3])