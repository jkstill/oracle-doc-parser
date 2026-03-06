---
id: 19c__DBMS_LIBCACHE.COMPILE_FROM_REMOTE
name: DBMS_LIBCACHE.COMPILE_FROM_REMOTE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LIBCACHE
tags: [dbms_libcache]
source_file: DBMS_LIBCACHE.html
---

# DBMS_LIBCACHE.COMPILE_FROM_REMOTE

This procedure extracts SQL in batch from the source instance and compiles the SQL at the target instance.

## Syntax

```sql
DBMS_LIBCACHE.COMPILE_FROM_REMOTE ( 
   p_db_link                 IN     dbms_libcache$def.db_link%type, 
   p_username                IN     VARCHAR2 default null,
   p_threshold_executions    IN     NATURAL  default 3,
   p_threshold_sharable_mem  IN     NATURAL  default 1000,
   p_parallel_degree         IN     NATURAL  default 1);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| p_db_link | dbms_libcache$def.db_link%type | IN | Database link to the source name (mandatory). The database link pointing to the instance that will be used for extracting the SQL statements. The user must have the role SELECT_ON_CATALOG at the source instance. For improved security, the connection may use a password file or LDAP authentication. The database link is mandatory only for releases with dbms_libcache$def.ACCESS_METHOD = DB_LINK_METHOD |
| p_instance_name |  |  | (Reserved for future use). The name of the instance that will be used for extracting the SQL statements. The instance name must be unique for all instances excluding the local instance. The name is not case sensitive. |
| p_username | VARCHAR2 | IN | Source username (default is all users). The name of the username that will be used for extracting the SQL statements. The username is an optional parameter that is used to ensure the parsing user id is the same as that on the source instance. For an application where users connect as a single user_id , for example APPS , APPS is the parsing user_id that is recorded in the shared pool. To select only SQL statements parsed by APPS , enter the string 'APPS' in this field. To also select statements executed by batch, repeat the executing the procedure with the schema owner, for example GL. If the username is supplied, it must be valid. The name is not case sensitive. |
| p_threshold_executions | NATURAL | IN | The lower bound for the number of executions, below which a SQL statement will not be selected for parsing. This parameter is optional. It allows the application to extract and compile statements with executions, for example, greater than 3. The default value is 1. This means SQL statements that have never executed, including invalid SQL statements, will not be extracted. |
| p_threshold_sharable_mem | NATURAL | IN | The lower bound for the size of the shared memory consumed by the cursors on the source instance. Below this value a SQL statement will not be selected for parsing. This parameter is optional. It allows the application to extract and compile statements with shared memory for example, greater than 10000 bytes. |
| p_parallel_degree | NATURAL | IN | The number of parallel jobs that execute to complete the parse operation. These tasks are spawned as parallel jobs against a sub-range of the SQL statements selected for parsing. This parameter is reserved for parallel compile jobs which are currently not implemented. |

## Usage Notes

Syntax DBMS_LIBCACHE.COMPILE_FROM_REMOTE ( p_db_link IN dbms_libcache$def.db_link%type, p_username IN VARCHAR2 default null, p_threshold_executions IN NATURAL default 3, p_threshold_sharable_mem IN NATURAL default 1000, p_parallel_degree IN NATURAL default 1); Parameters Table 98-2 COMPILE_FROM_REMOTE Procedure Parameters Parameter Description p_db_link Database link to the source name (mandatory). The database link pointing to the instance that will be used for extracting the SQL statements. The user must have the role SELECT_ON_CATALOG at the source instance. For improved security, the connection may use a password file or LDAP authentication. The database link is mandatory only for releases with dbms_libcache$def.ACCESS_METHOD = DB_LINK_METHOD p_instance_name (Reserved for future use). The name of the instance that will be used for extracting the SQL statements. The instance name must be unique for all instances excluding the local instance. The name is not case sensitive. p_username Source username (default is all users). The name of the username that will be used for extracting the SQL statements. The username is an optional parameter that is used to ensure the parsing user id is the same as that on the source instance. For an application where users connect as a single user_id , for example APPS , APPS is the parsing user_id that is recorded in the shared pool. To select only SQL statements parsed by APPS , enter the string 'APPS' in this field. To also select statements executed by batch, repeat the executing the procedure with the schema owner, for example GL. If the username is supplied, it must be valid. The name is not case sensitive. p_threshold_executions The lower bound for the number of executions, below which a SQL statement will not be selected for parsing. This parameter is optional. It allows the application to extract and compile statements with executions, for example, greater than 3. The default value is 1. This means SQL statements that have never executed, including invalid SQL statements, will not be extracted. p_threshold_sharable_mem The lower bound for the size of the shared memory consumed by the cursors on the source instance. Below this value a SQL statement will not be selected for parsing. This parameter is optional. It allows the application to extract and compile statements with shared memory for example, greater than 10000 bytes. p_parallel_degree The number of parallel jobs that execute to complete the parse operation. These tasks are spawned as parallel jobs against a sub-range of the SQL statements selected for parsing. This parameter is reserved for parallel compile jobs which are currently not implemented.