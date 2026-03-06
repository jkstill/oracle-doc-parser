---
id: 19c__DBMS_LOCK
name: DBMS_LOCK
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOCK
tags: [dbms_lock]
source_file: DBMS_LOCK.html
---

# DBMS_LOCK

User locks never conflict with Oracle locks because they are identified with the prefix "UL". You can view these locks using the Enterprise Manager lock monitor screen or the appropriate fixed views.

## Usage Notes

User locks are automatically released when a session terminates. The lock identifier is a number in the range of 0 to 1073741823. Because a reserved user lock is the same as an Oracle lock, it has all the functionality of an Oracle lock, such as deadlock detection. Be certain that any user locks used in distributed transactions are released upon COMMIT , or an undetected deadlock may occur. DBMS_LOCK is most efficient with a limit of a few hundred locks for each session. Oracle strongly recommends that you develop a standard convention for using these locks in order to avoid conflicts among procedures trying to use the same locks. For example, include your company name as part of your lock names.