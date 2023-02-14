from pathlib import Path
from pandas import read_excel, DataFrame

#Nome ou caminho do arquivo
folder = Path("./data")

#onde será acoplado os dados
df = []

# Qualquer coisa (*) que contenha xlsx no diretório
for file in folder.glob("*.xlsx"):
    
    #File.name  == nome do arquivo exato
    print(f"Loading file {file.name}")
    
    #Pega conteudo de uam lsita e coloca em outra, resolve == resolve o caminho do arquivo, volta o caminho completo
    df.extend((read_excel(file.resolve())
               .to_dict("records")))

print(len(df))

#Cria o DataFrame e gera o arquivo xlsx
df_principal = DataFrame(df)
df_principal.to_excel('./todas_as_consultas.xlsx', index=False)