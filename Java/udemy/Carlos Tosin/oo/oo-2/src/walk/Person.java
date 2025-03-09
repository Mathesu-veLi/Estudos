package walk;

public class Person implements Walkable, Jumpable {
  private int steps;
  private int distancePerSteep;

  @Override
  public void walk() {
    steps++;
    distancePerSteep += 10;
  }

  @Override
  public void stop() {
    steps = 0;
  }

  @Override
  public void jump() {
    walk();
    walk();
  }
}
