from math import floor

def solve (Q, query):
        result = []
        for i in range(Q):
                a,b=query[i]
                x,af,bf,c=0,0,0,0
                for i in range(2,1000000000,2):
                    x+=i*(i+1)
                    if a<=x and af==0:
                        ac,af,ai,ax=c,1,i,x-i*(i+1)
                    if b<=x and bf==0:
                        bc,bf,bi,bx=c,1,i,x-i*(i+1)
                    if af and bf:break
                    c+=i+1
                ar,br=(a-ax)/ai,(b-bx)/bi
                if ar>int(ar):ar=ar+1
                if br>int(br):br=br+1
                result.append((bc+int(br))-(ac+int(ar))+1)

        return result                           



Q = int(input())
query = [list(map(int, input().split())) for i in range(Q)]

out_ = solve(Q, query)
print (' '.join(map(str, out_)))

