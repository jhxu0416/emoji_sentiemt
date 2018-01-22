import numpy as np
with open("word_list.txt", "r") as f:
    word_list = f.read().split("\n")

mat = np.loadtxt("word_mat.txt")
np.save("weight.npy",mat)
