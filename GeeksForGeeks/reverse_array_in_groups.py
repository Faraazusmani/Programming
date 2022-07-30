'''
Question - 

Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.
 

Example 2:

Input:
N = 4, K = 3
arr[] = {5,6,8,9}
Output: 8 6 5 9
 

Your Task:
You don't need to read input or print anything. The task is to complete the function reverseInGroups() which takes the array, N and K as input parameters and modifies the array in-place. 

 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

 

Constraints:
1 ≤ N, K ≤ 107
1 ≤ A[i] ≤ 1018

'''

'''
Approach - 

assuming 0 indexed array

Store the indices of last elements of each group from the given array.
Example - arr = [1,2,3,4,5,6,8,9,10] and K = 3 
L = [3,6,9] -> list of indices till which we can identify each group.

Group 1 = [1,2,3] indices 0 to 2
Group 2 = [4,5,6] indices 3 to 5
Group 3 = [7,8,9] indices 6 to 8
the remainig element in the array is [10] whose length is 1 which is less than K. 
This means that we can directly assume it to be a group in itself and we don't need to find the last index of this group as the last index will surpass the length of the array.

Now we reverse the groups in the array by using list slicing.

Point to note : Slicing slices the list from i to j-1 in arr[i:j].
so if we slice the array arr[0:3] we get [1,2,3]. (element at 3rd index is not included)


we'll understand the entire program by taking example arr = [1,2,3,4,5,6,7,8,9,10,11]
'''




#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
	
	# arr = [1,2,3,4,5,6,7,8,9,10,11]
	
	if K >= len(arr):
            arr[:] = arr[:][::-1]
            # if size of group (K) is greater than the size of the array itself, then the entire array will be reversed as a single group
        
        else:
            i = K
            l = []    #list to store the last index of each group from the array
            while i < len(arr):
                l.append(i)
                i += K
            #print(l)
            # l = [3,6,9]
            j = 0
            for i in range(len(l)):
                arr[j:l[i]] = arr[j:l[i]][::-1]  #reversing each group by using the indices stored in the list l
                j = l[i]
            
	    # first iteration -> [3,2,1,4,5,6,7,8,9,10,11]
	    # second iteration -> [3,2,1,6,5,4,7,8,9,10,11]
	    # third iteration -> [3,2,1,6,5,4,9,8,7,10,11]
		
	    #the remaining elements 10 and 11 will form one group.
            
            arr[l[i]:] = arr[l[i]:][::-1]
	    
	    # reverses the last remaining group
	
	    # [3,2,1,6,5,4,9,8,7,11,10]
        
        
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
