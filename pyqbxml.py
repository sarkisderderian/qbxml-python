#!usr/bin/python
__Authorization__="Sarkis Derderian"
#import library for connect to quickbook but note you shoud have admin access
import connect

path="C:\Documents and Settings\All Users\Documents\Intuit\QuickBooks\Company Files\demo.qbw"
name="demo"

s,t=connect.start(name,path)


# Send query and receive responsec
qbxml_query = 
"""
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
qbxml_response = s.ProcessRequest(t, qbxml_query)

#Disconnect connection
s.EndSession(t)
s.CloseConnection()


# Parse the response by Element Tree 
QBXML=connect.Et.fromstring(qbxml_response)

QBXMLMsgRs=QBXML.find("QBXMLMsgsRs")
AccountRet=QBXMLMsgRs.getiterator("AccountRet")

for a in AccountRet:
    names=a.find('Name').text
    balances=a.find('Balance').text
    print names,"\t|\t",balances

