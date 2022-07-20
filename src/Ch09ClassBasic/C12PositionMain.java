package Ch09ClassBasic;

class C12Position{
	
	int x,y,z;
	
	C12Position(){
		
	}
	
	C12Position(int x){
		this.x=x;
	}
	
	C12Position(int x, int y){
		this.x =x;
		this.y=y; //asdf
	}
	
	C12Position(int x, int y, int z){
		this.x = x;
		this.y=y;
		this.z=z;
	}

	
	void ShowInfo() {
		System.out.printf("x=%d y=%d z=%d", x,y,z);
	}
}

public class C12PositionMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		C12Position ob1 = new C12Position();
		C12Position ob2 = new C12Position(10);
		C12Position ob3 = new C12Position(10,20);
		C12Position ob4 = new C12Position(10,20,30);
	}

}
