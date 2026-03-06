---
id: 19c__DBA_REGISTRY_HISTORY
name: DBA_REGISTRY_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_REGISTRY_HISTORY.html
---

# DBA_REGISTRY_HISTORY

DBA_REGISTRY_HISTORY provides information about upgrades, downgrades, and critical patch updates that have been performed on the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ACTION_TIME | TIMESTAMP(6) | The time the upgrade, downgrade, or patch action was completed |
| ACTION | VARCHAR2(30) | The specific action (for example, UPGRADE or DOWNGRADE) |
| NAMESPACE | VARCHAR2(30) | The namespace of the components affected (for example, SERVER) |
| VERSION | VARCHAR2(30) | The version number of the server (for example, 10.2.0.1.0) |
| ID | NUMBER | Bundle ID |
| COMMENTS | VARCHAR2(255) | Additional comments about the action taken |
| BUNDLE_SERIES | VARCHAR2(30) | If a bundle patch, the series (for example, PSU or DBBP) |