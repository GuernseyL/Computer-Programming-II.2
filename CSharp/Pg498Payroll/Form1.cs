using Microsoft.VisualBasic;

namespace Pg498Payroll
{
    public partial class Form1 : Form
    {
        const decimal decHOURLY_PAY_RATE = 6.0m;
        const int intMAX_EMPLOYEES = 5;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Calculate and display the gross pay earned by employees
            int[] intHours = new int[intMAX_EMPLOYEES];
            //Make a new int array of capacity intMAX_EMPLOYEES
            //Capacity can never change, unlike lists in Python
            //Explicity define an array with int[] thing = {0, 1, 2, 3, 4}; (len 5)
            int intCount = 0;         // Loop Counter
            int intEmpHours = 0;      // Hours
            decimal decEmpPay = 0.0m; // Gross Pay

            // Get the hours worked by employees
            for (intCount = 0; intCount < intMAX_EMPLOYEES; intCount++)
            {
                while (int.TryParse(
                    Interaction.InputBox("Enter the number of hours worked by employee #" + 
                    (intCount + 1).ToString(), "Need Hours Worked"), out intEmpHours) == false)
                {
                    MessageBox.Show("Please enter an integer for hours worked");
                }
                    intHours[intCount] = intEmpHours;
            }
            // Calculate and display each employee's gross pay
            listBox1.Items.Clear();
            for (intCount = 0; intCount < intMAX_EMPLOYEES; intCount++)
            {
                decEmpPay = intHours[intCount] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Emplyee " + (intCount + 1).ToString() + " earned " + decEmpPay.ToString("$.00"));
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}