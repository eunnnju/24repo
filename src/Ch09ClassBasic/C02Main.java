package Ch09ClassBasic;

public class C02Main {

	public static void main(String[] args) {
		C02Car mycar = new C02Car();
		mycar.owner="홍길동";
		mycar.speed=0;
		mycar.fuel=100;
		//System.out.printf("%s %d %d\n",mycar.owner,mycar.speed,mycar.fuel);
		mycar.Accel();
		mycar.Break();
		mycar.ShowInfo();
	}

}
//------------------------------- 1문제-------------------------------
//-----------------------
//C02Car
//-----------------------
////속성
//+owner : String 
//+speed : int
//+fuel : int
//
//-----------------------
//C02Main
//-----------------------
//C02Car mycar = new C02Car();
//mycar.owner="홍길동";
//mycar.speed=0;
//mycar.fuel=100;
//System.out.printf("%s %d %d\n",mycar.owner,mycar.speed,mycar.fuel)


//------------------------------- 2 문제(기능 추가)-------------------------------
//-----------------------
//C02Car
//-----------------------
//속성
//+owner : String 
//+speed : int
//+fuel : int
//기능
//+Accel() : void ->owner+ " 님의 차의 속도를 증가합니다" 가 출력
//+Break() : void ->owner+ " 님의 차의 속도가 감소합니다" 가 출력
//+ShowInfo():void ->멤버변수의 값을 모두 화면에 출력
//-----------------------
//C02Main
//-----------------------
//C02Car mycar = new C02Car();
//mycar.owner="홍길동";
//mycar.speed=0;
//mycar.fuel=100;
//mycar.Accel();
//mycar.Break();
//mycar.ShowInfo();


