---
id: 19c__DBMS_APP_CONT.GET_LTXID_OUTCOME
name: DBMS_APP_CONT.GET_LTXID_OUTCOME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APP_CONT
tags: [dbms_app_cont]
source_file: DBMS_APP_CONT.html
---

# DBMS_APP_CONT.GET_LTXID_OUTCOME

This procedure lets customer applications and third party application servers determine the transactional status of the last session when that session becomes unavailable.

## Syntax

```sql
DBMS_APP_CONT.GET_LTXID_OUTCOME (
 client_ltxid          IN    RAW, 
 committed             OUT   BOOLEAN, 
 user_call_completed   OUT   BOOLEAN)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_ltxid | RAW | IN | Client-side logical transaction ID. Obtain the LTXID from the previous failed session using the client driver provided APIs - getLTXID for JDBC, and LogicalTransactionId for ODP . net ., and OCI_ATTR_GET with LTXID for OCI. |
| committed | BOOLEAN | OUT | Returns TRUE if the transaction with the named logical LTXID has COMMITTED . Returns FALSE if the logical LTXID has not COMMITTED . When returning FALSE , the procedure blocks the LTXID from further use so that there is no possibility of previous in-flight work committing this LTXID . |
| user_call_completed | BOOLEAN) | OUT | Whether all information has been returned to the client. Examples of such messages are the number of rows processed when using autocommit or commit on success, parameter and function results when calling PL/SQL, or PL/SQL with more work to do after the COMMIT . Applications that expect to use data returned from the commit in order to function correctly must look at this second parameter. |

## Usage Notes

Syntax DBMS_APP_CONT.GET_LTXID_OUTCOME ( client_ltxid IN RAW, committed OUT BOOLEAN, user_call_completed OUT BOOLEAN) Parameters Table 18-6 GET_LTXID_OUTCOME Procedure Parameters Parameter Description client_ltxid Client-side logical transaction ID. Obtain the LTXID from the previous failed session using the client driver provided APIs - getLTXID for JDBC, and LogicalTransactionId for ODP . net ., and OCI_ATTR_GET with LTXID for OCI. committed Returns TRUE if the transaction with the named logical LTXID has COMMITTED . Returns FALSE if the logical LTXID has not COMMITTED . When returning FALSE , the procedure blocks the LTXID from further use so that there is no possibility of previous in-flight work committing this LTXID . user_call_completed Whether all information has been returned to the client. Examples of such messages are the number of rows processed when using autocommit or commit on success, parameter and function results when calling PL/SQL, or PL/SQL with more work to do after the COMMIT . Applications that expect to use data returned from the commit in order to function correctly must look at this second parameter. Exceptions Table 18-7 GET_LTXID_OUTCOME Procedure Exceptions Exception Description ORA-14950 - SERVER_AHEAD The server is ahead so the transaction is both an old transaction and one which has already committed. This is an error as the application is passing an older LTXID that is the not the last used for that session. The purpose of GET_LTXID_OUTCOME is to return the current transaction outcome for that session after a recoverable outage. ORA-14951 - CLIENT_AHEAD The client is ahead of the server. This can happen if the server has been flashed backed, recovered using media recovery, or is a standby that has opened earlier with data loss. ORA-14906 - SAME_SESSION Executing GET_LTXID_OUTCOME is not supported on the session owning the LTXID as it blocks further processing on that session after a recoverable outage. ORA-14909 - COMMIT_BLOCKED Your session has been blocked from committing by another user with the same username using GET_LTXID_OUTCOME . GET_LTXID_OUTCOME should only be called on dead sessions. Please check with your application administrator. ORA-14952 - ERROR The outcome cannot be determined. During processing an error happened. The error stack shows the error detail.