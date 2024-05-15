namespace Prog366b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("The following numbers generated " + "by the formular x^2 - x + 41 are: ");
            int x = 1;
            while (true)
            {
                int num = f(x);
                if (IsPrime(num, 2))
                    listBox1.Items.Add(num + "\tprime");
                else
                {
                    int factor = FindSmallestFactor(num);
                    listBox1.Items.Add(num + "\ttestfails/factor=" + factor);
                    return;
                }
                x++;
            }
        }

        public int f(int x) { return (int)Math.Pow(x, 2) - x + 41; }

        public bool IsPrime(int n, int f)
        {
            // Trial Division Algorithm
            if (n <= 1) return false;
            if (n == 2 || f * f > n) return true;
            if (n % f == 0) return false;
            return IsPrime(n, f + 1);
        }

        public int FindSmallestFactor(int n)
        {
            for (int lcv = 2; lcv <= Math.Sqrt(n); lcv++)
                if (n % lcv == 0) return lcv;
            return n;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}