while True:
    sen =input(' Enetr your string and k: ')
    
 
#checking the sen is str or not
    if  sen.isnumeric():
        print('please enter a string ')
    else: 
        break

    
#function

    
def pancake_scramble(sen):
    lensen = len(sen)
    for k in range (0,lensen):
       print ( sen[k::-1] + sen[k+1:])
         

print(pancake_scramble(sen))


        
    



    
        
