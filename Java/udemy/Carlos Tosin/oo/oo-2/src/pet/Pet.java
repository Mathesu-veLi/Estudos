package pet;

public abstract class Pet {
  private String color;
  private int amountEaten;

  public String getColor() {
    return color;
  }

  public void setColor(String color) {
    this.color = color;
  }

  public void feed(int amount) {
    amountEaten += amount;
  }

  public int getAmountEaten() {
    return amountEaten;
  }

  public abstract void sleep(int time);
}
