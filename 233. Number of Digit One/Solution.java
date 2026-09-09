class Solution {
    public int countDigitOne(int n) {
        long ans=0;
        for(long i=1;i<=n;i*=10){
            long a=n/(i*10);
            long b=(n/i)%10;
            long c=n%i;
            if(b==0) ans+=a*i;
            else if(b==1) ans+=a*i+c+1;
            else ans+=(a+1)*i;
        }
        return (int)ans;
    }
}
