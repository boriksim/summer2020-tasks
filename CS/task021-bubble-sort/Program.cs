using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Runtime.CompilerServices;

namespace task021_bubble_sort
{
    class BubbleSort
    {
        static void Main()
        {
            int length = 100;
            List<int> nums = new List<int>();
            Random rnd = new Random();

            for (int n = 0; n < length; n++)
            {
                nums.Add(rnd.Next(100));
            }

            for (int i = 0; i < nums.Count - 1; i++)
            {
                for (int j = 0; j < nums.Count - i - 1; j++)
                {
                    if (nums[j] > nums[j + 1])
                    {
                        var tmp = nums[j + 1];
                        nums[j + 1] = nums[j];
                        nums[j] = tmp;
                    }
                }
            }

            foreach (int item in nums)
            {
                Console.WriteLine(item);
            }
        }
    }
}
