package Ch09ClassBasic;

class Position{
	int xpos;
	int ypos;
	
	Position() {
		xpos = 100;
		ypos = 100;
	}
	
	void setposXY(int xpos){
		this.xpos = xpos;
		ypos = 0;
	}
	
	void setposXY(int xpos, int ypos) {
		this.xpos = xpos;
		this.ypos = ypos;
	}
	
	void showInfo() {
		System.out.println("xpos: "+xpos+", ypos: "+ypos);
		
	}
	
}

public class C11PositionMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Position obj = new Position();
		obj.setposXY(10); //멤버 xpos에 값이 저장, ypos는 0 저장
		obj.setposXY(10,20);
		obj.showInfo();
	}
}
