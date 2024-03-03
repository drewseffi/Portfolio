using System;
using System.IO;

class Program
{
	static void Main(string[] args)
	{
		int[] INCREMENTS = { 500, 100, 25, 10, 5, 2, 1 };
		int[] change = { 0, 0, 0, 0, 0, 0, 0 };
		int inputAmount = 0;

		Console.WriteLine("What amount would you like exchanged?");

		string currentLine = Console.ReadLine();

		while (currentLine == null || currentLine == "" || int.TryParse(currentLine, out inputAmount) == false)
		{
			Console.WriteLine("Please input an amount");

			currentLine = Console.ReadLine();
		}

		inputAmount = int.Parse(currentLine);

		Console.WriteLine(inputAmount.ToString() + " accepted");

		int index = 0;
		bool canUse = true;

		while (inputAmount > 0) 
		{
			canUse = true;
			
			while (canUse)
			{
				if (inputAmount - INCREMENTS[index] < 0) 
				{ 
					canUse = false;
				}
				else
				{
					change[index]++;
					inputAmount -= INCREMENTS[index];
				} 
			}

			index++;
		}

		int i = 0;
		foreach (int c in change)
		{
			Console.WriteLine(INCREMENTS[i] + ": " + c);
			i++;
		}
	}

}