decimal_number = 100
binary_number = 0
flag = 0
temp = decimal_number
ones_Complement = 0

def decToBin( decimal_number ):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 *
                decToBin(int(decimal_number // 2)))
 
binary_number = (decToBin(decimal_number))
print(binary_number)


def binToOne(bin,temp):
  if bin == 0 :
    return temp;
  else : 
    ones_Complement = binToOne(bin//10, temp*10 + bin%10)
    return ones_Complement
    
print("one's complemet is : {}" .format(binToOne(binary_number,0)))
