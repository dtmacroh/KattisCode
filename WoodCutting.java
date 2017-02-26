package programming_contest_problems;


import java.util.*;
import java.io.*;
public class WoodCutting{
	
	public static void main(String [] args)
	{
		
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int iter = in.nextInt();
		in.nextLine();
		for (int i= 0; i< iter; i++ )
		{
			int numOfCust = in.nextInt();
			in.nextLine();
			for (int j = 0; j<numOfCust; j++)
			{
				String cust = in.nextLine();
				int numOfItems = Integer.parseInt(cust.split(" ")[0]);
				int total=0;
				
				for (int n=1; n<=numOfItems; n++)
				{
					total = total + Integer.parseInt(cust.split(" ")[n]);
					
				}
				System.out.println(total);
			}
			
		}
		
		
	}
}
	
	
	