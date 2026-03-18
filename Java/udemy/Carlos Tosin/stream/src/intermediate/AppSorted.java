package intermediate;

import java.util.Comparator;

public class AppSorted {
    public static void main(String[] args) {
        var names = Student.list()
            .stream()
            .map(Student::name)
            .sorted(Comparator.reverseOrder())
            .toList();

        System.out.println(names);
    }
}
