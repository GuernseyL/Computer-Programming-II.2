using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace LiveChatRoom
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form2 ChatRoom = new Form2();
            string ServerName = Interaction.InputBox("Server name here:", "Enter server name");
            string HostName = Interaction.InputBox("Enter your admin name here:", "Enter host name");
            this.Hide();
            ChatRoom.Show();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form3 GuestRoom = new Form3();
            GuestRoom.Show();
            this.Hide();
        }
    }
}
