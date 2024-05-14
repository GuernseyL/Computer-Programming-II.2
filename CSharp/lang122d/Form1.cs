namespace lang122d
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("Input (X) \t\t Output (Y)");
            double X = -12;
            while (X < 16) {
                double y = (Math.Pow(X, 6) + -3 * Math.Pow(X, 5) + -93 * Math.Pow(X, 4) + 87 * Math.Pow(X, 3) + 1596 * Math.Pow(X, 2) + -1380 * X - 2800);
                listBox1.Items.Add(X + "\t\t" + y);
                X++;
            }
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}