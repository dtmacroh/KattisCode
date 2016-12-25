


import java.io.*;
import java.util.*;

public class conundrum
{


	public static void main (String [] args)
	{
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		String word = in.nextLine();
		
		int counter = 0;
		for (int i=0; i< word.length(); i++)
		{
			int mod = i%3;
			if (mod== 0 && word.charAt(i)!= 'P')
			{
				counter++;
			}
			else if (mod== 1 && word.charAt(i)!= 'E')
			{
				counter++;
			}
			else if (mod== 2 && word.charAt(i)!= 'R')
			{
				counter++;
			}
		}
		
		System.out.println(counter);
	
	}




}