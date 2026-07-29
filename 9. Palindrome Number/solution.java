class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false;
        }
        int rev=0;
        int original=x;
        while (x!=0){
            int last=x%10;
            x=x/10;
            rev=(rev*10)+last;
        }
        if (original==rev){
            return true;
        }else{
            return false;
        }
    }
}
