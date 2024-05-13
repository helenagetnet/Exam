#1
def find (list , key):
    list = [1,2,3,4]
    key =3
    for i in list :
        if i != key:
            return 'no' 
        else:
            return 'yes'
print (find(list , key))
        