def checkIfMAtrix(A):
    count=0
    for i in range(1,len(A)):
        if len(A[i])==len(A[i-1]):
            count+=1
    if count==len(A)-1:
        return True
    else:
        return False
def checkIfSquareMatrix(A):
    count=0
    for i in range(len(A)):
        if len(A)==len(A[i]):
            count+=1
    if count==len(A):
        return True
    else:
        return False
def productOfMatrices(A,B):
    if len(A[0])==len(B):
        pass
    else:
        return 'given matrices can\'t be multiplied'
    AXB=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(B[0])):
            count=0
            for k in range(len(A[0])):
                count=count+A[i][k]*B[k][j]
            row.append(count)
        AXB.append(row)
    return AXB
def transposeOfMatrices(A):
    transpose=[]
    for i in range(len(A[0])):
        row=[]
        for j in range(len(A)):
            element=A[j][i]
            row.append(element)
        transpose.append(row)
    return transpose
def detOfOrd1Matrix(A):
    return A[0][0]
def detOfORd2Matrix(A):
    det=(A[0][0]*A[1][1])-(A[0][1]*A[1][0])
    return det
def detOfMatrix(A):
    if len(A)==2:
        return detOfORd2Matrix(A)
    elif len(A)==1:
        return detOfOrd1Matrix(A)
    original=A
    count=0
    for i in range(len(A)):
        A.pop(0)
        for j in range(len(A)):
            A[j].pop(i)
        minor=detOfMatrix(A) 
        cofactor=((-1)**(i))*minor
        count=count+(original[0][i]*cofactor)
        A=original
    return count
        # cofactor=detOfMAtrix()
    
A=[[1,2,3],[2,4,6],[7,8,9]]
B=[[1,1,1],[2,2,2],[2,5,8]]
# print(detOfMatrix(A))
# for i in range(len(A)):
#     print(A[0][i])
print(detOfMatrix(A))
    








# def minorOfAnElement(A[i][j]):


# def determinantOfMAtrices(A):

    
# A=[[1,2,3],[4,5,6],[7,8,9]]
# B=[[1,1,3],[5,2,6],[-2,-1,-3]]
# c=productOfMatrices(A,A)
# print(productOfMatrices(c,A))
# print(c)
# M=[[1,1],[2,2]]
# print(detOfORd2Matrix(M))


