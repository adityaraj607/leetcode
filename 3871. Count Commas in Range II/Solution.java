class Solution {
    public long countCommas(long n) {
        if (n<1000) return 0;
        long a=0;
        long x=1000;
        while(x<=n){
            a+=n-(x-1);
            if(x>(n/1000)){
                break;
            }
            x*=1000;
        }
        return a;
    }
}
