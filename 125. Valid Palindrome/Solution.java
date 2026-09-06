class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder ns = new StringBuilder();
        for (int i=0;i<s.length();i++) {
            if (Character.isLetterOrDigit(s.charAt(i))) {
                ns.append(Character.toLowerCase(s.charAt(i)));
            }
        }
        String original=ns.toString();
        ns.reverse();
        String reverse=ns.toString();
        return original.equals(reverse);
    }
}