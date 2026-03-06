---
id: 19c__DBMS_AQ.POST
name: DBMS_AQ.POST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQ
tags: [dbms_aq]
source_file: DBMS_AQ.html
---

# DBMS_AQ.POST

This procedure posts to a list of anonymous subscriptions that allows all clients who are registered for the subscriptions to get notifications.

## Syntax

```sql
DBMS_AQ.POST (
  post_list       IN  SYS.AQ$_POST_INFO_LIST,
  post_count      IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| post_list | SYS.AQ$_POST_INFO_LIST | IN | Specifies the list of anonymous subscriptions to which you want to post. It is a list of AQ$_POST_INFO_LIST Type . |
| post_count | NUMBER) | IN | Specifies the number of entries in the post_list. |

## Usage Notes

Syntax DBMS_AQ.POST ( post_list IN SYS.AQ$_POST_INFO_LIST, post_count IN NUMBER); Parameters Table 22-12 POST Procedure Parameters Parameter Description post_list Specifies the list of anonymous subscriptions to which you want to post. It is a list of AQ$_POST_INFO_LIST Type . post_count Specifies the number of entries in the post_list. Usage Notes This procedure is used to post to anonymous subscriptions which allows all clients who are registered for the subscriptions to get notifications. Several subscriptions can be posted to at one time.