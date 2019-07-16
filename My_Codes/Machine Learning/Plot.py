import pandas as pd
import matplotlib.pyplot as plt

frame = pd.DataFrame([1,2,3,4,5,1,1,2,2,2,2,2,2,5,4,4,3,3,5])
print(frame)

frame.plot(kind="hist")
plt.show()
