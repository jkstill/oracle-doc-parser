---
id: 19c__DBMS_XSTREAM_AUTH.GRANT_REMOTE_ADMIN_ACCESS
name: DBMS_XSTREAM_AUTH.GRANT_REMOTE_ADMIN_ACCESS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_AUTH
tags: [dbms_xstream_auth]
source_file: DBMS_XSTREAM_AUTH.html
---

# DBMS_XSTREAM_AUTH.GRANT_REMOTE_ADMIN_ACCESS

This procedure enables a remote XStream administrator to perform administrative actions at the local database by connecting to the grantee using a database link.

## Syntax

```sql
DBMS_XSTREAM_AUTH.GRANT_REMOTE_ADMIN_ACCESS(
   grantee  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| grantee | VARCHAR2) | IN | The user who allows remote access. The procedure adds the grantee to the DBA_XSTREAM_ADMINISTRATOR data dictionary view with YES for the ACCESS_FROM_REMOTE column. If the user already has an entry in this data dictionary view, then the procedure does not make another entry. Instead, it updates the ACCESS_FROM_REMOTE column to YES . |

## Usage Notes

Syntax DBMS_XSTREAM_AUTH.GRANT_REMOTE_ADMIN_ACCESS( grantee IN VARCHAR2); Parameters Table 218-3 GRANT_REMOTE_ADMIN_ACCESS Procedure Parameter Parameter Description grantee The user who allows remote access. The procedure adds the grantee to the DBA_XSTREAM_ADMINISTRATOR data dictionary view with YES for the ACCESS_FROM_REMOTE column. If the user already has an entry in this data dictionary view, then the procedure does not make another entry. Instead, it updates the ACCESS_FROM_REMOTE column to YES . Usage Notes Typically, you run the procedure and specify a grantee at a local source database if a downstream capture process captures changes originating at the local source database. The XStream administrator at a downstream capture database administers the source database using this connection. Note: The GRANT_ADMIN_PRIVILEGE procedure in this package runs this procedure. See Also: " GRANT_ADMIN_PRIVILEGE Procedure " Note: The GRANT_ADMIN_PRIVILEGE procedure in this package runs this procedure. See Also: " GRANT_ADMIN_PRIVILEGE Procedure "