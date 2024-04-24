using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pg273Bookpoints
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter number of books bought this month: ");
            int Books = int.Parse(Console.ReadLine());
            if (Books == 0) Console.WriteLine("You earn 0 BookPoints");
            else if (Books == 1) Console.WriteLine("You earn 5 BookPoints");
            else if (Books == 2) Console.WriteLine("You earn 15 BookPoints");
            else if (Books == 3) Console.WriteLine("You earn 30 BookPoints");
            else if (Books >= 4) Console.WriteLine("You earn 60 BookPoints");
            else Console.WriteLine("You haven't bought any books");
            Console.ReadLine();
        }
    }
}
