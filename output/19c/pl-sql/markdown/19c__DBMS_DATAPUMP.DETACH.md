---
id: 19c__DBMS_DATAPUMP.DETACH
name: DBMS_DATAPUMP.DETACH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.DETACH

This procedure specifies that the user has no further interest in using the handle.

## Syntax

```sql
DBMS_DATAPUMP.DETACH(
   handle  IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER) | IN | The handle of the job. The current session must have previously attached to the handle through a call to either an OPEN or ATTACH function. |

## Usage Notes

Syntax DBMS_DATAPUMP.DETACH( handle IN NUMBER); Parameters Table 49-9 DETACH Procedure Parameters Parameter Description handle The handle of the job. The current session must have previously attached to the handle through a call to either an OPEN or ATTACH function. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes Through this call, you specify that you have no further interest in using the handle. Resources associated with a completed job cannot be reclaimed until all users are detached from the job. An implicit detach from a handle is performed when the user's session is exited or aborted. An implicit detach from a handle is also performed upon the expiration of the timeout associated with a STOP_JOB that was applied to the job referenced by the handle. All previously allocated DBMS_DATAPUMP handles are released when an instance is restarted.