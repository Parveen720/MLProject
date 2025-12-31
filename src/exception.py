import sys
import logging
#get this document in python exception handling 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
      file_name,exc_tb.tb_lineno,str(error))

    return error_message
    


class CustomException(Exception):
    #constructor hota h python ek tarike se ye def init
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        #super use hota h parent class ka contructor k liye
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        #self kaam aata h ek trike se value ko store krne k liye kisi m
        def __str__(self):
            return self.error_message