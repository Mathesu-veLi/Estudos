package curso_nelio;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter three numbers: ");
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		
		int higher = max(a, b, c);
		
		showResult(higher);
		
		sc.close();
	}
	
	public static int max(int number1, int number2, int number3) {
		if (number1 > number2 && number1 > number3) return number1;
		else if (number2 > number3) return number2;
		else return number3;
	}
	
	public static void showResult(int value) {
		System.out.println("Higher = " + value);
	}

}