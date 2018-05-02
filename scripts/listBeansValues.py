from __builtin__ import isinstance
import array
from jarray import array_class
from java.lang import Integer, String
from java.lang.reflect import Array
 
from tomcat.tomcatLib import getConnection, getDomainList, \
    getObjectNames, getAttribute
 
remoteServerConnection = getConnection("localhost", "8004")
 
domainList = getDomainList(remoteServerConnection)
 
for domain in domainList:
    print 'Domain:' + domain
    objectNames = getObjectNames(remoteServerConnection, domain)
    for objectName in objectNames:
        print ' Object Name:' + str(objectName)
        mInfo = remoteServerConnection.getMBeanInfo(objectName)
        mBeanAttrs = mInfo.getAttributes()
        for oAttribute in mBeanAttrs :    
            if not(oAttribute.isWritable()) :
                print '  Attribute, Name: ' + oAttribute.getName() + ', type: ' + str(oAttribute.getType()) + ': is ReadOnly'
            if not(oAttribute.isReadable()) :
                print '  Attribute, Name: ' + oAttribute.getName() + ', type: ' + str(oAttribute.getType()) + ': is Not Readable'
                continue
            if (oAttribute.isWritable()) :
                print '  Attribute, Name: ' + oAttribute.getName() + ', type: ' + str(oAttribute.getType()) + ': is Writable'
 
            if (str(oAttribute.getType()) != "None") :                 
                # Filter non basetypes
                if (String(oAttribute.getType()).toString()).__contains__("int"):
                    None
                elif (String(oAttribute.getType()).toString()).__contains__("String"):
                        None    
                elif (String(oAttribute.getType()).toString()).__contains__("Float"):
                        None
                elif (String(oAttribute.getType()).toString()).__contains__("array"):
                        None
                        
    #             elif (String(oAttribute.getType()).toString()).__contains__("long"):
    #                     None
    #             elif (String(oAttribute.getType()).toString()).__contains__("boolean"):
    #                     None
                else:
                    print "  Attribute Type: " + oAttribute.getType() + " : Can't be handled"
                    break    
     
                value = getAttribute(remoteServerConnection, str(objectName), str(oAttribute.getName()))
                if (String(str(value))).contains("array"):
                    for entry in value:
                        print "   Value: " + str(entry) + "\n"
                elif (isinstance(value, long)):
                    print "   Value: " + str(value)
                elif (isinstance(value, int)):
                    print "   Value: " + str(value)
                elif (isinstance(value, array)):
                    for entry in value:
                        print "   Value: " + str(entry) + "\n"
                else :
                    print "   Value: " + str(value) + "\n"
     