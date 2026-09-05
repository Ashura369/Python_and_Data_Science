# TYPE 1
def addBinary(a, b):
        num1, num2 = len(a)-1, len(b)-1
        in_hand = 0
        result=[]

        while num1>=0 or num2>=0 or in_hand:
            total = in_hand

            if num1 >= 0:
                total += int(a[num1])
                num1 -= 1
            if num2 >= 0:
                total += int(b[num2])
                num2 -= 1
            
            result.append(str(total % 2))                  # storing the result
            in_hand = total // 2                           # storing the remaining values of sum in in_hand
        return "".join(reversed(result))





a = "1010" 
b = "1011"
print(addBinary(a,b))

# TYPE 2

print(int(a, 2))                        # here a is being treated as an int, and 2 here specifies to treat it as 'binary'
print(int(b, 2))

print(bin(int(a,2)))                    # prints as actual binary but need to use slice to remvoe first two elements 
print(bin(int(a,2) + int(b,2))[2:])     # used slice here, now it will print the actual ans









