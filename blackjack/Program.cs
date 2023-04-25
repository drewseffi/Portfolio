using System;
using System.Security.Cryptography;

class Program
{
    static void Main(string[] args)
    {
        String line;

        String[] cards = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
        List<String> playerHand = new List<string>();
        List<String> dealerHand = new List<string>();

        Console.WriteLine("Welcome to virtual blackjack. Please type 'draw' to draw another card and type 'stand' to stop drawing cards");
    
        dealerHand.Add(cards[Randomize()]);
        playerHand.Add(cards[Randomize()]);
        Console.WriteLine(playerHand[0]);

        line = Console.ReadLine();
        if (line != null)
        {
            if (line.Equals("draw"))
            {
                
            }
            else if (line.Equals("stand"))
            {
                
            }
        }
        else 
        {
            Console.WriteLine("OK then");
        }

    }

    public static int Randomize()
    {
        Random rand = new Random();
        int randomNumber = rand.Next(0, 13); // generates a random integer between 0 and 12 (inclusive)

        return randomNumber;
    }
}