class Solution {
    public boolean checkDivisibility(int n) {
        int nc=n;
        int digitsum=0;
        int digitprod=1;
        while(nc>0){
            int digit=nc%10;
            digitsum+=digit;
            digitprod*=digit;
            nc=nc/10;
        }
        if ((n%(digitprod+digitsum))==0){
            return true;
        }else{
            return false;
        }
    }
}