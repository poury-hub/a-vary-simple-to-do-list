import re

import json 
import R_storage
import W_storage
import state_changer

from R_storage import readboy
from W_storage import add_task
from state_changer import Done , Deleter



instractions = '''
for adding a new task use  -> \t\t\t add {Title} 
for deleting a task use  -> \t\t\t del {ID}  
if you want to mark a task a finished use  -> \t done {ID} 
if you wish to quit use  -> \t\t\t q 
      '''
def main():
      readboy()
      while(True):
            
            
            print(instractions)
            
            
            text = input()
            if text == 'q': return

            text = re.search(r'([a-zA-Z]+) (\d+|[a-zA-Z ]+)' , text)
            command = text.group(1)
            T = text.group(2)
                        
                  
            
            match command:
                  case 'add':
                        if(add_task(T)):
                              readboy()
                              print("\n task added successfully")
                        else:
                              print('invalid input please try again')
                  case 'del':
                        if(Deleter(T)):
                              readboy()
                              print("\n task deleted successfully")
                        else:
                              print('invalid input please try again')
                  case 'done':
                        if(Done(T)):
                              readboy()
                              print("\n task marked as finished")
                        else:
                              print('invalid input please try again')



main()




