public class foobar {


	public static String foobar(int n) {
		if (n % 3 == 0 && n % 5 == 0) {
			return n + "foobar";
		
		} else if (n % 3 == 0) {
			return n + "foo";

		} else if (n % 5 == 0) {
			return n + "bar";
		}
		return Integer.toString(n);
	}


	public static void main(String[] args) {
		System.out.println(foobar(1));
		System.out.println(foobar(9));
		System.out.println(foobar(10));
		System.out.println(foobar(15));
	}
}