using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pg266Console
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter 1st number to be compared: ");
            int num1 = int.Parse(Console.ReadLine());
            Console.Write("Enter 2nd number to be compared: ");
            int num2 = int.Parse(Console.ReadLine());
            // && AND, || OR, ! NOT
            if (num1 > num2) Console.WriteLine(num1 + " is greater than " + num2);
            else if (num1 < num2) Console.WriteLine(num1 + " is less than " + num2);
            else if (num1 == num2) Console.WriteLine(num1 + " is equal to " + num2);
            Console.ReadLine();
        }
    }
}
