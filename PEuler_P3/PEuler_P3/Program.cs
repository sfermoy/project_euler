using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace PEuler_P3
{
    class Program
    {
        static void Main(string[] args)
        {
            Stopwatch timer = new Stopwatch();

            timer.Start();
            int i=0;
            long num = 600851475143;
            long sqrt = (long)Math.Sqrt(num) ;
            long ans=0;
            long test = 2;
            while(ans==0 && test>1)
            {
                test = sqrt - i;
                if (num % test == 0)
                {
                    if(isPrime(test))
                    {
                        ans = test;
                    }
                }
                i++;
            }
            timer.Stop();
            Console.WriteLine(timer.Elapsed.Milliseconds);
            Console.WriteLine(ans.ToString());
            
        }
        public static bool isPrime(long n)
        {
            int primetest=2;
            while (primetest > 1 && primetest <(int)Math.Sqrt(n))
            {
                if (n % primetest == 0)
                {
                    return false;
                }
                primetest++;
            }

            return true;
        }
    }
}
