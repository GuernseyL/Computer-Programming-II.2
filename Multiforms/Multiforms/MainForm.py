﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(49, 40)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(380, 364)
		self._button1.TabIndex = 0
		self._button1.Text = "Show New Form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(467, 445)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Multiforms"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Hello, world!")
		form1.Show()
		self.Hide()
		
		from FormioNumerioDosio import *
		form2 = FormioNumerioDosio()
		form2.Show()