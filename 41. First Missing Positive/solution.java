class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int res=1;
        for(int x:nums){
            if (x==res){
                res++;
            }
        }
        return res;
    }
}
