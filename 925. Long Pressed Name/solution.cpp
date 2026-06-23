class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int i=0, j=0;
        while (j<typed.length()){
            if (i<name.length() && name[i]==typed[j]){
                i+=1;
                j+=1;
            }else if(j>0 && typed[j]==typed[j-1]){
                j+=1;
            }else{
                return false;
            }
        }
        return i==name.length();
    }
};
