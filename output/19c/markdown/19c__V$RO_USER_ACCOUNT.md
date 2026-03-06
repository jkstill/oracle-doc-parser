---
id: 19c__V$RO_USER_ACCOUNT
name: V$RO_USER_ACCOUNT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dynamic_performance]
source_file: V-RO_USER_ACCOUNT.html
---

# V$RO_USER_ACCOUNT

In an Oracle Data Guard environment, some of the security information for user accounts on the standby is inherited from the primary server. For example, if the account is locked out unlimited on the primary, then it will be locked on the standby database(s). The information stored on the standby is volatile information that user actions on the standby database(s) can affect, such as the number of failed logins, and the time the account was locked on the standby due to failed access attempts. Note that failed login attempts on standbys do not affect the account status on primaries.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERID | NUMBER |  |
| PASSW_EXPIRED | NUMBER |  |
| PASSW_IN_GRACE | NUMBER |  |
| PASSW_LOCKED | NUMBER |  |
| PASSW_LOCK_UNLIM | NUMBER |  |
| FAILED_LOGINS | NUMBER |  |
| EXPIRATION_AFTER_GRACE | TIMESTAMP(3) |  |
| PASSW_LOCK_TIME | TIMESTAMP(3) |  |
| CON_ID | NUMBER |  |
| USERNAME | VARCHAR2(128) |  |

## Usage Notes

In an Oracle Data Guard environment, some of the security information for user accounts on the standby is inherited from the primary server. For example, if the account is locked out unlimited on the primary, then it will be locked on the standby database(s). The information stored on the standby is volatile information that user actions on the standby database(s) can affect, such as the number of failed logins, and the time the account was locked on the standby due to failed access attempts. Note that failed login attempts on standbys do not affect the account status on primaries. If this view is queried from the root in a multitenent container database (CDB), then only common users and the SYS user are returned. If this view is queried from a pluggable database (PDB), only rows that pertain to the current PDB are returned.