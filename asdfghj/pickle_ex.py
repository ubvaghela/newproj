import pickle
'''cars = ['Audi','BMW','Maruti','Honda']
file = 'mycar.pkl'
fileobj = open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()
'''
file = 'mycar.pkl'
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)