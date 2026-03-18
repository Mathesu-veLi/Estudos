package intermediate;

import java.util.Collection;

public class AppFlatMap {
    public static void main(String[] args) {
        var grades = Student.list()
            .stream()
            .map(Student::grades)
            .flatMap(Collection::stream)
            .toList();

        System.out.println(grades);
    }
}
