#Run this code from terminal

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt


digits = load_digits()
plt.gray()
plt.matshow(digits.images[5])
plt.show()
