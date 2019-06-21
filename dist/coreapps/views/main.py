#!usr/bin/env python
from pathlib import Path
import platform

import wx

# from AppsSDS.SDSHollandWindowUtama import SDSHollandWindowUtama as I


# class run(I):
# 
# 	def __init__(self, *args, **kwrgs):
# 		super(run, self).__init__(*args, **kwrgs)
# 
# 	pass


root = wx.App()


class VerifyKey():
	
	def __init__(self, parent):
		self.value = parent
		pass
	
	def Verify(self):
		
		return self.value

	def __repr__(self):
		return str(self.value)


def openWindows():
# 	start = run(None)
# 	start.Show()
# 	root.MainLoop()	
	# print ("lewat sini")
	return None


def close():
	from coreapps.views.authenticationFrameWarningKey import authenticationFrameWarningKey
	start = authenticationFrameWarningKey(None)
	start.Show()
	root.MainLoop()
	# print ("lewat close")
	return None

# my_file = Path("/home/binakarir/Projects/PySDS/run.py")


if platform.system() == "Windows":
	print (platform.system())
	my_file = Path("C:\\ProgramData\\3351.txt")

	# print (my_file)
	if my_file.is_file():
		# print ("file ada")
		openWindows()

	else : 
		# print ("file tidak ada")
		
		KeyVerification = VerifyKey("2")
		# print (KeyVerification.Verify())
		# print (type(KeyVerification))

		if KeyVerification.Verify() == "1":
			openWindows()

		else :
			close()

elif platform.system() == "Linux" :
	print (platform.system())
	my_file = Path.home() / ".3351"
	# print (my_file)
	if my_file.is_file():
		# print ("file ada")
		openWindows()
		print ("le")
	else : 
		# print ("file tidak ada")
# 		KeyVerification = VerifyKey("2")
		# print (KeyVerification.Verify())
		# print (type(KeyVerification))

		if KeyVerification.Verify() == "1":
			openWindows()

		else :
			close()
