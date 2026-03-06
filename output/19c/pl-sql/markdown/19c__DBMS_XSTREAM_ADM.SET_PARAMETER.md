---
id: 19c__DBMS_XSTREAM_ADM.SET_PARAMETER
name: DBMS_XSTREAM_ADM.SET_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XSTREAM_ADM
tags: [dbms_xstream_adm]
source_file: DBMS_XSTREAM_ADM.html
---

# DBMS_XSTREAM_ADM.SET_PARAMETER

This procedure sets a parameter for an outbound server, an inbound server, or an outbound server's capture process.

## Syntax

```sql
DBMS_XSTREAM_ADM.SET_PARAMETER(
   streams_name    IN  VARCHAR2,
   streams_type    IN  VARCHAR2,
   parameter       IN  VARCHAR2,
   value           IN  VARCHAR2  DEFAULT NULL,
   no_wait         IN  BOOLEAN   DEFAULT FALSE,
   source_database IN  VARCHAR2  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| streams_type | VARCHAR2 | IN | The type of XStream client: Specify capture for a capture process. Specify apply for an outbound server or inbound server. |
| streams_name | VARCHAR2 | IN | The name of the capture process, outbound server, or inbound server. Do not specify an owner. |
| parameter | VARCHAR2 | IN | The name of the parameter you are setting. See " Capture Process Parameters " for information about capture process parameters. See " Apply Component Parameters " for information about outbound server and inbound server parameters. |
| value | VARCHAR2 | IN | The value to which the parameter is set. If NULL , then the parameter is set to its default value. |
| no_wait | BOOLEAN | IN | If TRUE , then the parameter is set immediately. If FALSE , then the parameter is set after synchronizing with the running capture process, inbound server, or outbound server. When you modify multiple parameters for the same process consecutively, setting this parameter to TRUE speeds up each call. However, if the process is currently running, you must set this parameter to FALSE in the last to the procedure to ensure that the process uses the modified parameter values. If the no_wait parameter is set to TRUE for the last call to the procedure, the running process might not detect the parameter changes. |
| source_database | VARCHAR2 | IN | If CURRENT , then the parameter is set only in the container where the procedure is invoked. CURRENT can be specified while connected to the root or to a PDB. If ALL , then the parameter is set in all containers in the CDB and all PDBs created after the procedure is invoked. To specify ALL , the procedure must be invoked in the root. If a container name, then the parameter is set in the specified container. To specify root, use CDB$ROOT while connected to the root. To specify a PDB, the procedure must be invoked in the root. Note: This parameter only applies to CDBs. Also, a non-null value can be specified only for the following parameters: include_objects capture parameter excludetag capture or apply parameter excludetrans capture or apply parameter excludeuser capture or apply parameter excludeuserid capture or apply parameter getreplicates capture or apply parameter getapplops capture or apply parameter |

## Usage Notes

Syntax DBMS_XSTREAM_ADM.SET_PARAMETER( streams_name IN VARCHAR2, streams_type IN VARCHAR2, parameter IN VARCHAR2, value IN VARCHAR2 DEFAULT NULL, no_wait IN BOOLEAN DEFAULT FALSE, source_database IN VARCHAR2 DEFAULT NULL); Parameters Table 217-33 SET_PARAMETER Procedure Parameters Parameter Description streams_type The type of XStream client: Specify capture for a capture process. Specify apply for an outbound server or inbound server. streams_name The name of the capture process, outbound server, or inbound server. Do not specify an owner. parameter The name of the parameter you are setting. See " Capture Process Parameters " for information about capture process parameters. See " Apply Component Parameters " for information about outbound server and inbound server parameters. value The value to which the parameter is set. If NULL , then the parameter is set to its default value. no_wait If TRUE , then the parameter is set immediately. If FALSE , then the parameter is set after synchronizing with the running capture process, inbound server, or outbound server. When you modify multiple parameters for the same process consecutively, setting this parameter to TRUE speeds up each call. However, if the process is currently running, you must set this parameter to FALSE in the last to the procedure to ensure that the process uses the modified parameter values. If the no_wait parameter is set to TRUE for the last call to the procedure, the running process might not detect the parameter changes. source_database If CURRENT , then the parameter is set only in the container where the procedure is invoked. CURRENT can be specified while connected to the root or to a PDB. If ALL , then the parameter is set in all containers in the CDB and all PDBs created after the procedure is invoked. To specify ALL , the procedure must be invoked in the root. If a container name, then the parameter is set in the specified container. To specify root, use CDB$ROOT while connected to the root. To specify a PDB, the procedure must be invoked in the root. Note: This parameter only applies to CDBs. Also, a non-null value can be specified only for the following parameters: include_objects capture parameter excludetag capture or apply parameter excludetrans capture or apply parameter excludeuser capture or apply parameter excludeuserid capture or apply parameter getreplicates capture or apply parameter getapplops capture or apply parameter