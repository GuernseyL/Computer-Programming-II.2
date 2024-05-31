// See https://aka.ms/new-console-template for more information
{
    Console.WriteLine("Host or join a server. (Host/Join)");
    string HostClient = Console.ReadLine();
    string HostUser = " ";
    string GuestUser = " ";
    if (HostClient == "Host") { Console.WriteLine("Enter your admin name"); HostUser = Console.ReadLine(); Console.WriteLine(HostUser); }
    else if (HostClient == "Join") { Console.WriteLine("Enter your guest name"); GuestUser = Console.ReadLine(); Console.WriteLine(GuestUser); }
    else { Console.WriteLine("You did not enter Host or Join, shutting down."); System.Environment.Exit(0); }
    Console.WriteLine(HostClient);
    Console.WriteLine("Enter your message (Type 'Room.Exit' to leave:");
    int constant = 0;
    while (constant <= 0)
    {
        string Message = Console.ReadLine(); Console.WriteLine("{" + HostUser + "}  " + "'" + Message + "'"); if (Message == "Room.Exit") { constant++; }
    }
//Create host server
//Allow client server joining
//User message system

}