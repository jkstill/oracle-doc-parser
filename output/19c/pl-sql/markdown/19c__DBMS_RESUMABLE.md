---
id: 19c__DBMS_RESUMABLE
name: DBMS_RESUMABLE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESUMABLE
tags: [dbms_resumable]
source_file: DBMS_RESUMABLE.html
---

# DBMS_RESUMABLE

When you suspend a statement, you should log the suspension in the alert log. You should also register a procedure to be executed when the statement is suspended. Using a view, you can monitor the progress of the statement and indicate whether the statement is currently executing or suspended.

## Usage Notes

Suspending a statement automatically results in suspending the transaction. Thus all transactional resources are held during a statement suspend and resume. When the error condition disappears, the suspended statement automatically resumes execution. A resumable space allocation can be suspended and resumed multiple times during execution. A suspension timeout interval is associated with resumable space allocations. A resumable space allocation that is suspended for the timeout interval (the default is two hours) wakes up and returns an exception to the user. A suspended statement may be forced to throw an exception using the DBMS_RESUMABLE.ABORT() procedure.