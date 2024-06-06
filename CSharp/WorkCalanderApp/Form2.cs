using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WorkCalanderApp
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form1 MainMenu = new Form1();
            MainMenu.Show();
            this.Hide();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string Note = textBox1.Text;
            if (comboBox1.Text == "Day 1") { label8.Text = (Note); }
            else if (comboBox1.Text == "Day 2") { label9.Text = (Note); }
            else if (comboBox1.Text == "Day 3") { label10.Text = (Note); }
            else if (comboBox1.Text == "Day 4") { label11.Text = (Note); }
            else if (comboBox1.Text == "Day 5") { label12.Text = (Note); }
            else if (comboBox1.Text == "Day 6") { label13.Text = (Note); }
            else if (comboBox1.Text == "Day 7") { label14.Text = (Note); }
            else if (comboBox1.Text == "Day 8") { label15.Text = (Note); }
            else if (comboBox1.Text == "Day 9") { label16.Text = (Note); }
            else if (comboBox1.Text == "Day 10") { label17.Text = (Note); }
            else if (comboBox1.Text == "Day 11") { label18.Text = (Note); }
            else if (comboBox1.Text == "Day 12") { label19.Text = (Note); }
            else if (comboBox1.Text == "Day 13") { label20.Text = (Note); }
            else if (comboBox1.Text == "Day 14") { label21.Text = (Note); }
            else if (comboBox1.Text == "Day 15") { label22.Text = (Note); }
            else if (comboBox1.Text == "Day 16") { label23.Text = (Note); }
            else if (comboBox1.Text == "Day 17") { label24.Text = (Note); }
            else if (comboBox1.Text == "Day 18") { label25.Text = (Note); }
            else if (comboBox1.Text == "Day 19") { label26.Text = (Note); }
            else if (comboBox1.Text == "Day 20") { label27.Text = (Note); }
            else if (comboBox1.Text == "Day 21") { label28.Text = (Note); }
            else if (comboBox1.Text == "Day 22") { label29.Text = (Note); }
            else if (comboBox1.Text == "Day 23") { label30.Text = (Note); }
            else if (comboBox1.Text == "Day 24") { label31.Text = (Note); }
            else if (comboBox1.Text == "Day 25") { label32.Text = (Note); }
            else if (comboBox1.Text == "Day 26") { label33.Text = (Note); }
            else if (comboBox1.Text == "Day 27") { label34.Text = (Note); }
            else if (comboBox1.Text == "Day 28") { label35.Text = (Note); }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
