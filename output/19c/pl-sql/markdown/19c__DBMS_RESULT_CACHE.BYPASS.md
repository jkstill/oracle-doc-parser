---
id: 19c__DBMS_RESULT_CACHE.BYPASS
name: DBMS_RESULT_CACHE.BYPASS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESULT_CACHE
tags: [dbms_result_cache]
source_file: DBMS_RESULT_CACHE.html
---

# DBMS_RESULT_CACHE.BYPASS

This procedure sets the bypass mode for the Result Cache.

## Syntax

```sql
DBMS_RESULT_CACHE.BYPASS (
   bypass_mode    IN   BOOLEAN,
   session        IN   BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| bypass_mode | BOOLEAN | IN | TRUE => Result Cache usage is bypassed FALSE => Result Cache usage is turned on |
| session | BOOLEAN) | IN | TRUE => Applies to current session FALSE (default) => Applies to all sessions |

## Usage Notes

It sets one of the following bypass modes: When bypass mode is turned on, it implies that cached results are no longer used and that no new results are saved in the cache. When bypass mode is turned off, the cache resumes normal operation. Syntax DBMS_RESULT_CACHE.BYPASS ( bypass_mode IN BOOLEAN, session IN BOOLEAN); Parameters Table 144-6 BYPASS Procedure Parameters Parameter Description bypass_mode TRUE => Result Cache usage is bypassed FALSE => Result Cache usage is turned on session TRUE => Applies to current session FALSE (default) => Applies to all sessions Usage Notes This operation is database instance specific. Examples This operation can be used when there is a need to hot patch PL/SQL code in a running system. If a code-patch is applied to a PL/SQL module on which a result cached function directly or transitively depends, then the cached results associated with the result cache function are not automatically flushed (if the instance is not restarted/bounced). This must be manually achieved. To ensure correctness during the patching process follow these steps: Place the result cache in bypass mode, and flush existing result. BEGIN DBMS_RESULT_CACHE.BYPASS(TRUE); DBMS_RESULT_CACHE.FLUSH; END; / This step must be performed on each instance if in a Oracle Real Application Clusters environment. Apply the PL/SQL code patches. Resume use of the result cache, by turning off the cache bypass mode. BEGIN DBMS_RESULT_CACHE.BYPASS(FALSE); END; / This step must be performed on each instance if in a Oracle Real Application Clusters environment.