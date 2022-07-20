package Ch09ClassBasic;

// 함수 오버로딩
// 함수의 이름을 동일하게 두고 함수의 매개변수를 다양하게 둘 수 있도록 허용한 문법

class Calc
{	
	int sum(int a, int b) {
		System.out.println("SUM(a,b) 호출!");
		return a+b;
	}

	int sum(int a, int b, int c) {
		System.out.println("SUM(a,b,c) 호출!");
		return a+b+c;
	}
	
	int sum(String a, String b) {
		System.out.println(a+b);
		return 1; 
	}

}

public class C10MethodOverloading {
	//overloading 과 overriding의 차이

	public static void main(String[] args) {
		Calc obj = new Calc();
		System.out.println(obj.sum(10, 20));
		System.out.println(obj.sum(10, 20, 30));
		obj.sum("안녕", "하세요");
	}

}
