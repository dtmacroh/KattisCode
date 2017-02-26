package programming_contest_problems;


import java.util.*;
import java.io.*;
public class Soylent{
	
	public static void main(String [] args)
	{
		
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int iter = in.nextInt();
		
		for (int i= 0; i< iter; i++ )
		{
			int cal = in.nextInt();
			double soylent = Math.ceil((float)cal/400);
			System.out.println(Math.round(soylent));
		}
		
		
	}
}
	
	
	