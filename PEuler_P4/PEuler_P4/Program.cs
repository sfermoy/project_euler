using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace PEuler_P4
{
    class Program
    {
        static void Main(string[] args)
        {
            int i;
            int ans=0,test=0,tempans=0;
            int x=999, y=999;
            bool cycle = true;
            while (ans == 0)
            {
                cycle = true;
                for (i = 0; i < x; i++)
                {
                    test = x * y;
                    if (isPalendrome6(test))
                    {
                        if (test > tempans)
                        {
                            tempans = test;
                            cycle = false;
                            x = x - 1;
                            y = x;
                         
                        }
                    }
                    if(tempans>=((x-1)*(x-1)))
                            ans = tempans;
                    if (cycle == false)
                        break;
                    y = x - i;
                }
                if (cycle == true)
                {
                    x = x - 1;
                }
            }
            Console.WriteLine(ans.ToString());

        }

        public static bool isPalendrome6(int n)
        {
            
            string pal = n.ToString();
            if (pal.Length == 6)
            {
                if(pal[0]==pal[5]&& pal[1]==pal[4] &&pal[2]==pal[3])
                {
                    return true;
                //Console.WriteLine(pal[1]);
                }
            }
                return false;
        }
    }
}
