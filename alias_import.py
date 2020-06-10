# alias_import.py

import os, sys

FILE_NAME = ""
file_data = ""
aliases = {}

try:
	FILE_NAME = sys.argv[1]
except IndexError:
	print("Please specify a file name.")
	sys.exit()

with open(FILE_NAME, "r") as java_file:
	file_data = java_file.read()

up_until_class = file_data[:file_data.find("public")]
import_code = up_until_class.split()

file_data = file_data.replace("\t", "    ")

for index, token in enumerate(import_code):
	if token == "import":
		package = import_code[index + 1]
		if not package.endswith(";"):
			aliases[" " + import_code[index + 3].rstrip(";")] = package

for alias, real_name in aliases.items():
	file_data = file_data.replace(alias, real_name)

for index, token in enumerate(import_code):
	if token == "as":
		import_code[index], import_code[index + 1] = None, None
		import_code[index - 1] += ";"

while None in import_code:
	import_code.remove(None)


modified_imports = "".join([token + " " for token in import_code]).rstrip()

file_data = file_data.split()
file_without_imports = file_data[file_data.index("public"):]

properly_spaced_version = "".join([token + " " for token in file_without_imports]).rstrip()

final_file_revision = modified_imports + properly_spaced_version
final_file_revision = final_file_revision.replace(";", ";\n").replace("{", "{\n").replace("}", "}\n")

# print("Final file revision:", final_file_revision)

os.system(f"mkdir No_Alias:\\ {FILE_NAME}")
with open(f"No_Alias: {FILE_NAME}/{FILE_NAME}", "w") as output_file:
	output_file.write(final_file_revision)
