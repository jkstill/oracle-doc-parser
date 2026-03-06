---
id: 19c__DBMS_LOGSTDBY.UNSKIP
name: DBMS_LOGSTDBY.UNSKIP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.UNSKIP

Use the UNSKIP procedure to delete rules specified earlier with the SKIP procedure.

## Syntax

```sql
DBMS_LOGSTDBY.UNSKIP (
     stmt                      IN VARCHAR2,
     schema_name               IN VARCHAR2 DEFAULT NULL,
     object_name               IN VARCHAR2 DEFUALT NULL,
     container_name            IN VARCHAR2 DEFAULT NULL);
```

## Usage Notes

The parameters specified in the UNSKIP procedure must match exactly for it to delete an already-specified rule. The container_name argument is valid only in a CDB. Syntax DBMS_LOGSTDBY.UNSKIP ( stmt IN VARCHAR2, schema_name IN VARCHAR2 DEFAULT NULL, object_name IN VARCHAR2 DEFUALT NULL, container_name IN VARCHAR2 DEFAULT NULL); Parameters The parameter information for the UNSKIP procedure is the same as that described for the SKIP procedure. See Table 102-14 for complete parameter information. Exceptions Table 102-21 UNSKIP Procedure Exceptions Exception Description ORA-01031 need DBA privileges to execute this procedure ORA-16103 Logical Standby apply must be stopped to allow this operation ORA-16104 invalid Logical Standby option requested Usage Notes WARNING: If DML changes for a table have been skipped and not compensated for, you must follow the call to the UNSKIP procedure with a call to the INSTANTIATE_TABLE procedure to synchronize this table with those maintained by SQL Apply. This procedure requires DBA privileges to execute. Wildcards passed in the schema_name or the object_name parameter are not expanded. The wildcard character is matched at the character level. Thus, you can delete only one specified rule by invoking the UNSKIP procedure, and you will need a distinct UNSKIP procedure call to delete each rule that was previously specified. For example, assume you have specified the following two rules to skip applying DML statements to the HR.EMPLOYEE and HR.EMPTEMP tables: SQL> EXECUTE DBMS_LOGSTDBY.SKIP (STMT => 'DML',- SCHEMA_NAME => 'HR', - OBJECT_NAME => 'EMPLOYEE', - PROC_NAME => null); SQL> EXECUTE DBMS_LOGSTDBY.SKIP (STMT => 'DML',- SCHEMA_NAME => 'HR', - OBJECT_NAME => 'EMPTEMP', - PROC_NAME => null); In the following example, the wildcard in the TABLE_NAME parameter cannot be used to delete the rules that were specified: SQL> EXECUTE DBMS_LOGSTDBY.UNSKIP (STMT => 'DML',- SCHEMA_NAME => 'HR', - OBJECT_NAME => 'EMP%'); In fact, this UNSKIP procedure matches neither of the rules, because the wildcard character in the TABLE_NAME parameter is not expanded. Instead, the wildcard character will be used in an exact match to find the corresponding SKIP rule.