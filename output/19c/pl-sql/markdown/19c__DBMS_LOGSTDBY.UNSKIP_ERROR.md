---
id: 19c__DBMS_LOGSTDBY.UNSKIP_ERROR
name: DBMS_LOGSTDBY.UNSKIP_ERROR
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.UNSKIP_ERROR

Use the UNSKIP_ERROR procedure to delete rules specified earlier with the SKIP_ERROR procedure.

## Syntax

```sql
DBMS_LOGSTDBY.UNSKIP_ERROR (
     stmt                      IN VARCHAR2,
     schema_name               IN VARCHAR2 DEFAULT NULL,
     object_name               IN VARCHAR2 DEFAULT NULL,
     container_name            IN VARCHAR2 DEFAULT NULL);
```

## Usage Notes

The parameters specified in the UNSKIP_ERROR procedure must match exactly for the procedure to delete an already-specified rule. The container_name argument is valid only in a CDB. Syntax DBMS_LOGSTDBY.UNSKIP_ERROR ( stmt IN VARCHAR2, schema_name IN VARCHAR2 DEFAULT NULL, object_name IN VARCHAR2 DEFAULT NULL, container_name IN VARCHAR2 DEFAULT NULL); Parameters The parameter information for the UNSKIP_ERROR procedure is the same as that described for the SKIP_ERROR procedure. See Table 102-17 for complete parameter information. Exceptions Table 102-22 UNSKIP_ERROR Procedure Exceptions Exception Description ORA-01031 Need DBA privileges ORA-16103 Logical Standby apply must be stopped to allow this operation ORA-16104 invalid Logical Standby option requested Usage Notes This procedure requires DBA privileges to execute. Wildcards passed in the schema_name or the object_name parameters are not expanded. Instead, the wildcard character is treated as any other character and an exact match is made. Thus, you can delete only one specified rule by invoking the UNSKIP_ERROR procedure, and you need a distinct UNSKIP_ERROR procedure call to delete each rule that you previously specified. For example, assume you have specified the following two rules to handle the HR.EMPLOYEE and HR.EMPTEMP tables: SQL> EXECUTE DBMS_LOGSTDBY.SKIP_ERROR (STMT => 'DML',- SCHEMA_NAME => 'HR', - OBJECT_NAME => 'EMPLOYEE', - PROC_NAME => 'hr_employee_handler'); SQL> EXECUTE DBMS_LOGSTDBY.SKIP_ERROR (STMT => 'DML',- SCHEMA_NAME => 'HR', - OBJECT_NAME => 'EMPTEMP', - PROC_NAME => 'hr_tempemp_handler'); In this case, the following UNSKIP procedure cannot be used to delete the rules that you have specified: SQL> EXECUTE DBMS_LOGSTDBY.UNSKIP_ERROR (STMT => 'DML',- SCHEMA_NAME => 'HR', - OBJECT_NAME => 'EMP%'); In fact, the UNSKIP procedure will match neither of the rules, because the wildcard character in the OBJECT_NAME parameter will not be expanded.