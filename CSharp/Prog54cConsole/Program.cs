/*
 * Created by SharpDevelop.
 * User: guernsey.l
 * Date: 4/10/2024
 * Time: 2:31 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Prog54cConsole
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("Enter radius: ");
			double radius = int.Parse(Console.ReadLine());
			
			double circumfrence = radius * 2;
			double area = radius * radius * 3.14159;
			Console.WriteLine("Circumfrence: " + Math.Round(circumfrence, 2));
			Console.WriteLine("Area: " + Math.Round(area, 2));
			Console.ReadKey();
			
		}
	}
}