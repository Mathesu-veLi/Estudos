package application;

import java.util.Locale;
import java.util.Scanner;

import entities.Triangle;

public class Program1 {
	public static void main(String[] args) {
		Locale.setDefault(Locale.US);
		Scanner sc = new Scanner(System.in);
		
		Triangle x, y;
		x = new Triangle();
		y = new Triangle();
		
		System.out.println("ENter the measures of triangle X: ");
		x.a = sc.nextDouble();
		x.b = sc.nextDouble();
		x.c = sc.nextDouble();
		System.out.println("ENter the measures of triangle Y: ");
		y.a = sc.nextDouble();
		y.b = sc.nextDouble();
		y.c = sc.nextDouble();
		
		
		System.out.printf("Triangle X area: %.4f%n", x.calculateArea());
		System.out.printf("Triangle Y area: %.4f%n", y.calculateArea());
		
		if (x.calculateArea() > y.calculateArea()) {
			System.out.println("Larger area: X");
		} else {
			System.out.println("Larger area: Y");
		}
		
		sc.close();
	}
}
