using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PEuler_P5
{
    class Program
    {
        static void Main(string[] args)
        {
            int i,x=0,y=0,ans;
            for (i = 0; i <= 100; i++)
            {
                x = x + i;
                y = y + (i * i);
            }
            ans = y - (x * x);
            Console.WriteLine(ans.ToString());
        }
    }
}
