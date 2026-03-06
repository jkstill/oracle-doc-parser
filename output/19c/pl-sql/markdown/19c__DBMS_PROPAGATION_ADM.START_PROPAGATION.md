---
id: 19c__DBMS_PROPAGATION_ADM.START_PROPAGATION
name: DBMS_PROPAGATION_ADM.START_PROPAGATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PROPAGATION_ADM
tags: [dbms_propagation_adm]
source_file: DBMS_PROPAGATION_ADM.html
---

# DBMS_PROPAGATION_ADM.START_PROPAGATION

This procedure starts a propagation.

## Syntax

```sql
DBMS_PROPAGATION_ADM.START_PROPAGATION(
   propagation_name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| propagation_name | VARCHAR2) | IN | The name of the propagation you are starting. You must specify an existing propagation name. Do not specify an owner. |

## Usage Notes

Syntax DBMS_PROPAGATION_ADM.START_PROPAGATION( propagation_name IN VARCHAR2); Parameter Table 134-5 START_PROPAGATION Procedure Parameter Parameter Description propagation_name The name of the propagation you are starting. You must specify an existing propagation name. Do not specify an owner. Usage Notes The propagation status is persistently recorded. Hence, if the status is ENABLED , then the propagation is started upon database instance startup.