import csv 


#prep
f = open("cereal.csv", 'r') 
reader = csv.reader(f)
header = next(reader)
header = next(reader)

#dict
cBrand = {}
healthy_cBrand = []
rating = 0
x = ""

for row in reader: 
    #get cereal name, sodium, sugar   
    cBrand = {'cereal':row[0], 'sodium': row[6], 'sugar': row[9]}
    #if cereal has 0 sodium AND 0 sugar, get cereal in healthly_cBrand List
    if(cBrand['sodium'] == '0' and cBrand['sugar'] == '0'):
        healthy_cBrand.append(cBrand['cereal']) 

    #Extra: compare ratings and get the best one
    rat = float(row[15])
    if (rat > rating): 
        rating = rat
        x = row[0]
        
print("These are some healthly choices of cereal: ", healthy_cBrand) #base project 
print(x, "cereal has the highest rating of", rating) #Extra 





    
    
   
        



