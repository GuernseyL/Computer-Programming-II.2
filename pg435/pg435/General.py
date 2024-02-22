
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class General(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self.SuspendLayout()
		# 
		# General
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Name = "General"
		self.Text = "General"
		self.FormClosing += self.GeneralFormClosing
		self.ResumeLayout(False)


	def GeneralFormClosing(self, sender, e):
		self.myparent.Show()