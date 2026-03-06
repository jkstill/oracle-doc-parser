---
id: 19c__DBMS_ALERT.REMOVEALL
name: DBMS_ALERT.REMOVEALL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ALERT
tags: [dbms_alert]
source_file: DBMS_ALERT.html
---

# DBMS_ALERT.REMOVEALL

This procedure removes all alerts for this session from the registration list. You should do this when the session is no longer interested in any alerts.

## Syntax

```sql
DBMS_ALERT.REMOVEALL;
```

## Usage Notes

This procedure is called automatically upon first reference to this package during a session. Therefore, no alerts from prior sessions which may have terminated abnormally can affect this session. This procedure always performs a commit. Syntax DBMS_ALERT.REMOVEALL;