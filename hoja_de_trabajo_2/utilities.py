import csv

class Utilities:
    def csv_converter(self):
        with open(input('Seleccione un archivo CSV: '), newline='') as csvfile:
              lector_csv = csv.DictReader(csvfile)
              for fila in lector_csv:
                  print(fila['Zip'])
