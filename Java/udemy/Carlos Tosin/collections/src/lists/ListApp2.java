package lists;

import java.util.List;

public class ListApp2 {
    public static void main(String[] args) {
        var list = List.of("A", "B", "C", "D");

        //list.add("J") ERROR

        for (String s : list) {
            System.out.println(s);
        }
    }
}
