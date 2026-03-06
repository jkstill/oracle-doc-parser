---
id: 19c__INTRODUCTION.PACKAGE
name: INTRODUCTION.PACKAGE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: INTRODUCTION
tags: [introduction]
source_file: introduction-to-oracle-supplied-plsql-packages-and-types.html
---

# INTRODUCTION.PACKAGE

PL/SQL packages have two parts: the specification and the body, although sometimes the body is unnecessary. The specification is the interface to your application; it declares the types, variables, constants, exceptions, cursors, and subprograms available for use. The body fully defines cursors and subprograms, and so implements the specification.

## Syntax

```sql
CREATE PACKAGE name AS  -- specification (visible part)
   -- public type and item declarations
   -- subprogram specifications
END [name];

CREATE PACKAGE BODY name AS  -- body (hidden part)
   -- private type and item declarations
   -- subprogram bodies
[BEGIN
   -- initialization statements]
END [name];
```

## Usage Notes

Unlike subprograms, packages cannot be called, parameterized, or nested. However, the formats of a package and a subprogram are similar: CREATE PACKAGE name AS -- specification (visible part) -- public type and item declarations -- subprogram specifications END [name]; CREATE PACKAGE BODY name AS -- body (hidden part) -- private type and item declarations -- subprogram bodies [BEGIN -- initialization statements] END [name]; The specification holds public declarations that are visible to your application. The body holds implementation details and private declarations that are hidden from your application. You can debug, enhance, or replace a package body without changing the specification. You can change a package body without recompiling calling programs because the implementation details in the body are hidden from your application.