class Solution {
    public boolean hasDuplicate(int[] nums) {
 for(int i = 0; i < nums.length - 1; i++)
 {
    for(int j = i; j < nums.length - 1; j++){

    
    if( nums[i] == nums[j+1]) {
        return true;
    } else {}
    }
 }
 return false;
    }

}
