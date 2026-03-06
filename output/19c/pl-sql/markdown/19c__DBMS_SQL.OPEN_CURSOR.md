---
id: 19c__DBMS_SQL.OPEN_CURSOR
name: DBMS_SQL.OPEN_CURSOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL
tags: [dbms_sql]
source_file: DBMS_SQL.html
---

# DBMS_SQL.OPEN_CURSOR

This function opens a new cursor.

## Syntax

```sql
DBMS_SQL.OPEN_CURSOR (
   treat_as_client_for_results    IN     BOOLEAN    DEFAULT FALSE) 
  RETURN INTEGER;

DBMS_SQL.OPEN_CURSOR (
   security_level                 IN     INTEGER,
   treat_as_client_for_results    IN     BOOLEAN    DEFAULT FALSE) 
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| security_level | INTEGER | IN | Specifies the level of security protection to enforce on the opened cursor. Valid security level values are 0 , 1 , and 2 . When a NULL argument value is provided to this overload, as well as for cursors opened using the overload of open_cursor without the security_level parameter, the default security level value 1 will be enforced on the opened cursor. Level 0 - allows all DBMS_SQL operations on the cursor without any security checks. The cursor may be fetched from, and even re-bound and re-executed, by code running with a different effective userid or roles than those in effect at the time the cursor was parsed. This level of security is off by default. Level 1 - requires that the referenced container, effective userid, and roles of the caller to DBMS_SQL for bind and execute operations on this cursor must be the same as those of the caller of the most recent parse operation on this cursor. Level 2 - requires that the referenced container, effective userid, and roles of the caller to DBMS_SQL for all bind, execute, define, describe, and fetch operations on this cursor must be the same as those of the caller of the most recent parse operation on this cursor. |
| treat_as_client_for results |  |  | Allows the caller of the recursive statement to set itself as the client to receive the statement results returned from the recursive statement to client. The statement results returned may be retrieved by the GET_NEXT_RESULT Procedures . |

**Returns:** `INTEGER`

## Usage Notes

The security_level parameter allows for application of fine-grained control to the security of the opened cursor. Syntax DBMS_SQL.OPEN_CURSOR ( treat_as_client_for_results IN BOOLEAN DEFAULT FALSE) RETURN INTEGER; DBMS_SQL.OPEN_CURSOR ( security_level IN INTEGER, treat_as_client_for_results IN BOOLEAN DEFAULT FALSE) RETURN INTEGER; Parameters Table 162-28 OPEN_CURSOR Function Parameters Parameter Description security_level Specifies the level of security protection to enforce on the opened cursor. Valid security level values are 0 , 1 , and 2 . When a NULL argument value is provided to this overload, as well as for cursors opened using the overload of open_cursor without the security_level parameter, the default security level value 1 will be enforced on the opened cursor. Level 0 - allows all DBMS_SQL operations on the cursor without any security checks. The cursor may be fetched from, and even re-bound and re-executed, by code running with a different effective userid or roles than those in effect at the time the cursor was parsed. This level of security is off by default. Level 1 - requires that the referenced container, effective userid, and roles of the caller to DBMS_SQL for bind and execute operations on this cursor must be the same as those of the caller of the most recent parse operation on this cursor. Level 2 - requires that the referenced container, effective userid, and roles of the caller to DBMS_SQL for all bind, execute, define, describe, and fetch operations on this cursor must be the same as those of the caller of the most recent parse operation on this cursor. treat_as_client_for results Allows the caller of the recursive statement to set itself as the client to receive the statement results returned from the recursive statement to client. The statement results returned may be retrieved by the GET_NEXT_RESULT Procedures . Pragmas pragma restrict_references(open_cursor,RNDS,WNDS); Return Values Returns the cursor ID number of the new cursor