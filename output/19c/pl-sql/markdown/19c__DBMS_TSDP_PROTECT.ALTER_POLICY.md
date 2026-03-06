---
id: 19c__DBMS_TSDP_PROTECT.ALTER_POLICY
name: DBMS_TSDP_PROTECT.ALTER_POLICY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_TSDP_PROTECT
tags: [dbms_tsdp_protect]
source_file: DBMS_TSDP_PROTECT.html
---

# DBMS_TSDP_PROTECT.ALTER_POLICY

This procedure alters an existing TDSP policy

## Syntax

```sql
DBMS_TSDP_PROTECT.ALTER_POLICY (
   policy_name              IN VARCHAR2, 
   policy_enable_options    IN FEATURE_OPTIONS,
   policy_apply_condition   IN POLICY_CONDITION default TSDP$default_condition);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| policy_name | VARCHAR2 | IN | Name of the policy to alter |
| policy_enable_options | FEATURE_OPTIONS | IN | Initialized with the parameter-value pairs corresponding to the security feature |
| policy_apply_condition | POLICY_CONDITION | IN | Initialized with the property-value pairs that must be satisfied in order to apply the corresponding policy_enable_options . This is an associative array with Property as the key ( PLS_INTEGER ). Example: example_policy_condition ( Property )= property_value . Permissible values for Property: DBMS_TSDP_PROPERTY.DATATYPE DBMS_TSDP_PROPERTY.LENGTH DBMS_TSDP_PROPERTY.PARENT_SCHEMA DBMS_TSDP_PROPERTY.PARENT_TABLE |

## Usage Notes

Syntax DBMS_TSDP_PROTECT.ALTER_POLICY ( policy_name IN VARCHAR2, policy_enable_options IN FEATURE_OPTIONS, policy_apply_condition IN POLICY_CONDITION default TSDP$default_condition); Parameters Table 182-4 ALTER_POLICY Procedure Parameters Parameter Description policy_name Name of the policy to alter policy_enable_options Initialized with the parameter-value pairs corresponding to the security feature policy_apply_condition Initialized with the property-value pairs that must be satisfied in order to apply the corresponding policy_enable_options . This is an associative array with Property as the key ( PLS_INTEGER ). Example: example_policy_condition ( Property )= property_value . Permissible values for Property: DBMS_TSDP_PROPERTY.DATATYPE DBMS_TSDP_PROPERTY.LENGTH DBMS_TSDP_PROPERTY.PARENT_SCHEMA DBMS_TSDP_PROPERTY.PARENT_TABLE Usage Notes If the policy_apply_condition matches an existing condition for the policy, then the corresponding enable options are updated with policy_enable_options . If the policy_apply_condition does not match any existing condition for the policy, the combination of policy_enable_options and policy_apply_condition is added to the policy. Examples Add a new combination of policy_apply_condition and policy_enable_options to an existing policy PARTIAL_MASK_POLICY : DECLARE redact_feature_options DBMS_TSDP_PROTECT.FEATURE_OPTIONS; policy_conditions DBMS_TSDP_PROTECT.POLICY_CONDITIONS; BEGIN redact_feature_options ('expression') := 'SYS_CONTEXT(''USERENV'',''SESSION_USER'')=''APPUSER'''; redact_feature_options ('function_type') := 'DBMS_REDACT.PARTIAL'; redact_feature_options ('function_parameters') := 'STR, VVVVVVVVV,VVVVVVVVV, *, 1, 6'; policy_conditions (DBMS_TSDP_PROTECT.DATATYPE) := 'VARCHAR2'; DBMS_TSDP_PROTECT.ALTER_POLICY ('PARTIAL_MASK_POLICY', redact_feature_options, policy_conditions); END;