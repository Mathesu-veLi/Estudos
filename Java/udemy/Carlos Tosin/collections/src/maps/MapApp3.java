package maps;

import java.util.Map;
import java.util.TreeMap;

public class MapApp3 {
    public static void main(String[] args) {
        Map<Name, Integer> map = new TreeMap<>();
        map.put(new Name("João", "Oliveira"), 35);
        map.put(new Name("Marina", "Silva"), 20);
        map.put(new Name("Celso", "Fernandes"), 49);
        map.put(new Name("Celso", "Fernandes"), 49);

        System.out.println(map);
    }
}
