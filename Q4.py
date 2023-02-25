#Q4) given two arrays as constant for example A=[1,2,4,6] B=[2,3,6]
# you should be able to merge them so
# the output will be C=[1,2,2,3,4,6,6]
A=[1,2,4,6]
B=[2,3,6]
C=[]
i=0
s=0
d=0
for i in range(len(A)+len(B)):

    if s==len(A):
        C.append(B[d:])
    break

    if d==len(B):
        C.append(A[s:])
        break


  if A[s]<B[d]:
      C.append(A[s])
      s=s+1
  else:
      print("ss")
      C.append(B[d])
      d=d+1