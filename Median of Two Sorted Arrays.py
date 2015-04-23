class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length = len(A) + len(B)
        if length%2:
            return self.kth(A, B, length/2+1)
        else:
            return (self.kth(A, B, length/2) + self.kth(A, B, length/2+1)) / 2.0

    def kth(self, A, B, k):
        if not (A and B):
            return A[k-1] if A else B[k-1]

        if k == 1:
            return A[0] if A[0] <= B[0] else B[0]

        step = k/2
        index_A = min(step, len(A));
        index_B = min(step, len(B));
        if(A[index_A-1] <= B[index_B-1]):
            return self.kth(A[index_A:], B, k-index_A)
        else:
            return self.kth(A, B[index_B:], k-index_B)