package entities;

public class Triangle {
	public double a;
	public double b;
	public double c;
	
	public double calculateArea() {
		double p = (this.a + this.b + this.b) / 2.0;
		double area = Math.sqrt(p * (p - this.a) * (p - this.b) * (p - this.c));
		return area;
	}
}
