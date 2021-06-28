please comment if you have any doubts regarding the code.

#this function returns the max value when we modulus of n with k while removing each digit form n.
def max_value(n , k):
        #this line just removes the trailing and starting spaces and tabs 
        n = n.strip()
        #this line converts the n to int and calculates the modulus of n with k and assigns to ans variable
        ans = int(n) % k
        #in this for loop we iterate over the each index in n and for each index we remove the digit number at that index
        #and we convert it to int and we find the modulus with k and checks against the previous ans value if the present modulus 
        #greater than the previous ans value then we replace the ans value with the presen one
        for i in range(len(n)):
                #removing the present index from n
                s = n[:i] + n[i+1:]
                s = int(s) #converting to int
                
                if s % k > ans: #checking if the modulus after the index removal is greater than the previous ans value
                        ans = s%k
        return ans #returning the final ans value


T = int(input())
for _ in range(T):
        n = input()
        k = int(input())
        
        out_ = max_value(n, k)
        print(out_)

