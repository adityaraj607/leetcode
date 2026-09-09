class Solution {
    public int maxArea(int[] height) {
        int l=0;
        int r=height.length-1;
        int maxw=0;
        while(l<r){
            int area=Math.min(height[l],height[r])*(r-l);
            maxw=Math.max(maxw,area);
            if(height[l]<height[r]){
                l+=1;
            }else{
                r-=1;
            }
        }
        return maxw;
    }
}
