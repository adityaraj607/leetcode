class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nlist=nums1+nums2
        nlist.sort()
        if (len(nlist)%2) == 0:
            mindex=(len(nlist)-1)//2
            mindex2=mindex+1
            self=(nlist[mindex]+nlist[mindex2])/2.0
        else:
            medianindex=(len(nlist)//2)
            self=nlist[medianindex]
        return self