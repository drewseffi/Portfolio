using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        Dictionary<String, int> myDictionary = new Dictionary<string, int>();
        myDictionary.Add("a", 1);
        myDictionary.Add("b", 2);
        myDictionary.Add("c", 3);
        myDictionary.Add("d", 4);
        myDictionary.Add("e", 5);
        myDictionary.Add("f", 6);
        myDictionary.Add("g", 7);
        myDictionary.Add("h", 8);
        myDictionary.Add("i", 9);
        myDictionary.Add("j", 10);
        myDictionary.Add("k", 11);
        myDictionary.Add("l", 12);
        myDictionary.Add("m", 13);
        myDictionary.Add("n", 14);
        myDictionary.Add("o", 15);
        myDictionary.Add("p", 16);
        myDictionary.Add("q", 17);
        myDictionary.Add("r", 18);
        myDictionary.Add("s", 19);
        myDictionary.Add("t", 20);
        myDictionary.Add("u", 21);
        myDictionary.Add("v", 22);
        myDictionary.Add("w", 23);
        myDictionary.Add("x", 24);
        myDictionary.Add("y", 25);
        myDictionary.Add("z", 26);

        Console.WriteLine("People input a string in lower case");
        string inputString = Console.ReadLine();

        Char[] splitString = inputString.ToCharArray();

        int totalSum = 0;

        foreach (char c in splitString)
        {
            string s = c.ToString();
            if (myDictionary.ContainsKey(s))
            {
                totalSum += myDictionary[s];
            }
        }

        Console.WriteLine(totalSum);
    }
}
