import fasttext

# Skipgram model :
model = fasttext.train_unsupervised('t1.txt', model='skipgram')
model.save_model("t1.bin")

print("t1 done")
# Skipgram model :
model = fasttext.train_unsupervised('t2.txt', model='skipgram')
model.save_model("t2.bin")
print("t2 done")