import java.util.Map;
import java.util.Scanner;
import java.util.HashMap;

public class Question1_1 {
    public static boolean noDataStruct(String s){
        for(int i=0; i<s.length()-1; i++){
            for(int j=i+1; j<s.length(); j++){
                if (s.charAt(i) == s.charAt(j)){
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean isUnique(String s){
        HashMap<Character, Integer> map = new HashMap<>();
        // no foreach on string, cast to character array
        for (char c:s.toCharArray()){
            // if character is already a key in the map
            if(map.get(c) != null){
                // increment value at key
                map.put(c, map.get(c) + 1);
            }
            else{
                map.put(c, 1);
            }
        }

        // iterate over map, if any letter occurs more than once, return false
        for(Map.Entry<Character, Integer> entry: map.entrySet()){
            if(entry.getValue() > 1){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String user;
        while(true) {
            user = input.nextLine();
            if(user.equals("")) break;
            System.out.println(noDataStruct(user));
            System.out.println(isUnique(user));
        }
    }
}
