﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg266CSharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);

            if (num1 > num2)
                label1.Text = (num1 + " is greater than " + num2);
            else if (num1 < num2)
                label1.Text = (num1 + " is less than " + num2);
            else if (num1 == num2)
                label1.Text = (num1 + " is equal to " + num2);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            
        }
    }
}
