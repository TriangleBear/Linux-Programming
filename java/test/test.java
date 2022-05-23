import java.util.*;
class test{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a,b;
		System.out.print("Enter first num: ");
		a = sc.nextInt();
		System.out.print("Enter second num: ");
		b = sc.nextInt();
		sc.close();
		System.out.println(ADD(a,b));

	}
	public static int ADD(int a, int b){
		return a+b;
	}
}