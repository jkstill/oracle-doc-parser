---
id: 19c__DBMS_XDB_CONFIG.ADDHTTPEXPIREMAPPING
name: DBMS_XDB_CONFIG.ADDHTTPEXPIREMAPPING
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ADDHTTPEXPIREMAPPING

This procedure adds to XDB$CONFIG a mapping of the URL pattern to an expiration date. This will control the Expire headers for URLs matching the pattern.

## Syntax

```sql
DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING (
     pattern    IN    VARCHAR2,
     expire     IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pattern | VARCHAR2 | IN | URL pattern (only * accepted as wildcards) |
| expire | VARCHAR2) | IN | Expiration directive, follows the ExpireDefault in Apache's mod_expires : base [plus] (num type)* -- base: now | modification -- type: year|years|month|months|week|weeks|day|days| minute|minutess|second|seconds |

## Usage Notes

Syntax DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING ( pattern IN VARCHAR2, expire IN VARCHAR2); Parameters Table 196-3 ADDHTTPEXPIREMAPPING Procedure Parameters Parameter Description pattern URL pattern (only * accepted as wildcards) expire Expiration directive, follows the ExpireDefault in Apache's mod_expires : base [plus] (num type)* -- base: now | modification -- type: year|years|month|months|week|weeks|day|days| minute|minutess|second|seconds Examples DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING ('/public/test1/*', 'now plus 4 weeks'); DBMS_XDB_REPOS.ADDHTTPEXPIREMAPPING ( '/public/test2/*', 'modification plus 1 day 30 seconds');