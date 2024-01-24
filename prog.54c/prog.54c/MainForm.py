import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Goldenrod
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(104, 6)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(246, 31)
		self._textBox1.TabIndex = 16
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkOrange
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 84)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(338, 24)
		self._label4.TabIndex = 15
		self._label4.Text = "Area:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkOrange
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 48)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(338, 24)
		self._label3.TabIndex = 14
		self._label3.Text = "Circumfrence:"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkOrange
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(85, 28)
		self._label1.TabIndex = 12
		self._label1.Text = "Radius:"
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Chocolate
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(246, 123)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 57)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Chocolate
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(129, 123)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(111, 57)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Chocolate
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 123)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(111, 57)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PeachPuff
		self.ClientSize = System.Drawing.Size(365, 188)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog.54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Radius = float(self._textBox1.Text)
		Circumfrence = Radius * 2 * 3.141
		Area = Radius ** 2 * 3.141
		self._label3.Text = "Circumfrence: " + str(round(Circumfrence, 3))
		self._label4.Text = "Area: " + str(round(Area, 3))
		

	def Button2Click(self, sender, e):
		self._label3.Text = "Circumfrence: "
		self._label4.Text = "Area: "
		self._textBox1.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()