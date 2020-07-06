#!usr/bin/python
__madeby__="Sarkis Derderian"

#Should be Quickbooks opened
import win32com.client
import xml.etree.ElementTree


# Connect to Quickbooks
sessionManager = win32com.client.Dispatch("QBXMLRP2.RequestProcessor")
sessionManager.OpenConnection('', 'Test qbXML Request')
ticket = sessionManager.BeginSession("", 0)

# Send query and receive responsec
qbxml_query ="""
<?qbxml version="4.0"?>
<QBXML>
   <QBXMLMsgsRq onError="continueOnError">
      <AccountQueryRq>
	<IncludeRetElement>Name</IncludeRetElement>
         <IncludeRetElement>Balance</IncludeRetElement>
      </AccountQueryRq>
   </QBXMLMsgsRq>
</QBXML>
"""
response_string = sessionManager.ProcessRequest(ticket, qbxml_query)


# Parse the response by Element Tree 
QBXML=xml.etree.ElementTree.fromstring(response_string)
QBXMLMsgsRs=QBXML.find('QBXMLMsgsRs')
AccountQueryRs=QBXMLMsgsRs.getiterator("AccountRet")


for account in AccountQueryRs:
    name=account.find('Name').text
    balance=account.find('Balance').text
    print(name,"\t|\t",balance)

# Disconnect from Quickbooks
sessionManager.EndSession(ticket)     # Close the company file
sessionManager.CloseConnection()      # Close the connection

