import pefile
import hashlib

#Abrir los archivos
pe= pefile.PE('sample_vg655_25th.exe')
pe2= pefile.PE('sample_qwrty_dk2')

#Obtener DLL's y llamadas
print('DLLs y Llamadas para el archivo sample_vg655_25th.exe:')
for entry in pe.DIRECTORY_ENTRY_IMPORT:
	print('DLL: ', entry.dll)
	print('Llamadas a funciones:')
	for function in entry.imports:
		print('\t', function.name)
print('\n')

print('DLLs y Llamadas para el archivo sample_qwrty_dk2:')
for entry in pe2.DIRECTORY_ENTRY_IMPORT:
	print('DLL: ', entry.dll)
	print('Llamadas a funciones:')
	for function in entry.imports:
		print('\t', function.name)
print('\n')

#Obtener secciones
print('Secciones para el archivo sample_vg655_25th.exe:')
for section in pe.sections:
	print(section.name, hex(section.VirtualAddress), hex(section.Misc_VirtualSize), section.SizeOfRawData)
print('\n')

print('Secciones para el archivo sample_qwrty_dk2:')
for section in pe2.sections:
	print(section.name, hex(section.VirtualAddress), hex(section.Misc_VirtualSize), section.SizeOfRawData)
print('\n')
	
#Calcular Hash SHA256
print('Hash SHA256 para el archivo sample_vg655_25th.exe:')
filename='sample_vg655_25th.exe'
with open(filename,"rb") as f:
    bytes = f.read() # read entire file as bytes
    readable_hash = hashlib.sha256(bytes).hexdigest();
    print(readable_hash)