using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PEuler_P6
{
    class Program
    {
        static void Main(string[] args)
        {
            int ans = 0,num,i=2;
            while (ans == 0)
            {
                num=20*i;
                if (num % 19 == 0 && num % 18 == 0 && num % 17 == 0 && num % 16 == 0 && num % 15 == 0 && num % 14 == 0 && num % 13 == 0 && num%12==0 && num%11==0)
                {
                    ans=num;
                }
                i++;
            }
        }
    }
}
