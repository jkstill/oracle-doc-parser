---
id: 19c__DBMS_TSDP_PROTECT.ASSOCIATE_POLICY
name: DBMS_TSDP_PROTECT.ASSOCIATE_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_PROTECT
tags: [dbms_tsdp_protect]
source_file: DBMS_TSDP_PROTECT.html
---

# DBMS_TSDP_PROTECT.ASSOCIATE_POLICY

This procedure associates or disassociates a TSDP policy with a sensitive column type.

## Syntax

```sql
DBMS_TSDP_PROTECT.ASSOCIATE_POLICY (
   policy_name        IN  VARCHAR2,
   sensitive_type     IN  VARCHAR2,
   associate          IN  BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| policy_name | VARCHAR2 | IN | Name of the TDSP policy |
| sensitive_type | VARCHAR2 | IN | Name of the sensitive column type: |
| associate | BOOLEAN | IN | Associate or Disassociate. TRUE implies Associate |

## Usage Notes

Syntax DBMS_TSDP_PROTECT.ASSOCIATE_POLICY ( policy_name IN VARCHAR2, sensitive_type IN VARCHAR2, associate IN BOOLEAN DEFAULT TRUE); Parameters Table 182-5 ASSOCIATE_POLICY Procedure Parameters Parameter Description policy_name Name of the TDSP policy sensitive_type Name of the sensitive column type: associate Associate or Disassociate. TRUE implies Associate Usage Notes Both the policy and the sensitive column type should exist in the database. Examples Associate PARTIAL_MASK_POLICY with SSN_TYPE : DBMS_TSDP_PROTECT.ASSOCIATE_POLICY ('PARTIAL_MASK_POLICY', 'SSN_TYPE');