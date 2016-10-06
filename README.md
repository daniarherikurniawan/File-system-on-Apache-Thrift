#APACHE THRIFT

##1. Generate Code
###Install
		According to https://thrift.apache.org/tutorial/
	
###Syntax Gen-java
		- Move directory to .thrift file
			``` cd Server/tutorial/
		- thrift --gen java file_system.thrift
###Create Client and Server
		- move file gen-java/FIleSystemService.java to src folder in Client and Server 
		- implement the real function for each command
		- build in eclipse by exporting project to runnable JAR
		- run in the command line
			``` java -jar Server.jar
					java -jar Client.jar

###2. Note
```
	sudo kill $(sudo lsof -t -i:9090)
