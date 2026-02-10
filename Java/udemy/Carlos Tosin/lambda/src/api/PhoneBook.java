package api;

import java.util.*;

public class PhoneBook {
    private final Map<String, String> entries = new HashMap<>();

    public PhoneBook() {
        entries.put("pedro", "223-444");
        entries.put("maria", "555-555");
        entries.put("ricardo", "888-942");
    }

    public Optional<String> findByName(String name) {
        return Optional.ofNullable(entries.get(name));
    }
}
