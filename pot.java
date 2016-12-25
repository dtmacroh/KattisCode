
import java.util.*;
import java.io.*;
import java.lang.Math;

public class pot{

	public static void main (String [] args)
	{
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int iter = in.nextInt(); in.nextLine();
		double result = 0;
		for (int i=0; i< iter; i++)
		{
			
			int numberString1 = in.nextInt();
			String numberString = String.valueOf(numberString1);
			if (numberString.length() > 1)
			{
			int exp = Integer.parseInt(Character.toString(numberString.charAt(numberString.length()-1)));
			int number = Integer.parseInt(numberString.substring(0,numberString.length()-1));
			result = result + Math.pow(number, exp);
			
			}
			
			
		}
		System.out.println((int)result);
	
	}




}