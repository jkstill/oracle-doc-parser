---
id: 19c__DBMS_LOGSTDBY.APPLY_UNSET
name: DBMS_LOGSTDBY.APPLY_UNSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOGSTDBY
tags: [dbms_logstdby]
source_file: DBMS_LOGSTDBY.html
---

# DBMS_LOGSTDBY.APPLY_UNSET

Use the APPLY_UNSET procedure to restore the default values of the parameters that you changed with the APPLY_SET procedure.

## Syntax

```sql
DBMS_LOGSTDBY.APPLY_UNSET (
     inname          IN VARCHAR);
```

## Usage Notes

In a CDB, the APPLY_UNSET procedure must be called from the root database. Syntax DBMS_LOGSTDBY.APPLY_UNSET ( inname IN VARCHAR); Parameters The parameter information for the APPLY_UNSET procedure is the same as that described for the APPLY_SET procedure. See Table 102-3 for complete parameter information. Exceptions Table 102-5 APPLY_UNSET Procedure Exceptions Exception Description ORA-16103 Logical Standby apply must be stopped to allow this operation ORA-16104 invalid Logical Standby option requested ORA-16236 Logical Standby metadata operation in progress Usage Notes Use the APPLY_SET procedure to specify a nondefault value for a parameter.