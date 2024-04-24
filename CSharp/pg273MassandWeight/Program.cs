using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pg273MassandWeight
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the mass in kilograms: ");
            double Mass = double.Parse(Console.ReadLine());
            double Newtons = Mass * 9.8;
            Console.WriteLine("The weight of the item is " + Math.Round(Newtons, 2) + " newtons");
            Console.ReadLine();
        }
    }
}
