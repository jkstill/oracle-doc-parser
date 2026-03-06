---
id: 19c__DBMS_SPACE
name: DBMS_SPACE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE

This function returns recommendations using the stored results of the auto segment advisor. This function returns results from the latest run on any given object.

## Syntax

```sql
DBMS_SPACE.ASA_RECOMMENDATIONS (
   all_runs        IN    VARCHAR2 DEFAULT := TRUE,
   show_manual     IN    VARCHAR2 DEFAULT := TRUE,
   show_findings   IN    VARCHAR2 DEFAULT := FALSE)
 RETURN ASA_RECO_ROW_TB PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| all_runs | VARCHAR2 | IN | Returns the results of all the auto advisor runs or only the results of the latest run. The valid values are TRUE and FALSE . The default value is TRUE . If TRUE , returns recommendations/findings for all runs of auto segment advisor. If FALSE , returns the results of the LATEST run only. LATEST does not make sense for manual invocation of segment advisor. This is applicable only for auto advisor. |
| show_manual | VARCHAR2 | IN | This parameter is used to indicate if the results of manual jobs should be included. If TRUE , results of manual tasks are shown. If FALSE , results of manual tasks are not shown. Specifying manual=true does not negate the specification of auto advisor tasks. However, the all_runs settings may override manual. If all_runs is FALSE , implying we only want to see the latest of auto advisor job, then manual may not be specified as TRUE . The valid values are TRUE and FALSE . The default value is TRUE . |
| show_findings | VARCHAR2 | IN | Shows only the findings instead of the recommendations. The valid values are TRUE and FALSE . The default value is FALSE . |

**Returns:** `ASA_RECO_ROW_TB`

## Usage Notes

Syntax DBMS_SPACE.ASA_RECOMMENDATIONS ( all_runs IN VARCHAR2 DEFAULT := TRUE, show_manual IN VARCHAR2 DEFAULT := TRUE, show_findings IN VARCHAR2 DEFAULT := FALSE) RETURN ASA_RECO_ROW_TB PIPELINED; Parameters Table 158-4 ASA_RECOMMENDATIONS Procedure Parameters Parameter Description all_runs Returns the results of all the auto advisor runs or only the results of the latest run. The valid values are TRUE and FALSE . The default value is TRUE . If TRUE , returns recommendations/findings for all runs of auto segment advisor. If FALSE , returns the results of the LATEST run only. LATEST does not make sense for manual invocation of segment advisor. This is applicable only for auto advisor. show_manual This parameter is used to indicate if the results of manual jobs should be included. If TRUE , results of manual tasks are shown. If FALSE , results of manual tasks are not shown. Specifying manual=true does not negate the specification of auto advisor tasks. However, the all_runs settings may override manual. If all_runs is FALSE , implying we only want to see the latest of auto advisor job, then manual may not be specified as TRUE . The valid values are TRUE and FALSE . The default value is TRUE . show_findings Shows only the findings instead of the recommendations. The valid values are TRUE and FALSE . The default value is FALSE . Table 158-5 Parameter Usage all_runs show_manual show_ findings Outcome TRUE TRUE TRUE All findings from auto advisor and manual tasks. TRUE TRUE FALSE All recommendations from auto advisor and manual tasks. TRUE FALSE TRUE All findings from auto advisor tasks. TRUE FALSE FALSE All recommendations from all auto advisor tasks. FALSE TRUE TRUE N/A FALSE TRUE FALSE N/A FALSE FALSE TRUE Findings for the latest auto advisor task. FALSE FALSE FALSE Recommendations from the latest auto advisor task.