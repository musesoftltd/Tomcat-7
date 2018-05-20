from time import sleep

from library.tomcat.tomcatLib import getConnection, getDomainList, \
    getObjectNames, getParameterValue
from library.util import appendToFile, writeToFile, mkdir_p


host = "localhost"
port = "8004"
username = ""
password = ""

mkdir_p("./autoGen")
auditAtomFile = "./autoGen/CodeGen.AuditAtomsWritable.py"
auditPropertyFile = "./autoGen/CodeGen.PropertiesWritable.py"

remoteServerConnection = getConnection(host, port)

domainList = getDomainList(remoteServerConnection)

writeToFile("\n", auditAtomFile) # reset file
writeToFile("\n", auditPropertyFile) # reset file

for domain in domainList:
    
    print "# Code generation. Copy AuditAtoms generated into your code.\n"
    print '# Domain:' + domain
    appendToFile("# Code generation. Copy AuditAtoms generated into your code.\n", auditAtomFile)
    appendToFile('# Domain:' + domain + "\n", auditAtomFile)
    objectNames = getObjectNames(remoteServerConnection, domain)
    
    for objectName in objectNames:
        sleep(0.1)        
        #print ' Object Name:' + name.toString()
        mInfo = remoteServerConnection.getMBeanInfo(objectName)
        mBeanAttrs = mInfo.getAttributes()
        for attr in mBeanAttrs :
            if (attr.isWritable()) :
                #print '  Attribute: ' + attr.getName() + ', type: ' + str(attr.getType()) + ', ' + name.toString() + ': is Writable'                        
                strToPrintAndUse = "\t" + "auditObjectAtoms.append(auditObjectAtom(servername, runtimeProperties[\"port\"], runtimeProperties[\"username\"], runtimeProperties[\"password\"], \"" + domain + ". " + attr.getName() + "\", \"" + objectName.toString() + "\", \"" + attr.getName() + "\", runtimeProperties[\"" + objectName.toString()+ "."+attr.getName() + "\"], bApplyRequiredChanges))"
                print strToPrintAndUse
                
                appendToFile(strToPrintAndUse + "\n", auditAtomFile)
                
    print "# Code generation. Copy Properties generated into your Dictionaries.\n"
    print '# Domain:' + domain
    appendToFile("# Code generation. Copy Properties generated into your Dictionaries.\n", auditPropertyFile)
    appendToFile('# Domain:' + domain + "\n", auditPropertyFile)
    for objectName in objectNames:
        sleep(0.1)        
        #print ' Object Name:' + name.toString()
        mInfo = remoteServerConnection.getMBeanInfo(objectName)
        mBeanAttrs = mInfo.getAttributes()
        for attr in mBeanAttrs :
            if (attr.isWritable()) :
                #print '  Attribute: ' + attr.getName() + ', type: ' + str(attr.getType()) + ', ' + name.toString() + ': is Writable'
                strToPrintAndUse = "\t\"" + objectName.toString()+ ". "+attr.getName() + "\" : \"" + getParameterValue(host, port, username, password, objectName.toString(), attr.getName(), silent=True) + "\","
                print strToPrintAndUse
                
                appendToFile(strToPrintAndUse + "\n", auditPropertyFile)
