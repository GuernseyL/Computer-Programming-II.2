﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg273BookPointsForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int Books = int.Parse(textBox1.Text);
            if (Books < 0) lblbook.Text = "0";
            else if (Books == 1) lblbook.Text = "5";
            else if (Books == 2) lblbook.Text = "15";
            else if (Books == 3) lblbook.Text = "30";
            else if (Books >= 4) lblbook.Text = "60";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
