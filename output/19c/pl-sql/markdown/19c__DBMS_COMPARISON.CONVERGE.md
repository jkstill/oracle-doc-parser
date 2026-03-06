---
id: 19c__DBMS_COMPARISON.CONVERGE
name: DBMS_COMPARISON.CONVERGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_COMPARISON
tags: [dbms_comparison]
source_file: DBMS_COMPARISON.html
---

# DBMS_COMPARISON.CONVERGE

This procedure executes data manipulation language (DML) changes to synchronize the portion of the database objects that was compared in the specified scan.

## Syntax

```sql
DBMS_COMPARISON.CONVERGE(
   comparison_name      IN   VARCHAR2,
   scan_id              IN   NUMBER,
   scan_info            OUT  COMPARISON_TYPE,
   converge_options     IN   VARCHAR2  DEFAULT CMP_CONVERGE_LOCAL_WINS,
   perform_commit       IN   BOOLEAN   DEFAULT TRUE,
   local_converge_tag   IN   RAW       DEFAULT NULL,
   remote_converge_tag  IN   RAW       DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| comparison_name | VARCHAR2 | IN | The name of the comparison. |
| scan_id | NUMBER | IN | The identifier for the scan that contains the differences between the database objects being converged. See " Overview " for more information about specifying a scan ID in this parameter. |
| scan_info | COMPARISON_TYPE | OUT | Information about the converge operation returned in the COMPARISON_TYPE datatype. See COMPARISON_TYPE Record Type . |
| converge_options | VARCHAR2 | IN | Either the CMP_CONVERGE_LOCAL_WINS constant or the CMP_CONVERGE_REMOTE_WINS constant. See " Constants " for information about these constants. |
| perform_commit | BOOLEAN | IN | If TRUE , then performs a COMMIT periodically while making the DML changes. The CONVERGE procedure might perform more than one COMMIT when this parameter is set to TRUE . If FALSE , then does not perform a COMMIT after making DML changes. |
| local_converge_tag | RAW | IN | The Replication tag to set in the session on the local database before performing any changes to converge the data in the database objects being converged. If non- NULL , then this parameter setting takes precedence over the local_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison. If NULL , then this parameter is ignored, and the local_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison is used. |
| remote_converge_tag | RAW | IN | The Replication tag to set in the session on the remote database before performing any changes to converge the data in the database objects being converged. If non- NULL , then this parameter setting takes precedence over the remote_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison. If NULL , then this parameter is ignored, and the remote_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison is used. |

## Usage Notes

Syntax DBMS_COMPARISON.CONVERGE( comparison_name IN VARCHAR2, scan_id IN NUMBER, scan_info OUT COMPARISON_TYPE, converge_options IN VARCHAR2 DEFAULT CMP_CONVERGE_LOCAL_WINS, perform_commit IN BOOLEAN DEFAULT TRUE, local_converge_tag IN RAW DEFAULT NULL, remote_converge_tag IN RAW DEFAULT NULL); Parameters Table 37-5 CONVERGE Procedure Parameters Parameter Description comparison_name The name of the comparison. scan_id The identifier for the scan that contains the differences between the database objects being converged. See " Overview " for more information about specifying a scan ID in this parameter. scan_info Information about the converge operation returned in the COMPARISON_TYPE datatype. See COMPARISON_TYPE Record Type . converge_options Either the CMP_CONVERGE_LOCAL_WINS constant or the CMP_CONVERGE_REMOTE_WINS constant. See " Constants " for information about these constants. perform_commit If TRUE , then performs a COMMIT periodically while making the DML changes. The CONVERGE procedure might perform more than one COMMIT when this parameter is set to TRUE . If FALSE , then does not perform a COMMIT after making DML changes. local_converge_tag The Replication tag to set in the session on the local database before performing any changes to converge the data in the database objects being converged. If non- NULL , then this parameter setting takes precedence over the local_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison. If NULL , then this parameter is ignored, and the local_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison is used. remote_converge_tag The Replication tag to set in the session on the remote database before performing any changes to converge the data in the database objects being converged. If non- NULL , then this parameter setting takes precedence over the remote_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison. If NULL , then this parameter is ignored, and the remote_converge_tag parameter in the CREATE_COMPARISON procedure that created the comparison is used. Usage Notes If one of the database objects being converged is a read-only materialized view, then the converge_options parameter must be set to ensure that the read-only materialized view "wins" in the converge operation. The CONVERGE procedure raises an error if it tries to make changes to a read-only materialized view.