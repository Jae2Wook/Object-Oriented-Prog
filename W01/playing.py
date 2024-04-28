# %%
print('Hello World')
name = input("what is your name: ")
print("hello", name)

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show()