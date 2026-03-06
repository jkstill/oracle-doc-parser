---
id: 19c__DBMS_PROPAGATION_ADM.STOP_PROPAGATION
name: DBMS_PROPAGATION_ADM.STOP_PROPAGATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROPAGATION_ADM
tags: [dbms_propagation_adm]
source_file: DBMS_PROPAGATION_ADM.html
---

# DBMS_PROPAGATION_ADM.STOP_PROPAGATION

This procedure stops a propagation.

## Syntax

```sql
DBMS_PROPAGATION_ADM.STOP_PROPAGATION(
   propagation_name  IN  VARCHAR2,
   force             IN  BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| propagation_name | VARCHAR2 | IN | The name of the propagation you are stopping. You must specify an existing propagation name. Do not specify an owner. |
| force | BOOLEAN | IN | If TRUE , then the procedure stops the propagation and clears the statistics for the propagation. If FALSE , then the procedure stops the propagation without clearing the statistics for the propagation. |

## Usage Notes

Syntax DBMS_PROPAGATION_ADM.STOP_PROPAGATION( propagation_name IN VARCHAR2, force IN BOOLEAN DEFAULT FALSE); Parameter Table 134-6 STOP_PROPAGATION Procedure Parameter Parameter Description propagation_name The name of the propagation you are stopping. You must specify an existing propagation name. Do not specify an owner. force If TRUE , then the procedure stops the propagation and clears the statistics for the propagation. If FALSE , then the procedure stops the propagation without clearing the statistics for the propagation. Usage Notes The propagation status is persistently recorded. Hence, if the status is DISABLED or ABORTED , then the propagation is not started upon database instance startup.