package record;

import java.util.Objects;

public class Person {
  private final String firstName;
  private final String lastName;
  private final int age;

  public Person(String firstName, String lastName, int age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  public String getFirstName() {
    return firstName;
  }

  public String getLastName() {
    return lastName;
  }

  public int getAge() {
    return age;
  }

  @Override
  public String toString() {
    return "Person{" + "firstName='" + firstName + '\'' + ", lastName='" +
        lastName + '\'' + ", age=" + age + '}';
  }

  @Override
  public boolean equals(Object o) {
    if(o == null || getClass() != o.getClass()) return false;

    Person person = (Person) o;
    return getAge() == person.getAge() && Objects.equals(getFirstName(),
                                                         person.getFirstName()) &&
        Objects.equals(getLastName(), person.getLastName());
  }

  @Override
  public int hashCode() {
    int result = Objects.hashCode(getFirstName());
    result = 31 * result + Objects.hashCode(getLastName());
    result = 31 * result + getAge();
    return result;
  }
}

