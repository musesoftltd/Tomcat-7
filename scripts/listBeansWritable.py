from library.tomcat.tomcatLib import getConnection, getDomainList, \
    getObjectNames


remoteServerConnection = getConnection("localhost", "8004")

domainList = getDomainList(remoteServerConnection)

for domain in domainList:
    print 'Domain:' + domain
    objectNames = getObjectNames(remoteServerConnection, domain)
    for name in objectNames:
        print ' Object Name:' + name.toString()
        mInfo = remoteServerConnection.getMBeanInfo(name)
        mBeanAttrs = mInfo.getAttributes()
        for attr in mBeanAttrs :
            if (attr.isWritable()) :
                print '  Attribute: ' + attr.getName() + ', type: ' + str(attr.getType()) + ', ' + name.toString() + ': is Writable'                        
