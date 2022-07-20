package Ch09ClassBasic;


//생성자
//객체생성에 필요한 초기값을 저장하는데 사용되는 메소드
//객체생성시 한번만 호출되며 객체 생성이후에는 사용이 불가능하다
//클래스내에서 생성자메서드를 명시하지 않았을 때 기본적으로 주입되는
//생성자 존재. 이를 디폴트 생성자라고 함.
//디폴트 생성자는 클래스명과 동일하며, 매개변수를 가지지 않는다.

class C09Car{
	String owner;
	int speed;
	int fuel;
	
	C09Car(){
		owner = "소유자없음";
		speed = 10;
		fuel = 10;
	}
}

public class C09CarMain {

	public static void main(String[] args) {
		C09Car mycar = new C09Car();
		System.out.println(mycar.owner+" "+mycar.speed+ " "+mycar.fuel);
		
	}

}
