class Solution {
    public int countDigitOne(int n) {
        int ans=0;
        for (int i=0;i<=n;i++){
            int curr=i;
            while(curr!=0){
                int digit=curr/10;
                if((curr%10)==1){
                    ans+=1;
                }
                curr=curr/10;
            }
        }
        return ans;
    }
}
