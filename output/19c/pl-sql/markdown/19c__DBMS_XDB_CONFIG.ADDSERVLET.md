---
id: 19c__DBMS_XDB_CONFIG.ADDSERVLET
name: DBMS_XDB_CONFIG.ADDSERVLET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.ADDSERVLET

This procedure adds a servlet to XDB configuration.

## Syntax

```sql
<servlet>
     <servlet-name>name</servlet-name>     <servlet-language>language</servlet-language>
     <display-name>dispname</display-name>
     <description>descript</description>
     <servlet-class>class</servlet-class>
     <servlet-schema>schema</servlet-schema>
</servlet>
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name |  |  | Servlet name |
| language |  |  | Must be one of "C", "Java", "PL/SQL" |
| dispname |  |  | Display name |
| icon |  |  | Icon |
| descript |  |  | Description |
| class |  |  | The class / jspfile / plsql function corresponding to this servlet. The first non- NULL argument amongst these three is chosen, and the others are treated as NULL . |
| jspfile |  |  | This parameter is not supported. Always provide NULL value for this parameter. System throws an error if the value is not NULL . |
| plsql |  |  | The class / jspfile / plsql function corresponding to this servlet. The first non- NULL argument amongst these three is chosen, and the others are treated as NULL . |
| schema |  |  | Schema is used to specify servlet-schema xml element name in xdbconfig.xml . It indicates the Oracle schema in which the Java class is loaded. If you do not specify any value, then the schema is searched using the default resolver specification. |

## Usage Notes

IT adds the following servlet: <servlet> <servlet-name>name</servlet-name> <servlet-language>language</servlet-language> <display-name>dispname</display-name> <description>descript</description> <servlet-class>class</servlet-class> <servlet-schema>schema</servlet-schema> </servlet> Syntax DBMS_XDB_CONFIG.ADDSERVLET( name IN VARCHAR2, language IN VARCHAR2, dispname IN VARCHAR2, icon IN VARCHAR2 := NULL, descript IN VARCHAR2 := NULL, class IN VARCHAR2 := NULL, jspfile IN VARCHAR2 := NULL, plsql IN VARCHAR2 := NULL, schema IN VARCHAR2 := NULL); Parameters Table 196-6 ADDSERVLET Procedure Parameters Parameter Description name Servlet name language Must be one of "C", "Java", "PL/SQL" dispname Display name icon Icon descript Description class The class / jspfile / plsql function corresponding to this servlet. The first non- NULL argument amongst these three is chosen, and the others are treated as NULL . jspfile This parameter is not supported. Always provide NULL value for this parameter. System throws an error if the value is not NULL . plsql The class / jspfile / plsql function corresponding to this servlet. The first non- NULL argument amongst these three is chosen, and the others are treated as NULL . schema Schema is used to specify servlet-schema xml element name in xdbconfig.xml . It indicates the Oracle schema in which the Java class is loaded. If you do not specify any value, then the schema is searched using the default resolver specification.