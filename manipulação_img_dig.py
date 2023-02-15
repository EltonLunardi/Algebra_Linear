import numpy as np
import matplotlib.pyplot as plt 
%matplotlib inline
imagem = plt.imread("747273.png")

plt.figure(figsize = (20,6))
plt.imshow(imagem)
plt.box(False)
plt.title("Imagem de um Ramo Estudantil")

