class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] a=IntStream.concat(Arrays.stream(nums1),Arrays.stream(nums2)).toArray();
        Arrays.sort(a);
        int n=a.length;
        if(n%2==1) return a[n/2];
        return (a[n/2-1]+a[n/2])/2.0;
    }
}
