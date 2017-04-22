# -*- coding: utf-8 -*- 
import sys
import configparser
from modules.DictParser import *

class MainProgram:
	def __init__(self):
		self.err = False
		self.err_desc = ""
		cfg = {}
		
	def rise_err(self, method_name, err_desc):
		self.err = True
		self.err_desc = "\n  Error in '" + self.__class__.__name__ + "." + method_name + "':" + err_desc + "\n"

	def read_ini(self, ini_file):
		cfg = {}
		config = configparser.ConfigParser()
		config.read(ini_file)
		for section in config.sections():
			cfg[section] = {}
			for key in config[section]:
				cfg[section][key] = config[section][key]
		return cfg

	def main(self, arguments):
		if len(arguments) > 1:
			self.cfg = self.read_ini(arguments[1])
			# --------- write your code here ---------
			dict_parser = DictParser()
			work_folder = self.cfg['path']['work_folder']
			dict_name = self.cfg['params']['dict_name']
			output_folder = self.cfg['path']['output_folder']
			dict_parser.parse(work_folder, dict_name, output_folder)
			if (dict_parser.err):
				self.rise_err(sys._getframe().f_code.co_name, dict_parser.err_desc)
			# ---------------------------------------------
		else:
			self.rise_err(sys._getframe().f_code.co_name, "ini file not present")

main_program = MainProgram()
main_program.main(sys.argv)
if main_program.err:
	print(main_program.err_desc)