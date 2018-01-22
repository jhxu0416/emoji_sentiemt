import re
f = open("glove.twitter.27B.100d.txt", "r")
f_word = open("word_list.txt", "w")
f_mat = open("word_mat.txt", "w")
for j in range(2**20):
    line = re.sub("\n", "", f.readline()).split(" ")
    f_word.write(line[0]+"\n")

    for i in line[1:]:
        f_mat.write(i+" ")
    f_mat.write("\n")

    if j%100 == 0:
        print("Done line {}".format(j))

f_mat.close()
f_word.close()

