using System;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        int counter = 0;
        int width = 1920;
        int height = 1080;
        int matrix_w = 16;
        int matrix_h = 9;

        while(width != 1280 && height != 720)
        {
            width = (width - matrix_w) + 1;
            height = (height - matrix_h) + 1;

            counter++;

            Console.WriteLine(width + "x" + height);
        }

        Console.WriteLine("It would take " + counter + " layers");
    }
}
