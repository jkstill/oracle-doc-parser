---
id: 19c__UTL_FILE.FCLOSE_ALL
name: UTL_FILE.FCLOSE_ALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_FILE
tags: [utl_file]
source_file: UTL_FILE.html
---

# UTL_FILE.FCLOSE_ALL

This procedure closes all open file handles for the session. This should be used as an emergency cleanup procedure, for example, when a PL/SQL program exits on an exception.

## Syntax

```sql
UTL_FILE.FCLOSE_ALL;
```

## Usage Notes

Syntax UTL_FILE.FCLOSE_ALL; Usage Notes Note: FCLOSE_ALL does not alter the state of the open file handles held by the user. This means that an IS_OPEN test on a file handle after an FCLOSE_ALL call still returns TRUE , even though the file has been closed. No further read or write operations can be performed on a file that was open before an FCLOSE_ALL . Note: FCLOSE_ALL does not alter the state of the open file handles held by the user. This means that an IS_OPEN test on a file handle after an FCLOSE_ALL call still returns TRUE , even though the file has been closed. No further read or write operations can be performed on a file that was open before an FCLOSE_ALL . Exceptions WRITE_ERROR