import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(261, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(277, 52)
		self._button1.TabIndex = 0
		self._button1.Text = "Student Sales"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(261, 86)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(277, 52)
		self._button2.TabIndex = 1
		self._button2.Text = "General Sales"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 17)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(243, 52)
		self._label1.TabIndex = 2
		self._label1.Text = "Student Sales: All sales sold to students:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 86)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(243, 52)
		self._label2.TabIndex = 3
		self._label2.Text = "General Sales: All sales sold to the public:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(553, 149)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg435"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Student import *
		student = Student(self)
		student.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from General import *
		general = General(self)
		student.Show()
		self.Hide()