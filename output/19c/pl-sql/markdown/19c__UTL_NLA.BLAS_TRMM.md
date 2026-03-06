---
id: 19c__UTL_NLA.BLAS_TRMM
name: UTL_NLA.BLAS_TRMM
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.BLAS_TRMM

This procedure performs a matrix-matrix operation.

## Syntax

```sql
B := alpha*op( A )*B
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| side |  |  | Specifies whether the symmetric matrix A appears on the left or right in the operation: side = 'L' or 'l' : B := alpha*op(A)*B side = 'R' or 'r' : B := alpha*B*op(A) |
| uplo |  |  | Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' : A is an upper triangular matrix. uplo = 'L' or 'l' ' : A is a lower triangular matrix. |
| transa |  |  | Specifies the form of op (A) to be used in the matrix multiplication as follows: transa = 'N' or 'n' : op(A) = A transa = 'T' or 't' : op(A) = A' transa = 'C' or 'c' : op(A) = A' |
| diag |  |  | Specifies whether or not A is unit triangular: diag = 'U' or 'u' . A is assumed to be unit triangular. diag = 'N' or 'n' . A is not assumed to be unit triangular. |
| m |  |  | Specifies the number of rows of the B . m must be at least zero. |
| n |  |  | Specifies the number of columns of B . n must be at least zero. |
| alpha |  |  | SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. When alpha is zero then A is not referenced and B need not be set before entry. |
| a |  |  | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,k) where k is m when side = 'L' or 'l' , and is n when side = ' 'R' or 'r' . Before entry with uplo = 'U' or 'u' , the leading k by k upper triangular part of the array A must contain the upper triangular matrix, and the strictly lower triangular part of A is not referenced. Before entry with uplo = 'L' or 'l' , the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced. Note that when diag = ' 'U' or 'u' , the diagonal elements of A are not referenced either, but are assumed to be unity. |
| lda |  |  | Specifies the first dimension of a as declared in the calling (sub) program. When side = 'L' or 'l' , lda must be at least max(1,m) , otherwise lda must be at least max(1,n) . |
| b |  |  | UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldb,n) . Before entry, the leading m by n part of the array B must contain the matrix B , and on exit is overwritten by the transformed matrix. |
| ldb |  |  | Specifies the first dimension of b as declared in the calling (sub) program. ldb must be at least max(1,m) . |
| pack |  |  | (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major |

## Usage Notes

It performs one of the following matrix-matrix operations: B := alpha*op( A )*B or B := alpha*B*op( A ) where alpha is a scalar, B is an m by n matrix, A is a unit, or non-unit, upper or lower triangular matrix and op(A) is one of op( A ) = A or op( A ) = A' See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group See Also: BLAS Level 3 (Matrix-Matrix Operations) Subprograms for other subprograms in this group Syntax UTL_NLA.BLAS_TRMM ( side IN flag, uplo IN flag, transa IN flag, diag IN flag, m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_DOUBLE, a IN UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_DBL, ldb IN POSITIVEN, pack IN flag DEFAULT 'C'); UTL_NLA.BLAS_TRMM ( side IN flag, uplo IN flag, transa IN flag, diag IN flag, m IN POSITIVEN, n IN POSITIVEN, alpha IN SCALAR_FLOAT, a IN UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, b IN OUT UTL_NLA_ARRAY_FLT, ldb IN POSITIVEN, pack IN flag DEFAULT 'C'); Parameters Table 271-35 BLAS_TRMM Procedure Parameters Parameter Description side Specifies whether the symmetric matrix A appears on the left or right in the operation: side = 'L' or 'l' : B := alpha*op(A)*B side = 'R' or 'r' : B := alpha*B*op(A) uplo Specifies whether the upper or lower triangular part of the array A is to be referenced: uplo = 'U' or 'u' : A is an upper triangular matrix. uplo = 'L' or 'l' ' : A is a lower triangular matrix. transa Specifies the form of op (A) to be used in the matrix multiplication as follows: transa = 'N' or 'n' : op(A) = A transa = 'T' or 't' : op(A) = A' transa = 'C' or 'c' : op(A) = A' diag Specifies whether or not A is unit triangular: diag = 'U' or 'u' . A is assumed to be unit triangular. diag = 'N' or 'n' . A is not assumed to be unit triangular. m Specifies the number of rows of the B . m must be at least zero. n Specifies the number of columns of B . n must be at least zero. alpha SCALAR_FLOAT / DOUBLE . Specifies the scalar alpha. When alpha is zero then A is not referenced and B need not be set before entry. a UTL_NLA_ARRAY_FLT / DBL of DIMENSION (lda,k) where k is m when side = 'L' or 'l' , and is n when side = ' 'R' or 'r' . Before entry with uplo = 'U' or 'u' , the leading k by k upper triangular part of the array A must contain the upper triangular matrix, and the strictly lower triangular part of A is not referenced. Before entry with uplo = 'L' or 'l' , the leading k by k lower triangular part of the array A must contain the lower triangular matrix and the strictly upper triangular part of A is not referenced. Note that when diag = ' 'U' or 'u' , the diagonal elements of A are not referenced either, but are assumed to be unity. lda Specifies the first dimension of a as declared in the calling (sub) program. When side = 'L' or 'l' , lda must be at least max(1,m) , otherwise lda must be at least max(1,n) . b UTL_NLA_ARRAY_FLT / DBL of DIMENSION (ldb,n) . Before entry, the leading m by n part of the array B must contain the matrix B , and on exit is overwritten by the transformed matrix. ldb Specifies the first dimension of b as declared in the calling (sub) program. ldb must be at least max(1,m) . pack (Optional) Flags the packing of the matrices: ' C ': column-major (default) ' R ': row-major