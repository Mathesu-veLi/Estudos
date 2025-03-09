package record;

import java.util.Objects;

public record PersonRecord(String firstName, String lastName, int age) {
  private static final int DEFAULT_AGE = 0;


  public PersonRecord {
    Objects.requireNonNull(firstName);
    Objects.requireNonNull(lastName);
  }

  public PersonRecord(String firstName, String lastName) {
    this(firstName, lastName, DEFAULT_AGE);
  }

  public String fullName() {
    return firstName + " " + lastName;
  }

  public static PersonRecord create(String name) {
    return new PersonRecord(name, "");
  }
}
