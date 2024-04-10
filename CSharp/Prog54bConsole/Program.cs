/*
 * Created by SharpDevelop.
 * User: guernsey.l
 * Date: 4/10/2024
 * Time: 2:21 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Prog54bConsole
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("Enter num1: ");
			int num1 = int.Parse(Console.ReadLine());
			Console.Write("Enter num2: ");
			int num2 = int.Parse(Console.ReadLine());
			Console.Write("Enter num3: ");
			int num3 = int.Parse(Console.ReadLine());
			Console.Write("Enter num4: ");
			int num4 = int.Parse(Console.ReadLine());
			
			int sum = num1 + num2 + num3 + num4;
			double average = (double)sum / 4.0;
			Console.WriteLine("Sum: " + sum);
			Console.WriteLine("Average: " + Math.Round(average, 2));
			Console.ReadKey();
			
		}
	}
}