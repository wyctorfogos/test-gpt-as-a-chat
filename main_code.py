import os 
import re
import PyPDF2
from PyPDF2 import PdfReader
import docx
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

 
def read_files(path_to_files):
    with open(path_to_files, "rb") as file:
        pdf = PdfReader(file)
        text = ""
        for page in range(len(pdf.pages)):
            aux=pdf.pages[page].extract_text()
            text+=aux
            print(aux)
            del aux
    return text

def read_word(path_to_files):
    document=docx.Document(path_to_files)
    text=""
    for paragraph in range(len(document)):
        text+= paragraph.text+"\n"
    return text
if __name__=='__main__':
    print(read_word('../QUESTIONS_ABOUT_GOD/dataset/Bible.pdf'))