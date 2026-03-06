---
id: 19c__DBMS_XSTREAM_AUTH.REVOKE_REMOTE_ADMIN_ACCESS
name: DBMS_XSTREAM_AUTH.REVOKE_REMOTE_ADMIN_ACCESS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_AUTH
tags: [dbms_xstream_auth]
source_file: DBMS_XSTREAM_AUTH.html
---

# DBMS_XSTREAM_AUTH.REVOKE_REMOTE_ADMIN_ACCESS

This procedure disables a remote XStream administrator from performing administrative actions by connecting to the grantee using a database link.

## Syntax

```sql
DBMS_XSTREAM_AUTH.REVOKE_REMOTE_ADMIN_ACCESS(
   grantee  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| grantee | VARCHAR2) | IN | The user for whom access from a remote XStream administrator is disabled. If a row for the grantee exists in the DBA_XSTREAM_ADMINISTRATOR data dictionary view, then the procedure updates the ACCESS_FROM_REMOTE column for the grantee to NO . If, after this update, both the LOCAL_PRIVILEGES column and the ACCESS_FROM_REMOTE column are NO for the grantee, then the procedure removes the grantee from the view. If no row for the grantee exists in the DBA_XSTREAM_ADMINISTRATOR data dictionary view, then the procedure does not update the view and does not raise an error. |

## Usage Notes

Note: The REVOKE_ADMIN_PRIVILEGE procedure in this package runs this procedure. See Also: " REVOKE_ADMIN_PRIVILEGE Procedure " Note: The REVOKE_ADMIN_PRIVILEGE procedure in this package runs this procedure. See Also: " REVOKE_ADMIN_PRIVILEGE Procedure " Syntax DBMS_XSTREAM_AUTH.REVOKE_REMOTE_ADMIN_ACCESS( grantee IN VARCHAR2); Parameters Table 218-5 REVOKE_REMOTE_ADMIN_ACCESS Procedure Parameter Parameter Description grantee The user for whom access from a remote XStream administrator is disabled. If a row for the grantee exists in the DBA_XSTREAM_ADMINISTRATOR data dictionary view, then the procedure updates the ACCESS_FROM_REMOTE column for the grantee to NO . If, after this update, both the LOCAL_PRIVILEGES column and the ACCESS_FROM_REMOTE column are NO for the grantee, then the procedure removes the grantee from the view. If no row for the grantee exists in the DBA_XSTREAM_ADMINISTRATOR data dictionary view, then the procedure does not update the view and does not raise an error.