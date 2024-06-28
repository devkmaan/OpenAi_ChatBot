from db_call import QASystem
import pandas as pd
import csv

def chatbot(input):
    # First try to get a response from the QASystem
    # Initialize the QASystem
    qa = QASystem('test.csv')
    try:
        qa_response = qa.get_response(input)
        print("Try")
    except:
        qa_response = "I can't answer this question."
        print("Except")
    return qa_response

