package programming_contest_problems;


import java.util.*;
import java.io.*;
public class CodeAnalysis {
	
	public static String [] arr;
	public static void main(String [] args)
	{
		
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int iter = in.nextInt();
		int numOfInst = 0;
		for (int i= 0; i< iter; i++ )
		{
			numOfInst = in.nextInt();
			in.nextLine();
			arr = new String [numOfInst];
			for (int j = 0; j < numOfInst; j++)
			{
				arr[j] = in.nextLine();	
			}
			recurse(arr, 1);
			
			for (int h = 0; h < arr.length; h++)
			{
				String bool;
				if (arr[h].compareTo("x") ==0){bool= "yes";}else{bool = "no";}
				System.out.println("step " + h + " "+ bool);
				
			}
		}
		
		
	}
	
	
	
	public static void recurse(String [] arr, int instNumber)
	{
		int instToGo; 
		
		if (arr[instNumber-1].compareTo("x")!=0)
		{
			
			char test = Character.toUpperCase(arr[instNumber-1].charAt(0));
			
			if (Character.compare('G', test) ==0)
			{
				instToGo = Integer.parseInt(arr[instNumber-1].split(" ")[1]);
				arr[instNumber-1] = "x";
				recurse(arr, instToGo);
				
}
			if (Character.compare('C', test) ==0)
			{
				instToGo = Integer.parseInt(arr[instNumber-1].split(" ")[1]);
				System.out.println("step no " + instToGo);
				arr[instNumber-1] = "x";
				recurse(arr, instNumber+1);
				recurse(arr, instToGo);
				
			}
			if (Character.compare('N', test) ==0)
			{
				arr[instNumber-1] = "x";
				recurse(arr, instNumber+1);
				
			}
			
		}
			
	}

}
