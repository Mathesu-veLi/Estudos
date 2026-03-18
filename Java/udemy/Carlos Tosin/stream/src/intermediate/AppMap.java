package intermediate;

import java.time.Year;
import java.util.Arrays;

public class AppMap {
    public static void main(String[] args) {
        var years = Student.list()
            .stream()
            .map(Student::yearOfBirth)
            .mapToInt(Year::getValue)
            .toArray();

        System.out.println(Arrays.toString(years));
    }
}
