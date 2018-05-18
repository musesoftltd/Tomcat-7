from library.tomcat.tomcatLib import getConnection, printDomainList, \
    getDomainList, printMBeanList, getAttribute

remoteServerConnection = getConnection("localhost", "8004")
printDomainList(remoteServerConnection)

domainList = getDomainList(remoteServerConnection)

for domain in domainList:
    printMBeanList(remoteServerConnection, domain)

baseDir = getAttribute(remoteServerConnection, "Catalina:type=Engine", "baseDir")
print "Tomcat Installation Folder: " + baseDir

appBase = getAttribute(remoteServerConnection, "Catalina:type=Host,host=localhost", "appBase")
print "Tomcat Deployment Folder: " + appBase

print 'Tomcat Full Deployment Folder: ' + baseDir + '\\' + appBase
