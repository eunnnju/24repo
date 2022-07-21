package Ch09ClassBasic;

import java.util.*;

class Solution{
	public ArrayList<Integer> solution(int n, int m) {
		ArrayList<Integer> answer = new ArrayList<>();
		
		for(int i=0; i<(n>m?n:m); i++) {
			
		}
		
		return answer;
	}
} 

public class Study {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt();
		
		Solution s = new Solution();
		
		System.out.println(s.solution(3,12));
	}
}
