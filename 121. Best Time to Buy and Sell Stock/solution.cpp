class Solution {
    public int maxProfit(int[] prices) {
        int lowest=prices[0];
        int max=0;
        for (int i:prices){
            if (i<lowest){
                lowest=i;
            }
            if (i-lowest>max) {
                max=i-lowest;
            }
        }
        return max;
    }
}
