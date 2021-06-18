import ldap

l = ldap.initialize ('ldap://il-hq-dc01.allot.local')
username = "CN=pytest,CN=Users,DC=ALLOT,DC=LOCAL"
password = "p@ssw0rd"
try:	
	l.protocol_version = ldap.VERSION3
	l.simple_bind_s(username,password)
	valid=true
except Exception, error:
	print error
