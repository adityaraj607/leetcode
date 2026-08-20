class Solution {
    public int[] resultArray(int[] nums) {
        List<Integer> arr1=new ArrayList<>();
        List<Integer> arr2=new ArrayList<>();
        arr1.add(nums[0]);
        arr2.add(nums[1]);
        int n=nums.length;
        for (int i=2;i<n;i++){
            if(arr1.get(arr1.size()-1)>arr2.get(arr2.size()-1)){
                arr1.add(nums[i]);
            }else{
                arr2.add(nums[i]);
            }
        }
        int in=0;
        int[] r=new int[n];
        for (int i:arr1){
            r[in++]=i;
        }
        for (int i:arr2){
            r[in++]=i;
        }
        return r;
    }
}
