myList = [76, 92.3, 'hello', True, 4, 76]

myList.append("apple")        
myList.append(76)              
myList.insert(3, "cat")        
myList.insert(0, 99)           

print(myList.index("hello"))   
print(myList.count(76))        
myList.remove(76)              
myList.pop(myList.index(True)) 

print (myList)
