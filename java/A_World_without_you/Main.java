import java.util.*;
public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int todo=0;

		System.out.println("What do you want to do in life?");

		System.out.println("1. Walk Outside\n"
						+"2. Sleep\n"
						+"3. Do something productive\n"
						+"4. Wait\n"
						+"5. Help yourself\n");
		todo=sc.nextInt();

		switch(todo){
			case 1:
				Walked();
				break;
			case 2:
				System.out.println();
				break;
		}
	}
	public static void Walked(){
		System.out.println("________________________________________");
		System.out.println("You walked outside..."
			+"");

	}
}