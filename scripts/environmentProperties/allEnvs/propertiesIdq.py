'''
Created on 4 Apr 2017

@author: x
'''


dictionary = {
    "port" : "8004",
    
    # properties auto-generated
    
    "Catalina:type=Service.name" : "Catalina",
    "Catalina:type=Service.managedResource" : "",
    "Catalina:type=StringCache.cacheSize" : "200",
    "Catalina:type=StringCache.trainThreshold" : "20000",
    "Catalina:type=StringCache.charEnabled" : "False",
    "Catalina:type=StringCache.byteEnabled" : "True",
    "Catalina:type=Valve,context=/,host=localhost,name=NonLoginAuthenticator.cache" : "True",
    "Catalina:type=Valve,context=/,host=localhost,name=NonLoginAuthenticator.changeSessionIdOnAuthentication" : "True",
    "Catalina:type=Valve,context=/,host=localhost,name=NonLoginAuthenticator.disableProxyCaching" : "True",
    "Catalina:type=Valve,context=/,host=localhost,name=NonLoginAuthenticator.securePagesWithPragma" : "False",
    "Catalina:type=Valve,host=localhost,name=StandardHostValve.asyncSupported" : "True",
    "Catalina:type=WebappClassLoader,context=/,host=localhost.delegate" : "False",
    "Catalina:type=WebappClassLoader,context=/,host=localhost.searchExternalFirst" : "False",
    "Catalina:type=WebappClassLoader,context=/,host=localhost.URLs" : "array(java.net.URL)",
    "Catalina:type=WebappClassLoader,context=/,host=localhost.antiJARLocking" : "False",
    "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none.runAs" : "None",
    "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none.available" : "0",
    "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none.backgroundProcessorDelay" : "-1",
    "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none.loadOnStartup" : "1",
    "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none.asyncSupported" : "False",
    "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none.objectName" : "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none",
    "Catalina:j2eeType=Servlet,name=default,WebModule=//localhost/,J2EEApplication=none,J2EEServer=none.maxInstances" : "20",
    "Catalina:type=Realm,realmPath=/realm0/realm0.allRolesMode" : "strict",
    "Catalina:type=Realm,realmPath=/realm0/realm0.digest" : "None",
    "Catalina:type=Realm,realmPath=/realm0/realm0.digestEncoding" : "None",
    "Catalina:type=Realm,realmPath=/realm0/realm0.realmPath" : "/realm0/realm0",
    "Catalina:type=Realm,realmPath=/realm0/realm0.resourceName" : "UserDatabase",
    "Catalina:type=Realm,realmPath=/realm0/realm0.validate" : "True",
    "Catalina:type=Host,host=localhost.aliases" : "array(java.lang.String)",
    "Catalina:type=Host,host=localhost.backgroundProcessorDelay" : "-1",
    "Catalina:type=Host,host=localhost.children" : "array(javax.management.ObjectName, [Catalina:j2eeType=WebModule,name=//localhost/,J2EEApplication=none,J2EEServer=none])",
    "Catalina:type=Host,host=localhost.deployXML" : "True",
    "Catalina:type=Host,host=localhost.workDir" : "None",
    "Catalina:type=Host,host=localhost.managedResource" : "",
    "Catalina:type=Host,host=localhost.undeployOldVersions" : "False",
    "Catalina:type=Host,host=localhost.deployIgnore" : "None",
    "Catalina:type=Host,host=localhost.valveNames" : "array(java.lang.String, [u'Catalina:type=Valve,host=localhost,name=AccessLogValve', u'Catalina:type=Valve,host=localhost,name=ErrorReportValve', u'Catalina:type=Valve,host=localhost,name=StandardHostValve'])",
    "Catalina:type=Host,host=localhost.deployOnStartup" : "True",
    "Catalina:type=Host,host=localhost.unpackWARs" : "True",
    "Catalina:type=Host,host=localhost.configClass" : "org.apache.catalina.startup.ContextConfig",
    "Catalina:type=Host,host=localhost.startStopThreads" : "1",
    "Catalina:type=Host,host=localhost.autoDeploy" : "True",
    "Catalina:type=Host,host=localhost.xmlBase" : "None",
    "Catalina:type=Host,host=localhost.appBase" : "webapps",
    "Catalina:type=Host,host=localhost.copyXML" : "False",
    "Catalina:type=Host,host=localhost.createDirs" : "True",
    "Catalina:type=Host,host=localhost.name" : "localhost",
    "Catalina:type=Host,host=localhost.realm" : "",
    "Catalina:type=Host,host=localhost.startChildren" : "True",
    "Catalina:type=Cache,host=localhost,context=/.desiredEntryAccessRatio" : "3",
    "Catalina:type=Cache,host=localhost,context=/.spareNotFoundEntries" : "500",
    "Catalina:type=Cache,host=localhost,context=/.maxAllocateIterations" : "20",
    "Catalina:type=Cache,host=localhost,context=/.cacheMaxSize" : "10240",
        
    # security hardening
    "x-powered-by" : "false",
    "rewrite-pattern" : "^(PUT|HEAD|DELETE|TRACE|TRACK|OPTIONS)$",
    "rewrite-flags" : "NC",
    "Http11Protocol" : "NotAvailable",
    "URI_ENCODING" : "UTF-8",
    "USE_BODY_ENCODING_FOR_QUERY_STRING" : "true",
    "enable-welcome-root": "false",
    "sampleWebAlias": "[\"localhost\"]",
    "customServerHeader": "NotAvailable",
    
    # SSL Ciphers
    "sslProtocols" : "TLSv1,TLSv1.1,TLSv1.2",
    "cipherSuite" : "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256"

}
