// See https://aka.ms/new-console-template for more information
{
    Console.WriteLine("Host or join a server. (Host/Join)");
    string HostClient = Console.ReadLine();
    if (HostClient == "Host") { Console.WriteLine("Enter your admin name"); string HostUser = Console.ReadLine(); Console.WriteLine(HostUser); }
    else if (HostClient == "Join") { Console.WriteLine("Enter your guest name"); string GuestUser = Console.ReadLine(); Console.WriteLine(GuestUser); }
    else { Console.WriteLine("You did not enter Host or Join, shutting down."); System.Environment.Exit(0); }
    Console.WriteLine(HostClient);
    Console.ReadLine();
}