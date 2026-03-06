---
id: 19c__DBMS_DATAPUMP.LOG_ENTRY
name: DBMS_DATAPUMP.LOG_ENTRY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_DATAPUMP
tags: [dbms_datapump]
source_file: DBMS_DATAPUMP.html
---

# DBMS_DATAPUMP.LOG_ENTRY

This procedure inserts a message into the log file.

## Syntax

```sql
DBMS_DATAPUMP.LOG_ENTRY(
   handle         IN NUMBER,
   message        IN VARCHAR2
   log_file_only  IN NUMBER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| handle | NUMBER | IN | The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. |
| message | VARCHAR2 | IN | A text line to be added to the log file |
| log_file_only | NUMBER | IN | Specified text should be written only to the log file. It should not be returned in GET_STATUS work-in-progress ( KU$_STATUS_WIP ) messages. |

## Usage Notes

Syntax DBMS_DATAPUMP.LOG_ENTRY( handle IN NUMBER, message IN VARCHAR2 log_file_only IN NUMBER DEFAULT 0); Parameters Table 49-13 LOG_ENTRY Procedure Parameters Parameter Description handle The handle of a job. The current session must have previously attached to the handle through a call to either the OPEN or ATTACH function. message A text line to be added to the log file log_file_only Specified text should be written only to the log file. It should not be returned in GET_STATUS work-in-progress ( KU$_STATUS_WIP ) messages. Exceptions INVALID_HANDLE . The specified handle is not attached to a Data Pump job. SUCCESS_WITH_INFO . The procedure succeeded, but further information is available through the GET_STATUS procedure. NO_SUCH_JOB . The specified job does not exist. Usage Notes The message is added to the log file. If log_file_only is zero (the default), the message is also broadcast as a KU$_STATUS_WIP message through the GET_STATUS procedure to all users attached to the job. The LOG_ENTRY procedure allows applications to tailor the log stream to match the abstractions provided by the application. For example, the command-line interface supports INCLUDE and EXCLUDE parameters defined by the user. Identifying these values as calls to the underlying METADATA_FILTER procedure would be confusing to users. Instead, the command-line interface can enter text into the log describing the settings for the INCLUDE and EXCLUDE parameters. Lines entered in the log stream from LOG_ENTRY are prefixed by the string, " ;;; "