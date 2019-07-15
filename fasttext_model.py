import fasttext

# Skipgram model :
model = fasttext.train_unsupervised('dta18.txt', model='skipgram', dim=512)
model.save_model("t1.bin")

print("t1 done")
# Skipgram model :
model = fasttext.train_unsupervised('dta19.txt', model='skipgram',  dim=512)
model.save_model("t2.bin")
print("t2 done")