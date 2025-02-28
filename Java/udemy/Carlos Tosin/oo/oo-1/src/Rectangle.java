public class Rectangle {
  private final int width;
  private final int height;

  public Rectangle (int width, int height) {
    this.width = width;
    this.height = height;
  }

  public Rectangle (int size) {
    this(size, size);
  }

  public int square() {
    return width * height;
  }
}
