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
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string EmployeeName = textBox1.Text;
            double EmployeeWage = double.Parse(textBox2.Text);
            comboBox1.Items.Add(EmployeeName);
            comboBox2.Items.Add(EmployeeWage);
        }

        private void Form3_Load(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Form1 MainMenu = new Form1();
            MainMenu.Show();
            this.Hide();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            double TotalEmployeePay = 0
            double Wage = double.Parse(comboBox2.Text);
            double Hours = double.Parse(textBox3.Text);
            double Pay = Wage * Hours;
            double PayRounded = Math.Round(Pay, 2);
            label1.Text = ("$" + PayRounded);
            TotalEmployeePay = TotalEmployeePay + PayRounded;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            double TotalMoney = double.Parse(textBox4.Text);
            double TotalMoneyRounded = Math.Round(TotalMoney, 2);
           

        }
    }
}
