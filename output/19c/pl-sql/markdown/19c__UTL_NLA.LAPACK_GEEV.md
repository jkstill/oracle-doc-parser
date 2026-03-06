---
id: 19c__UTL_NLA.LAPACK_GEEV
name: UTL_NLA.LAPACK_GEEV
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_NLA
tags: [utl_nla]
source_file: UTL_NLA.html
---

# UTL_NLA.LAPACK_GEEV

This procedures computes for an n by n real nonsymmetric matrix A , the eigenvalues and, optionally, the left and/or right eigenvectors.

## Syntax

```sql
UTL_NLA.LAPACK_GEEV (
   jobvl   IN      flag,
   jobvr   IN      flag,
   n       IN      POSITIVEN,
   a       IN OUT  UTL_NLA_ARRAY_DBL,
   lda     IN      POSITIVEN,
   wr      IN OUT  UTL_NLA_ARRAY_DBL,
   wi      IN OUT  UTL_NLA_ARRAY_DBL,
   vl      IN OUT  UTL_NLA_ARRAY_DBL,
   ldvl    IN      POSITIVEN,
   vr      IN OUT  UTL_NLA_ARRAY_DBL,
   ldvr    IN      POSITIVEN,
   info    OUT     INTEGER,
   pack    IN      flag DEFAULT 'C');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| jobvl | flag | IN | 'N' : Left eigenvectors of A are not computed. 'V' : Left eigenvectors of A are computed. |
| jobvr | flag | IN | 'N' : Right eigenvectors of A are not computed. 'V' : Right eigenvectors of A are computed. |
| n | POSITIVEN | IN | The order of the matrix a. N >= 0 . |
| a | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit, A has been overwritten. |
| lda | POSITIVEN | IN | The leading dimension of the array a. lda >= max(1,n) . |
| wr | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues. Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. |
| wi | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz, n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues. Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. |
| vl | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If jobvl = 'V' , the left eigenvectors u(j) are stored one after another in the columns of vl , in the same order as their eigenvalues. If jobvs = 'N' , vl is not referenced. If the j -th eigenvalue is real, then u(j) = VL(:,j) , the j -th column of vl . If the j -th and (j+1)-st eigenvalues form a complex conjugate pair, then u(j) = VL(:,j) + i*VL(:,j+1) and u(j+1) = VL(:,j) - i*VL(:,j+1) . |
| ldv1 |  |  | The leading dimension of the array vl . ldvl >= 1. If jobvl = 'v' , ldvl >= n . |
| vr | UTL_NLA_ARRAY_DBL | IN OUT | UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldvr, n) . If jobvr = 'V' , the right eigenvectors v(j) are stored one after another in the columns of vr , in the same order as their eigenvalues.. If jobvr = 'N' , vr is not referenced. If the j -th eigenvalue is real, then v(j) = VR(:,j) , the j -th column of vr . If the j -th and (j+1)-st eigenvalues form a complex conjugate pair, then v(j) = VR(:,j) + i*VR(:,j+1) and v(j+1) = VR(:,j) - i*VR(:,j+1) . |
| ldvr | POSITIVEN | IN | The leading dimension of the array vr . vr.ldvr >= 1 . If jobvr = 'V' , ldvr >= N |
| info | INTEGER | OUT | = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , and i is <= N : the QR algorithm failed to compute all the eigenvalues, and no eigenvectors have been computed. Elements i+1:N of wr and wi contain eigenvalues which have converged.. |
| pack | flag | IN | (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major |

## Usage Notes

The right eigenvector v(j) of A satisfies A * v(j) = lambda(j) * v(j) where lambda(j) is its eigenvalue. The left eigenvector u(j) of A satisfies u(j)**H * A = lambda(j) * u(j)**H where u(j)**H denotes the conjugate transpose of u(j) . The computed eigenvectors are normalized to have Euclidean norm equal to 1 and largest component real. See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group See Also: LAPACK Driver Routines (LLS and Eigenvalue Problems) Subprograms for other subprograms in this group Syntax UTL_NLA.LAPACK_GEEV ( jobvl IN flag, jobvr IN flag, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_DBL, lda IN POSITIVEN, wr IN OUT UTL_NLA_ARRAY_DBL, wi IN OUT UTL_NLA_ARRAY_DBL, vl IN OUT UTL_NLA_ARRAY_DBL, ldvl IN POSITIVEN, vr IN OUT UTL_NLA_ARRAY_DBL, ldvr IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); UTL_NLA.LAPACK_GEEV ( jobvl IN flag, jobvr IN flag, n IN POSITIVEN, a IN OUT UTL_NLA_ARRAY_FLT, lda IN POSITIVEN, wr IN OUT UTL_NLA_ARRAY_FLT, wi IN OUT UTL_NLA_ARRAY_FLT, vl IN OUT UTL_NLA_ARRAY_FLT, ldvl IN POSITIVEN, vr IN OUT UTL_NLA_ARRAY_FLT, ldvr IN POSITIVEN, info OUT INTEGER, pack IN flag DEFAULT 'C'); Parameters Table 271-45 LAPACK_GEEV Procedure Parameters Parameter Description jobvl 'N' : Left eigenvectors of A are not computed. 'V' : Left eigenvectors of A are computed. jobvr 'N' : Right eigenvectors of A are not computed. 'V' : Right eigenvectors of A are computed. n The order of the matrix a. N >= 0 . a UTL_NLA_ARRAY_FLT/DBL , DIMENSION (lda, n) . On entry, the n by n matrix A . On exit, A has been overwritten. lda The leading dimension of the array a. lda >= max(1,n) . wr UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues. Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. wi UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldz, n) . wr and wi contain the real and imaginary parts respectively of the computed eigenvalues. Complex conjugate pairs of eigenvalues will appear consecutively with the eigenvalue having the positive imaginary part first. vl UTL_NLA_ARRAY_FLT/DBL , DIMENSION (n) . If jobvl = 'V' , the left eigenvectors u(j) are stored one after another in the columns of vl , in the same order as their eigenvalues. If jobvs = 'N' , vl is not referenced. If the j -th eigenvalue is real, then u(j) = VL(:,j) , the j -th column of vl . If the j -th and (j+1)-st eigenvalues form a complex conjugate pair, then u(j) = VL(:,j) + i*VL(:,j+1) and u(j+1) = VL(:,j) - i*VL(:,j+1) . ldv1 The leading dimension of the array vl . ldvl >= 1. If jobvl = 'v' , ldvl >= n . vr UTL_NLA_ARRAY_FLT/DBL , DIMENSION (ldvr, n) . If jobvr = 'V' , the right eigenvectors v(j) are stored one after another in the columns of vr , in the same order as their eigenvalues.. If jobvr = 'N' , vr is not referenced. If the j -th eigenvalue is real, then v(j) = VR(:,j) , the j -th column of vr . If the j -th and (j+1)-st eigenvalues form a complex conjugate pair, then v(j) = VR(:,j) + i*VR(:,j+1) and v(j+1) = VR(:,j) - i*VR(:,j+1) . ldvr The leading dimension of the array vr . vr.ldvr >= 1 . If jobvr = 'V' , ldvr >= N info = 0 : successful exit < 0 : if info = -i , the i -th argument had an illegal value > 0 : if info = i , and i is <= N : the QR algorithm failed to compute all the eigenvalues, and no eigenvectors have been computed. Elements i+1:N of wr and wi contain eigenvalues which have converged.. pack (Optional) Flags the packing of the matrices: 'C' : column-major (default) 'R' : row-major