﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg347Sum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int lcv = 0;
            int Num = 0;
            string variable = Interaction.InputBox("Enter a positive Integer", "Sum of numbers");
            lcv = variable;
            while (lcv != 0)
                
            MessageBox.Show(variable);
        }
    }
}
