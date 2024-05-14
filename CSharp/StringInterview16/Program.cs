// See https://aka.ms/new-console-template for more information
{
    Console.WriteLine("Enter a string: ");
    string text = Console.ReadLine();
    Console.Write("Enter a substring to search for: ");
    string word = Console.ReadLine();
    static bool searchText(string text, string search)
    {
        int tLen = text.Length;
        int sLen = search.Length;

        if (sLen > tLen) return false;

        for (int lcv = 0; lcv <= tLen - sLen; lcv++)
            if (text.Substring(lcv, sLen) == search)
                return true;

        return false;
    }

    bool result = searchText(text, word);
    Console.WriteLine($"Does \"{text}\" contain \"{word}\"?: {result}");
    Console.ReadLine();
}
{
}