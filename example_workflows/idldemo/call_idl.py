import reflex 
import sys
import os

if __name__ == '__main__':

  #define i/o
  parser = reflex.ReflexIOParser()
  parser.add_option("-i", "--in_sof", dest="in_sof")
  parser.add_output("-o", "--out_sof", dest="out_sof")
  inputs  = parser.get_inputs()
  outputs = parser.get_outputs()


  #Initialize output:
  outputs.out_sof = inputs.in_sof

  # To call idl for a category of files (e.g., MASTER_BIAS):
  # uncomment the line #if file.category == 'MASTER_BIAS' : listed below
  for file in inputs.in_sof.files:
    #select a file category:
    #if file.category == 'MASTER_BIAS' : 
      infile = file.name
      newname= file.name.replace(".fits", "_new.fits")
      file.name= newname
      os.system("csh -c 'idl -e myidlscript -args \""+infile+"\" \""+newname+"\"'")


  #write the output 
  outputs.out_sof = inputs.in_sof
  parser.write_outputs()

