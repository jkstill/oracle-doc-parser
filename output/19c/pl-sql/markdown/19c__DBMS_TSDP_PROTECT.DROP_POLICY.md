---
id: 19c__DBMS_TSDP_PROTECT.DROP_POLICY
name: DBMS_TSDP_PROTECT.DROP_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_PROTECT
tags: [dbms_tsdp_protect]
source_file: DBMS_TSDP_PROTECT.html
---

# DBMS_TSDP_PROTECT.DROP_POLICY

This procedure removes a TDSP policy or one of its condition-enable_options combinations.

## Syntax

```sql
DBMS_TSDP_PROTECT.DROP_POLICY (
   policy_name              IN VARCHAR2, 
   policy_apply_condition   IN POLICY_CONDITIONS);

DBMS_TSDP_PROTECT.DROP_POLICY (
   policy_name              IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| policy_name | VARCHAR2 | IN | Name of the policy to drop |
| policy_apply_condition | POLICY_CONDITIONS) | IN | To be initialized with the relevant condition |

## Usage Notes

Syntax DBMS_TSDP_PROTECT.DROP_POLICY ( policy_name IN VARCHAR2, policy_apply_condition IN POLICY_CONDITIONS); DBMS_TSDP_PROTECT.DROP_POLICY ( policy_name IN VARCHAR2); Parameters Table 182-9 DROP_POLICY Procedure Parameters Parameter Description policy_name Name of the policy to drop policy_apply_condition To be initialized with the relevant condition Usage Notes The combination of policy_conditions and policy_enable_options can be dropped from a TSDP policy by giving the policy_apply_condition parameter. The default condition-default options combination can also be dropped (if it exists for the policy) by passing an empty associative array of type DBMS_TSDP_PROTECT.POLICY_CONDITION . If the condition-enable_options combination that is being dropped is the last condition-enable_options combination for the policy, the policy itself is dropped. A policy can be completely dropped by using the overloaded of the procedure that takes only policy_name . A policy or one of its conditions can be dropped only if the policy is not associated with any sensitive column type. This also means that a policy that is being dropped is not enabled on any column (object). Examples Dropping the condition-enable_options combination based on a specific condition: DECLARE policy_conditions DBMS_TSDP_PROTECT.POLICY_CONDITIONS; BEGIN policy_conditions (DBMS_TSDP_PROTECT.DATATYPE) := 'VARCHAR2'; DBMS_TSDP_PROTECT.DROP_POLICY ('PARTIAL_MASK_POLICY', policy_conditions); END; The default condition-enable_options combination can be dropped by passing an empty associative array of type DBMS_TSDP_PROTECT.POLICY_CONDITIONS for the policy_apply_condition parameter: DECLARE policy_conditions DBMS_TSDP_PROTECT.POLICY_CONDITIONS; BEGIN DBMS_TSDP_PROTECT.DROP_POLICY ('redact_partial_cc', policy_conditions); END; Dropping a TSDP policy: BEGIN DBMS_TSDP_PROTECT.DROP_POLICY( policy_name => 'PARTIAL_MASK_POLICY'); END;