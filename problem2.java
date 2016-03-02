/**
*@Author Daniel Gravel
*Calculates the sum of all even fibinacci numbers up to 4 million
*/
public class problem2{
	public int evenFibonacci(){
		int first = 1;
		int second = 0;
		int sum = 0;

		while(first <= 4000000){
			if(first%2 == 0){
				sum += first;
			}
			int temp = first + second;
			second = first;
			first = temp;
		}
		return sum;
	}

	public static void main(String args[]){
		System.out.println(new problem2().evenFibonacci() + "");
	}
}