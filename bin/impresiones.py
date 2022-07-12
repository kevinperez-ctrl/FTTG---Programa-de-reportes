import os
import win32print
import win32api

class MkPrints():
	def __init__(self, documento):
		GHOSTSCRIPT_PATH = "bin\\src\\GHOSTSCRIPT\\bin\\gswin32.exe"
		GSPRINT_PATH = "bin\\src\\GSPRINT\\gsprint.exe"
		
		currentprinter = win32print.GetDefaultPrinter()
		win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "'+documento+'"', '.', 0)