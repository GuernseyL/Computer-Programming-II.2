
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Student(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(29, 24)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(187, 27)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of tickets:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(222, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(194, 31)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(459, 28)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(192, 92)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CornflowerBlue
		self._label2.Location = System.Drawing.Point(12, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(419, 58)
		self._label2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.CornflowerBlue
		self._label3.Location = System.Drawing.Point(437, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(232, 315)
		self._label3.TabIndex = 4
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(459, 126)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(192, 86)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.CornflowerBlue
		self._label4.Location = System.Drawing.Point(12, 88)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(419, 236)
		self._label4.TabIndex = 6
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(29, 107)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(166, 29)
		self._label5.TabIndex = 7
		self._label5.Text = "Cost of Tickets:"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(29, 193)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(131, 29)
		self._label6.TabIndex = 8
		self._label6.Text = "Cost of Tax:"
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(29, 283)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(118, 29)
		self._label7.TabIndex = 9
		self._label7.Text = "Total Cost:"
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(201, 107)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(215, 29)
		self._label8.TabIndex = 10
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(166, 193)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(250, 29)
		self._label9.TabIndex = 11
		# 
		# label10
		# 
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(153, 283)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(263, 29)
		self._label10.TabIndex = 12
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(459, 218)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(192, 82)
		self._button3.TabIndex = 13
		self._button3.Text = "Return to Main Screen"
		self._button3.UseVisualStyleBackColor = True
		# 
		# Student
		# 
		self.ClientSize = System.Drawing.Size(681, 350)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label3)
		self.Name = "Student"
		self.Text = "Student"
		self.FormClosing += self.StudentFormClosing
		self.ResumeLayout(False)
		self.PerformLayout()


	def StudentFormClosing(self, sender, e):
		self.myparent.Show()

	def Button1Click(self, sender, e):
		tickets = self._textBox1.Text
		CoT = 7.00 * tickets
		CoTax = CoT * 0.055
		TC = CoTax + CoT
		self._label8.text = "$" + str(Round(CoT, 3))
		self._label9.text = "$" + str(Round(CoTax, 3))
		self._label10.text = "$" + str(Round(TC, 3))
		