#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
        if K >= len(arr):
            arr[:] = arr[:][::-1]
            # if size of group is greater than the size of the array itself, then the entire array will be reversed
        
        else:
            i = K
            l = []  #list to store the last index of each group from the array
            while i < len(arr):
                l.append(i)
                i += K
            #print(l)
            
            j = 0
            for i in range(len(l)):
                arr[j:l[i]] = arr[j:l[i]][::-1]  #reversing each group by using the indices stored in the list l
                j = l[i]
            
            
            arr[l[i]:] = arr[l[i]:][::-1]
        
        
#{ 
 # Driver Code Starts
#Initial template for Python
import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code 