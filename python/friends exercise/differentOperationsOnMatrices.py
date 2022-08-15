A=[[1,2,3],[2,3,6],[7,8,9]]

def detOfMatrix(A):
    original=tuple(A)
    if len(A)==2:
        return (A[0][0]*A[1][1])-(A[0][1]*A[1][0])
    elif len(A)==1:
        return A[0][0]
    count=0
    for i in range(len(A)):
        del(A[0])
        print(original,'and',A)
        # print(i, len(A), end='')
        for j in range(len(A)):
            A[j].pop(i)
        minor=detOfMatrix(A) 
        cofactor=((-1)**(i))*minor
        count=count+(original[0][i]*cofactor)
        if i==1:
            break
        # print(count)
        A=list[original]
    return count
    
print(detOfMatrix(A))