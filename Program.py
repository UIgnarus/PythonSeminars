seq = list(input())
234*9+16
[234,*,9,+,1,6]
parsed_seq=[]

def calculator(seq):
    while '/' in seq or '*' in seq:
        i=seq.find('*')
        if i!=-1:
            res=seq[i-1]*seq[i+1]
            seq.pop(i-1)
            seq[i]=res
            seq.pop(i+1)
        else:
            i=seq.find('/')
            if i!=-1:
                res=seq[i-1]/seq[i+1]
                seq.pop(i-1)
                seq[i]=res
                seq.pop(i+1)
            else:
                break
            
    while '-' in seq or '+' in seq:
        i=seq.find('-')
        if i!=-1:
            res=seq[i-1]-seq[i+1]
            seq.pop(i-1)
            seq[i]=res
            seq.pop(i+1)
        else:
            i=seq.find('+')
            if i!=-1:
                res=seq[i-1]+seq[i+1]
                seq.pop(i-1)
                seq[i]=res
                seq.pop(i+1)
            else:
                break
         
        
i=0
while i<len(seq):
    d=''
    while seq[i].isdigit():
        d+=seq[i]
        i+=1
    parsed_seq.append(int(d))
    
        open.append({2:seq[i]})
    i+=1

[(,234+8)*]
 
