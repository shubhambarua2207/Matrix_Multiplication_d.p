def matmul(A):

    a={}

    for i in range(len(A)-1):
        for j in range(0,len(A)-i-1):

            if i==0:
                b=(j,j)
                a[b]=0

            elif i==1:
                b=(j,j+1)
                a[b]=A[j]*A[j+1]*A[j+2]

            else:
                b=(j,j+i)
                a[b]=float('inf')

                for k in range(j,j+i):
                    hold=a[(j,k)]+a[(k+1,j+i)]+A[j]*A[k+1]*A[j+i+1]

                    if hold<a[b]:
                        a[b]=hold

    print(a[(0,len(A)-2)])
    print(a)

a=[1,2,3,4]
matmul(a)
