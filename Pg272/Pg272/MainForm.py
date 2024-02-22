import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.ControlDark
		self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(23, 23)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(334, 35)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Daytime (6:00 A.M. - 5:59 P.M.)"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.ControlDark
		self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(23, 64)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(345, 29)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening (6:00 P.M. - 11:59 P.M)"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.ControlDark
		self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(23, 99)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(345, 29)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Offpeak (12:00 A.M. - 5:59 A.M.)"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkGray
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(402, 79)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(164, 29)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGray
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(402, 40)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(164, 36)
		self._label1.TabIndex = 4
		self._label1.Text = "Minutes on call:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DimGray
		self._label2.Location = System.Drawing.Point(12, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(373, 136)
		self._label2.TabIndex = 5
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DimGray
		self._label3.Location = System.Drawing.Point(391, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(187, 136)
		self._label3.TabIndex = 6
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DimGray
		self._label4.Location = System.Drawing.Point(12, 157)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(566, 98)
		self._label4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightGray
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(23, 170)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(171, 28)
		self._label5.TabIndex = 8
		self._label5.Text = "Rate per Minute:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightGray
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(23, 208)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(120, 28)
		self._label6.TabIndex = 9
		self._label6.Text = "Total Cost:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Gray
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(12, 267)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(554, 98)
		self._label7.TabIndex = 12
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gainsboro
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(23, 278)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(171, 75)
		self._button1.TabIndex = 13
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gainsboro
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(200, 278)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(171, 75)
		self._button2.TabIndex = 14
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gainsboro
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(377, 278)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(171, 75)
		self._button3.TabIndex = 15
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightGray
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(200, 170)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(366, 28)
		self._label8.TabIndex = 16
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.LightGray
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(149, 208)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(417, 28)
		self._label9.TabIndex = 17
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(585, 374)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label3)
		self.Name = "MainForm"
		self.Text = "Pg272"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def RadioButton1CheckedChanged(self, sender, e):
		self._label8.Text = "$0.07"

	def RadioButton2CheckedChanged(self, sender, e):
		self._label8.Text = "$0.12"

	def RadioButton3CheckedChanged(self, sender, e):
		self._label8.Text = "$0.05"

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		if self._radioButton1.Checked:
			Rate = 0.07
		elif self._radioButton3.Checked:
			Rate = 0.05
		elif self._radioButton2.Checked:
			Rate = 0.12
		if self._textBox1.Text == "":
			MessageBox.Show("Enter how many minutes the call lasted")
		else:
			Minutes = float(self._textBox1.Text)
			TotalCost = Minutes * Rate
			self._label9.Text = "$" + str(TotalCost)

	def Button2Click(self, sender, e):
		self._label9.Text = ""
		self.textBox1.Text = ""