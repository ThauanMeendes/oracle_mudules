#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importando os modulos
def module():
    module_oracle = {
    "short_description": "Manage users/schemas in Oracle database",
    "description": "Manage users/schemas in an Oracle database | Can be run locally on the controlmachine or on a remote host"
    "version_adde": "1.9.1"
    }

module_oracle_hostname = {
    "description": "The Oracle database host",
    "required": False,
    "default": "localhost"
}

module_oracle_port = {
    "description": "The listener port number on the host",
    "required": False,
    "default", 1521
}

module_oracle_service_name = {
    "description": "The database service name to connect to",
    "required": True
}

module_oracle_user = {
    "description": "The Oracle user name to connect to the database",
    "required": False
}

module_oracle_password = {
    "description": "The Oracle user password for 'user'",
    "required": False
}

module_oracle_mode = {
    "description": "The mode with which to connect to the database",
    "required": False,
    "default": "normal",
    "choices": ['normal','sysdba'] # Verificar essa entrada
}

module_oracle_schema = {
    "description": "The schema that you want to manage",
    "required": False,
    "default": "None" # Ou "defaul": None
}

module_oracle_schema_password = {
    "description": "The password for the new schema. i.e '..identified by password'",
    "required": False,
    "default": "null"
}

module_oracle_schema_password_hash = {
    "description": "The password hash for the new schema. i.e '..identified by values 'XXXXXXX'",
    "required": False,
    "default": None
}

module_oracle_default_tablespace = {
    "description": "The default tablespace for the new schema. The tablespace must exist",
    "required": False,
    "default": None
}

module_oracle_default_temp_tablespace = {
    "description": "The default tablespace for the new schema. The tablespace must exist",
    "required": False,
    "default": None
}

module_oracle_update_password = {
    "description": "always will update passwords if they differ. on_create will only set the password for newly created users.",
    "required": False,
    "default": "always",
    "choices": ['always','on_create']
}

module_oracle_authentication_type = {
    "description": "",
    "required": False,
    "default": "password",
    "choices": ['password','external','global']
}

module_oracle_profile = {
    "description": "The profile for the user",
    "required": False,
    "default": None
}

module_oracle_grants = {
    "description": "The privileges granted to the new schema",
    "required": False,
    "default": None
}

module_oracle_state = {
    "description": "Whether the user should exist. Absent removes the user, locked/inlocked locks or unlocks the user"
    "required": False,
    "default": "present"
    "choices": ['present','absent','locked','unlock']
}

module_oracle_notes = {
    "description": "cx_Oracle need to be installed",
    "requirements": "cx_Oracle",
    "author": "Thauan Mendes Garcia"
}

modulo_oracle_connect = {
    "user": "",
    "passwd": "",
    "host": "",
    "port": "",
    "service": ""
}
