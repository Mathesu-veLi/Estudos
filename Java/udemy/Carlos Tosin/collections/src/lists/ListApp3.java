package lists;

import java.util.Iterator;
import java.util.List;

public class ListApp3 {
    public static void main(String[] args) {
        var list = List.of("A", "B", "C", "D");

        for (int i = 0; i < list.size(); i++) {
            String s = list.get(i);
            System.out.println(s);
        }

        Iterator<String> iter = list.iterator();
        while (iter.hasNext()) {
            String s = iter.next();
            if (s.equals("C")) {
                iter.remove();
            }
        }
    }
}
