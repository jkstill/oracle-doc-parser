---
id: 19c__DBMS_XDBT.CREATEDATASTOREPREF
name: DBMS_XDBT.CREATEDATASTOREPREF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDBT
tags: [dbms_xdbt]
source_file: DBMS_XDBT.html
---

# DBMS_XDBT.CREATEDATASTOREPREF

This procedure creates a user datastore preference for the CONTEXT index on the XML DB hierarchy.

## Syntax

```sql
DBMS_XDBT.CREATEDATASTOREPREF;
```

## Usage Notes

Syntax DBMS_XDBT.CREATEDATASTOREPREF; Usage Notes The name of the d atastore preference can be modified; see the DatastorePref configuration setting. The default USER datastore procedure also filters the incoming document. The DBMS_XDBT package provides a set of configuration settings that control the filtering process. The SkipFilter_Types array contains a list of regular expressions. Documents with a mime type that matches one of these expressions are not indexed. Some of the properties of the document metadata, such as author, remain unindexed. The NullFilter_Types array contains a list of regular expressions. Documents with a mime type that matches one of these expressions are not filtered; however, they are still indexed. This is intended to be used for documents that are text-based, such as HTML, XML and plain-text. All other documents use the INSO filter through the IFILTER API.