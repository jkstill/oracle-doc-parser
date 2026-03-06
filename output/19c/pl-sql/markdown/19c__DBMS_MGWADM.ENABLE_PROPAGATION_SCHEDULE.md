---
id: 19c__DBMS_MGWADM.ENABLE_PROPAGATION_SCHEDULE
name: DBMS_MGWADM.ENABLE_PROPAGATION_SCHEDULE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.ENABLE_PROPAGATION_SCHEDULE

This deprecated procedure enables a propagation schedule.

## Syntax

```sql
DBMS_MGWADM.ENABLE_PROPAGATION_SCHEDULE (
   schedule_id  IN VARCHAR2 );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| schedule_id | VARCHAR2 | IN | Identifies the propagation schedule to be enabled |

## Usage Notes

Note: This subprogram has been deprecated as a result of improved technology (see ENABLE_JOB Procedure ), and is retained only for reasons of backward compatibility. Note: This subprogram has been deprecated as a result of improved technology (see ENABLE_JOB Procedure ), and is retained only for reasons of backward compatibility. Syntax DBMS_MGWADM.ENABLE_PROPAGATION_SCHEDULE ( schedule_id IN VARCHAR2 ); Parameters Table 110-36 ENABLE_PROPAGATION_SCHEDULE Procedure Parameters Parameter Description schedule_id Identifies the propagation schedule to be enabled