'''
Created on 11 Oct 2016

@author: ...
'''

from environmentProperties.localhost.inventory import servers as localServers
from environmentProperties.localhost.properties import dictionary as localServerDictionary
from library.auditing.auditingLibrary import auditInitAudit
from library.informatica.auditServers_IDQ import auditServersIDQ

auditInitAudit("localMachine", "Informatica IDQ")

# whether to allow the auditing framework to make changes to correct its findings...
applyChanges = False

auditServersIDQ("Local Reference - Informatica IDQ", localServers, localServerDictionary, applyChanges)

exit()
