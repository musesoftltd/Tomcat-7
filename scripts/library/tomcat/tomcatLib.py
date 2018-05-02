import array
from java.lang import Object, String
from javax.management import ObjectName, Attribute
import javax.management.remote.JMXConnectorFactory
import javax.management.remote.JMXServiceURL
import sys
from time import sleep
import traceback

from library.util import extractDatasourceName, extractXADatasourceName, \
    sanitizeJDBCCliVector, stripQuotes, regularExpressionSearch
    
def getConnection(host, port):
    serviceURL = "service:jmx:rmi:///jndi/rmi://"
    serviceURL = serviceURL + host + ":" + str(port) + "/jmxrmi"
 
    url = javax.management.remote.JMXServiceURL(serviceURL)
    connector = javax.management.remote.JMXConnectorFactory.connect(url)
    remoteServerConnection = connector.getMBeanServerConnection()
    return remoteServerConnection
 
def getDomainList(remoteServerConnection):
    domainList = remoteServerConnection.getDomains()
    return domainList
 
def getObjectNames(remoteServerConnection, domain):
    objectNames = remoteServerConnection.queryNames(ObjectName(domain + ":*"), None)
    return objectNames
 
def getMbeans(remoteServerConnection, domain):
    mbeans = remoteServerConnection.queryMBeans(ObjectName(domain + ":*"), None)
    return mbeans
 
def printDomainList(remoteServerConnection):
    domainList = getDomainList(remoteServerConnection)
    print 'Domain List:'
    for element in domainList:
        print '    ' + element
 
def printMBeanList(remoteServerConnection, domain):
    print 'Domain:' + domain + ' has MBeans:'
    mbeans = remoteServerConnection.queryMBeans(ObjectName(domain + ":*"), None)
    for mbean in mbeans :
        print '    mbean:' + str(mbean)  
 
def getAttribute(remoteServerConnection, objectNameStr, attributeStr):
    obn = javax.management.ObjectName(objectNameStr)
    oAttribute = remoteServerConnection.getAttribute(obn, attributeStr)
    return oAttribute
 
def getAttributeValuesHost(host, port, objectNameStr, attributeStr):
    remoteServerConnection = getConnection(host, port)
    obn = javax.management.ObjectName(objectNameStr)
    oAttribute = remoteServerConnection.getAttribute(obn, attributeStr)
 
    if (str(oAttribute.getType()) != None) : 
                 
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
     
        value = getAttribute(remoteServerConnection, str(objectNameStr), str(oAttribute.getName()))
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
     
 
    return oAttribute.keyPropertyList
 
def getAttributeValuesConnection(remoteServerConnection, objectNameStr, attributeStr):
    obn = javax.management.ObjectName(objectNameStr)
    oAttribute = remoteServerConnection.getAttribute(obn, attributeStr)
 
    if (str(oAttribute.getType()) != None) : 
                 
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
     
        value = getAttribute(remoteServerConnection, str(objectNameStr), str(oAttribute.getName()))
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
 
    return oAttribute.keyPropertyList

def setAttributeHost(host, port, objectNameString, attribute, value):
    remoteServerConnection = getConnection(host, port)
    obn = javax.management.ObjectName(objectNameString)
    oAttribute = Attribute(attribute, value)
    result = remoteServerConnection.setAttribute(obn, oAttribute)
    return result

def setAttributeConnection(remoteServerConnection, objectNameString, attribute, value):
    obn = javax.management.ObjectName(objectNameString)
    oAttribute = Attribute(attribute, value)
    result = remoteServerConnection.setAttribute(obn, oAttribute)
    return result

def setParameterValue(servername, cliVector, cliProperty, targetValue, username='', password='', reloadServerIfRequired=False):
    cliConnected = None
    appliedOk = False
    
    print 'On Server :' + servername + ' applying ->' + cliProperty + '<- from CLI Vector ->' + cliVector + '<- ...'
    try:
        cliConnected = getConnection(servername)
        if (cliConnected != None):
            dealingWithADatasource = False
            dealingWithAnXaDatasource = False
            # check for regular datasource...
            datasourceName = extractDatasourceName(cliVector)
            xaDatasourceName = extractXADatasourceName(cliVector)
                        
            if (targetValue.lower() == "undefined".lower()) :
                # We must undefine a value, we cannot use set...
                cliCmd = str(cliVector) + ':undefine-attribute(name=' + str(cliProperty) + ')'
            else:
                if (isinstance (targetValue, int)) :
                    cliCmd = str(cliVector) + ':write-attribute(name=' + str(cliProperty) + ',value=' + targetValue + ')'
                else :    
                    cliCmd = str(cliVector) + ':write-attribute(name=' + str(cliProperty) + ',value=\"' + stripQuotes(targetValue) + '\")'
           
            print 'Issuing Server Command ->' + cliCmd + '<-'
            
            try :
                cliResult = cliConnected.cmd(cliCmd)
                
                if cliResult.success:
                    appliedOk = True
                    print 'On Server :' + servername + ' applied :' + targetValue
                else:
                    appliedOk = False
                    print 'Command Issue Failure ->' + cliCmd + '<-'
                    print cliResult.getResponse().get("failure-description").asString()
                    print cliResult.getResponse().get("response-headers").asString()
                
            except :
                print 'Exception Issuing Server Command ->' + cliCmd + '<- caused an exception. FAILED.'

                exc_type, exc_value, exc_traceback = sys.exc_info()
                print "*** print_tb:"
                traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
                print "*** print_exception:"
                traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
                print "*** format_exc, first and last line:"
                formatted_lines = traceback.format_exc().splitlines()
                print formatted_lines[0]
                print formatted_lines[-1]          
    except:
        appliedOk = False        
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print "*** print_tb:"
        traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
        print "*** print_exception:"
        traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
        print "*** format_exc, first and last line:"
        formatted_lines = traceback.format_exc().splitlines()
        print formatted_lines[0]
        print formatted_lines[-1]
        print 'On Server :' + servername + ' applying ->' + cliProperty + '<- from CLI Vector ->' + cliVector + '<- ...FAILED.'
    finally:
        if (cliConnected != None) : cliConnected.disconnect()
    
    if (reloadServerIfRequired) :
        print 'Here we ought to restart/load the server'    
#         if isServerReloadRequired(servername, username, password):
#             reloadServerThenWait(servername, username, password)
        
    print 'On Server :' + servername + ' applying ->' + cliProperty + '<- from CLI Vector ->' + cliVector + '<- ...end.'
    return appliedOk 

def getParameterValue(servername, username, password, cliVector, cliProperty, reloadServerIfRequired=False):
    retries = 1
    attempts = 0
    
    cliConnected = None
    currentValue = ''
    cliResult = None

    if (reloadServerIfRequired) :
        print 'Here we ought to restart/load the server'    
#         if isServerReloadRequired(servername, username, password):
#             reloadServerThenWait(servername, username, password)

    while (attempts <= retries) :
        try:
            attempts += 1
            print ''
            print 'On Server :' + servername + ' retrieving ->' + cliProperty + '<- from CLI Vector ->' + cliVector + '<- ...'
            cliConnected = getConnection(servername)
            if (cliConnected != None):
                    dealingWithADatasource = False
                    dealingWithAnXaDatasource = False
                    # check for regular datasource...
                    datasourceName = regularExpressionSearch("/subsystem=datasources/data-source=(.*)/", cliVector)
                    xaDatasourceName = regularExpressionSearch("/subsystem=datasources/xa-data-source=(.*)/", cliVector)
                                
                    if (datasourceName != '') :
                        # then we are dealing with a datsource.
                        # better stop then start it.
                        dealingWithADatasource = True
    
                        # if the datasource contains '/' we MUST escape it to work... 
                        cliVector = sanitizeJDBCCliVector(cliVector)
                    elif (xaDatasourceName != '') :
                        dealingWithAnXaDatasource = True
    
                        # if the datasource contains '/' we MUST escape it to work... 
                        cliVector = sanitizeJDBCCliVector(cliVector)
                                    
                    cliCmd = str(cliVector) + ':read-attribute(name=' + str(cliProperty) + ')'
                    
                    print 'Issuing Server Command ->' + cliCmd + '<-'
                    
                    cliResult = cliConnected.cmd(cliCmd)
                    
                    if cliResult.success:
                        appliedOk = True
                        response = cliResult.getResponse()
                        currentValue = response.get("result").asString()
                        print 'On Server :' + servername + ' retrieved :' + currentValue
                    else:
                        appliedOk = False
                        print 'Command Issue Failure ->' + cliCmd + '<-'
                        print 'On Server :' + servername + ' retrieving :' + cliProperty + ' from CLI Vector :' + cliVector + ' ...FAILED.'                        
                        print cliResult.getResponse().get("failure-description").asString()
                        print cliResult.getResponse().get("response-headers").asString()
                        currentValue = "Unknown"
                                                               
        except :
            print 'Exception Issuing Server Command ->' + cliCmd + '<- caused an exception. FAILED.'

            exc_type, exc_value, exc_traceback = sys.exc_info()
            print "*** print_tb:"
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            print "*** print_exception:"
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
            print "*** format_exc, first and last line:"
            formatted_lines = traceback.format_exc().splitlines()
            print formatted_lines[0]
            print formatted_lines[-1] 
            
        finally:
            if (cliConnected != None) : cliConnected.disconnect()
      
        print 'On Server :' + servername + ' retrieving ->' + cliProperty + '<- from CLI Vector ->' + cliVector + '<- ...end.'
        
        if ((cliConnected != None) and (currentValue != "Unknown") and (currentValue != "")):
            break
        else :
            sleep (0.2)
        
    return currentValue 

