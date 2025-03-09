package shape;

public class Retangle implements Shape {
  private final double width;
  private final double height;

  public Retangle(double width, double height) {
    this.width = width;
    this.height = height;
  }

  @Override
  public double surfaceArea() {
    return width * height;
  }
}
