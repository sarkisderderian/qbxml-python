import win32com.client
import xml.etree.ElementTree as Et

# i remove the second parameter (company_file_path) becuase i want to be only with opened file.
def connect(company_name):
    #Connect 
    sessionManager = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
    sessionManager.OpenConnection('', company_name)
    # i remove the first parameter (company_file_path) because i want to be only with opened file.
    # i put second parameter 1 because i use multi user quickbooks Desktop
    ticket = sessionManager.BeginSession('', 1)
    return (sessionManager,ticket)

def disconect(SessionManager):
    #Disconnect
    SessionManager.CloseConnection()
    return
