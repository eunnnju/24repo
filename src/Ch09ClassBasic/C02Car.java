package Ch09ClassBasic;

public class C02Car {
	public String owner;  
	public int speed;
	public int fuel;
	
	//	기능
	void Accel(){
		System.out.println(owner + " 님의 차가 가속합니다");
	}
	void Break() {
		System.out.println(owner + " 님의 차가 감속합니다");
	}
	void ShowInfo() {
		System.out.printf("%s %d %d\n", owner,speed,fuel);
	}
	
}
