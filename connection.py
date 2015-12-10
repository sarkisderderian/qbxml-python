import win32com.client
import xml.etree.ElementTree as Et

def connect(company_name,company_file_path):
    #Connect 
    sessionManager = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
    sessionManager.OpenConnection('', company_name)
    ticket = sessionManager.BeginSession(company_file_path, 0)
    return (sessionManager,ticket)

def disconect(SessionManager):
    #Disconnect
    SessionManager.CloseConnection()
    return
