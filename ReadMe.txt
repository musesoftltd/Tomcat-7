########################################################
# For Tomcat Scripting
########################################################

The JMX functionality in Tomcat can be made available by enabling a JMX port.
If you are using Eclipse to manage your Tomcat instance,
	You will need to edit the launch configuration properties for the Tomcat instance.
	For the VM (x)= Arguments tab.
	Enter -Dcom.sun.management.jmxremote.port=8004 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false
		in the VM Arguments entry. Screenshot in JMX for Eclipse Managing Tomcat Instance.png

If you are using an externally managed Tomcat Instance.
Add the following parameters to setenv.bat, or catalina.bat script of your Tomcat 
(see RUNNING.txt for details).
Note: This syntax is for Microsoft Windows. 
The command has to be on the same line. It is wrapped to be more readable. 
If Tomcat is running as a Windows service, use its configuration dialog to set 
	java options for the service. For un*xes remove "set " from beginning of the line.


set CATALINA_OPTS=-Dcom.sun.management.jmxremote
  -Dcom.sun.management.jmxremote.port=8004
  -Dcom.sun.management.jmxremote.ssl=false
  -Dcom.sun.management.jmxremote.authenticate=false

Here it is on one line for your convenience;
-Dcom.sun.management.jmxremote.port=8004 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false

    If you require authorization, add and change this:


      -Dcom.sun.management.jmxremote.authenticate=true
      -Dcom.sun.management.jmxremote.password.file=../conf/jmxremote.password
      -Dcom.sun.management.jmxremote.access.file=../conf/jmxremote.access
      
    edit the access authorization file $CATALINA_BASE/conf/jmxremote.access:


    monitorRole readonly
    controlRole readwrite

    edit the password file $CATALINA_BASE/conf/jmxremote.password:


    monitorRole tomcat
    controlRole tomcat

    Tip: The password file should be read-only and only accessible by the operating system user Tomcat is running as.
