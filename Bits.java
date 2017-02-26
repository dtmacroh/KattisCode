package programming_contest_problems;


import java.util.*;
import java.io.*;
public class Bits{
	
	public static void main(String [] args)
	{
		
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int iter = in.nextInt();
		in.nextLine();
		for (int i= 0; i< iter; i++ )
		{
			String bitString = Integer.toString(in.nextInt());
			String [] arr = bitString.split("");
			int longest = 0;
			int longesttemp = 0;
			String bit2;
			String test = "";
			for (int j = 0; j< arr.length; j++)
			{
				test = test + arr[j];
				bit2 = Integer.toBinaryString(Integer.parseInt(test));
				char [] charArray = bit2.toCharArray();
				longesttemp = 0;
				for (int c = 0; c<charArray.length; c++){
					if (Character.compare(charArray[c], '1') ==0)
					{
						longesttemp++;	
					}	
				}
				if (longest <longesttemp)
				{
					longest = longesttemp;
					
				}
				
				
			}
			
			System.out.println(longest);
		}
		
		
	}
}
	