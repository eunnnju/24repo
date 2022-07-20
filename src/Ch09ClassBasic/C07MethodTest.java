package Ch09ClassBasic;

//class Calculator{
//	int sum(int a, int b) {
//		return a+b;
//	}
//	
//	int sub(int a, int b) {
//		return a-b;
//	}
//	
//	void mul(int a, int b) {
//		System.out.println("r3: " +(a*b));
//	}
//	
//	void div(int a, int b) {
//		System.out.println();
//	}
//	
//	
//}
//
public class C07MethodTest {

	public static void main(String[] args) {
//		Calculator cal = new Calculator();
//		
//		int r1=cal.sum(10,20);
//		System.out.println("r1 : " + r1);
//		int r2=cal.sub(50,30);	//뺄셈 x-y
//		System.out.println("r2 : " + r2);
//		cal.mul(5,6); //곱셈->곱셈결과가 함수내의 print호출로 출력
//		cal.div(10,2); //나눈셈 -> 나눈셈결과가 함수내의 print호출로 출력
		
//		LocalTest obj = new LocalTest();
//		obj.Func1();
//		System.out.println();
//		obj.Func2();
//		System.out.println();
//		obj.Func3();
		
		C09Car mycar = new C09Car();
		
	}

}
//생성자
// 객체생성에 필요한 초기값을 저장하는데 사용되는 메소드
// 객체생성시 한번만 호출되며 객체 생성이후에는 사용이 불가능하다
// 클래스내에서 생성자메서드를 명시하지 않았을 때 기본적으로 주입되는
// 생성자 존재. 이를 디폴트 생성자라고 함.
// 디폴트 생성자는 클래스명과 동일하며, 매개변수를 가지지 않는다.


class C09Car{
	String owner;
	int speed;
	int fuel;
	
//	C09Car(String owner, int speed, int fuel){
//		this.owner = owner;
//		this.speed = speed;
//		this.fuel = fuel;
//	}
}


class LocalTest{
	int num=10;
	
	void Func1() {
		System.out.println("num : "+num);
		int num = 100;
		num++;
		System.out.println("num : "+num);
	}
	
	void Func2() {
		System.out.println("num : "+num);
		if(true) {
			int num = 55;
			num++;
			System.out.println("num : "+num);
		}
	}
	
	void Func3() {
		System.out.println("멤버변수 num : "+num);
		for(int num=1; num<10; num++) {
			System.out.println("지역변수 num : "+num);
		}
		System.out.println("전역변수 num : "+num);
	}
}
