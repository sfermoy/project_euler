using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PEuler_P2
{
    class Program
    {
        static void Main(string[] args)
        {
            int prev = 0;
            int curr = 1;
            int next = 0;
            int res = 0;
            while(next <=4000000)
            {
                next = prev + curr;
                if (next % 2 == 0)
                {
                    res += next;
                }
                prev = curr;
                curr = next;
            }
            Console.WriteLine(res.ToString());
        }
    }
}
