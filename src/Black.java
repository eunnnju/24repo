import java.util.ArrayList;
import java.util.Scanner;


public class Black {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N, M;
		ArrayList cards = new ArrayList();
		
		N = sc.nextInt();
		M = sc.nextInt();
		sc.nextLine();
		
		for(int i=0; i<N; i++) {
			cards.add(sc.nextInt());
		}
		
		
	}

}
