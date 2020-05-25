#!/usr/bin/env python
# coding: utf-8

# In[10]:


from os import listdir
from os.path import join
from PyPDF2 import PdfFileReader, PdfFileMerger


# In[11]:


def merge_pdf(files_dir, nome_saida):
    """Função para agrupar vários arquivos pdf em um só.
    
    Argumentos:
    files_dir (STRING): Caminho do diretório que contém os arquivos em pdf.
    nome_saida (STRING): Nome do arquivo de saída. Também poderá ser passado o caminho em que se deseja salvar.
    """
    
    pdf_files = [f for f in listdir(files_dir) if f.endswith("pdf")]
    merger = PdfFileMerger()

    for filename in pdf_files:
        merger.append(PdfFileReader(join(files_dir, filename), "rb"))

#     merger.write(os.path.join(files_dir, nome_saida))
    merger.write(nome_saida)
    
    return None


# In[13]:


merge_pdf('bases', 'arquivo.pdf')
print("PDF gerado.")
input("")

