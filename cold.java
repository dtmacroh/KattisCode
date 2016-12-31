
import java.util.*;
import java.io.*;
import java.lang.Math;

public class cold{

	public static void main (String [] args)
	{
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int iter = in.nextInt(); in.nextLine();
		int counter = 0;
		String [] tempsS = in.nextLine().split(" ");	
		int [] temps = new int [iter];
		for (int i=0; i<iter; i++)
		{
			temps[i] = Integer.parseInt(tempsS[i]);
		}
		for (int i=0; i<iter;i++){
			if (temps[i] <0 )
				counter++;
		}
		
		System.out.println(counter);
	
	}




}