'''
Created on 20 Oct 2016

@author: ...
'''

from environmentProperties.allEnvs.propertiesIdq import dictionary as globalDictionary
from library.auditing.auditingLibrary import auditObjectAtom, \
    auditObjectMolecule, auditReport, auditObjectAtoms
from library.util import scatterThread, gatherThreads


def auditServersIDQThread(environment, servername, propertiesDictionary, bApplyRequiredChanges): 
    runtimeProperties = dict()
    runtimeProperties.update(globalDictionary)
    runtimeProperties.update(propertiesDictionary)

#     if connectSilent(servername, runtimeProperties["username"], runtimeProperties["password"]) == None:
#         return
            
    auditObjectAtoms.append(auditObjectAtom(servername, runtimeProperties["port"], runtimeProperties["username"], runtimeProperties["password"], "ajp-bio - ThreadPool", "Catalina:type=ThreadPool,name=\"ajp-bio-8009\"", "maxThreads", runtimeProperties["maxThreads"], False))    
                
    
def auditServersIDQ(environment, servers, propertiesDictionary, bApplyRequiredChanges) :
    # merge global properties into dict - deliberately overwriting local with global dict all values

    strThreadPoolId = "auditServersIDQ"
    for servername in servers:
        # Create new threads
        scatterThread(strThreadPoolId, auditServersIDQThread, args=(environment, servername, propertiesDictionary, bApplyRequiredChanges))

    gatherThreads(strThreadPoolId)

    for servername in servers:
        auditReport(environment, servername)
