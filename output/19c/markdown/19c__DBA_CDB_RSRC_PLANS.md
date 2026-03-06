---
id: 19c__DBA_CDB_RSRC_PLANS
name: DBA_CDB_RSRC_PLANS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_CDB_RSRC_PLANS.html
---

# DBA_CDB_RSRC_PLANS

DBA_CDB_RSRC_PLANS provides information about all the CDB resource plans.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PLAN_ID | NUMBER | CDB resource plan ID |
| PLAN | VARCHAR2(128) | CDB resource plan name |
| COMMENTS | VARCHAR2(2000) | Text comment on the CDB resource plan |
| STATUS | VARCHAR2(128) | PENDING if it is part of the pending area, NULL otherwise |
| MANDATORY | VARCHAR2(3) | Whether the resource plan is mandatory. Mandatory plans cannot be deleted. |