#!/usr/bin/python

#  ansible-oracle-modules
# Módulos Oracle para Ansible
# Para usá-los, crie um diretório 'library' próximo aos seus playbooks de nível superior e coloque os diferentes módulos nesse diretório. Em seguida, basta referenciá-los como faria com qualquer outro módulo.
# Para mais informações, confira: http://docs.ansible.com/developing_modules.html
# Estes são os diferentes módulos:
# <b> oracle_user </ b>
#  - Este módulo pode criar e soltar um usuário.
# - pre-req: cx_Oracle

try:
	import cx_Oracle
except ImportError:
	cx_oracle_exists = False
else:
	cx_oracle_exists = True
	sql = 'select count(*) from dba_users where username = upper(\''+schema+'\')'
	
	try:
		cursor.execute(sql)
		result = cursor.fetchall()[0][0]
	except cx_Oracle.DatabaseError, exc:
			error, = exc.args
			msg[0] = error.message+ 'sql: ' + sql
			return False
 def check_user_exists (msg, cursor, schema):
			
	if result > 0:
		msg[0] = 'The schema '+schema+' already exists'
		return True
 def create_user (msg, cursor, schema, schema_password, default_tablespace, grants):
	sql = 'create user '+schema+' identified by '+schema_password+' '
	if (default_tablespace):
		sql += 'default tablespace '+default_tablespace+' ' 
		sql += 'quota unlimited on '+default_tablespace 
	
 	
	try:
		cursor.execute(sql)
	except cx_Oracle.DatabaseError, exc:
		error, = exc.args
		msg[0] = 'Blergh, something went wrong while creating the schema - ' + error.message +'sql: '+ sql
		return False
 	# Add grants to user if explicitly set. If not, only 'create session' is granted
	if (grants):
		sql = 'grant '+grants+ ' to '+schema
	else:
		sql = 'grant create session to '+schema
 	try:
		cursor.execute(sql)
	except cx_Oracle.DatabaseError, exc:
		error, = exc.args
		mess[0] = 'Blergh, something went wrong while adding grants to the schema - ' + error.message +'sql: '+ sql
		return False
 	return True
	
 def drop_user (msg, cursor, schema):
	#black_list = ['sys','system']
 	#	msg[0] = 'Trying to drop an internal user. Not allowed'
	#	return False
 	sql = 'drop user '+schema+' cascade'
 	try:
		cursor.execute(sql)
	except cx_Oracle.DatabaseError, exc:
		error, = exc.args
		msg[0] = 'Blergh, something went wrong while dropping the schema - ' + error.message +'sql: '+ sql
		return False
 	return True
 def main():
 	msg = ['']
	module = AnsibleModule(
		argument_spec = dict(
			hostname      = dict(default='localhost'),
			port          = dict(default=1521),
			service_name  = dict(required=True),
			user          = dict(required=True),
			password      = dict(required=True),
			schema        = dict(required=True),
			schema_password  = dict(required=True),
			state         = dict(sdefault="present", choices=["present", "absent"]),
			default_tablespace = dict(default=None),
			grants         = dict(default=None)
		)
	)

 	hostname = module.params["hostname"]
	port = module.params["port"]
	service_name = module.params["service_name"]
	user = module.params["user"]
	password = module.params["password"]
	schema = module.params["schema"]
	schema_password = module.params["schema_password"]
	state = module.params["state"]
	default_tablespace = module.params["default_tablespace"]
	grants = module.params["grants"]
 	if not cx_oracle_exists:
		module.fail_json(msg="The cx_Oracle module is required. 'pip install cx_Oracle' should do the trick")
 	dsn = cx_Oracle.makedsn(host=hostname,port=port,service_name=service_name)
	try:
		conn = cx_Oracle.connect(user,password,dsn)
	except cx_Oracle.DatabaseError, exc:
		error, = exc.args
		msg[0] = 'Could not connect to database - ' + error.message
		module.fail_json(msg=msg[0], changed=False)
 	cursor = conn.cursor()
 	if state == 'present':
		if not check_user_exists(msg, cursor, schema):
			if create_user(msg, cursor, schema, schema_password, default_tablespace, grants):
				msg[0] = 'The schema '+schema+' has been created successfully'
				module.exit_json(msg=msg[0], changed=True)
			else:
				module.fail_json(msg=msg[0], changed=False)
	
 	elif state == 'absent':
		if check_user_exists(msg, cursor, schema):
			if drop_user(msg, cursor, schema):
				msg[0] = 'The schema '+schema+' dropped successfully'
				module.exit_json(msg=msg[0], changed=True)
		else:
			module.exit_json(msg='The schema '+schema+ ' doesn\'t exist', changed=False)				
	
	module.exit_json(msg=msg[0], changed=False)

from ansible.module_utils.basic import *
if __name__ == '__main__':
	main()
