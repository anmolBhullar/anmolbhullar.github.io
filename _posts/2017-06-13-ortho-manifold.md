---
layout: post
title: How the set of n by n orthogonal matrices forms a lie group.
summary: Some knowledge of linear algebra and basic group theory is required!
---

Preface: This article is the beginning of a series of articles about 
random parts about math that I find really cool.

I've always suspected that algebra and differential topology were somehow connected in some way, 
(after all, a lot of fields in Math are like this) but I've personally done any math which integrates
algebra and differential topology so seamlessly. This is why when I encountered this in <em>Differential
Topology by Victor Guillemin and Allan Pollack</em>, it blew my mind. This is why I wanted to write
this article to showcase the relationship between lie groups and orthogonal matrices.

### What is an Orthogonal Matrix?

Consider the rotation matrix \\(R(\theta)\\) in \\(\mathbb{R}^2\\). This is a matrix/transformation
which is distance preserving. I mean, 'distance preserving' in the same sense of the functions that
one would use to apply a change of variables in an integral. If we generalize this notion of linear
maps which are distance preserving, we obtain the idea of an orthogonal matrix. For example, in
order for a matrix \\(Q\\) to be distance preserving, we can say that it needs to preserve the dot
product, so, we can say that if \\(Q\\) is an \\(n\times n\\) dimensional matrix (i.e. a function
\\(\mathbb{R^n} \to \mathbb{R^n})\\), then it must obey the following rule for \\(u,v\in\mathbb{R}^n\\):
\\[ u\cdot v = (Qu)\cdot(Qv)\\]
This implies an important result. For any \\(v\in\mathbb{R}^n\\), we have that:
\\[ v^{T}\cdot v = (Qv)^{T}\cdot(Qv) = (v^{T}Q^{T})(Qv) = v^{T}(Q^{T}Q)v \\]
which implies that \\(Q^{T}Q = I\\) or in other words: \\(Q^{T} = Q^{-1}\\). Thus, we can just
define orthogonal matrices as matrices whose inverse is equal to its transpose.

### Step 1: Show the set of \\(n\times n\\) orthogonal matrices form a smooth manifold

Let \\(O(n)\\) be the set of \\(n\times n\\) orthogonal matrices, \\(S(n)\\) for symmetric matrices and
\\(M(n)\\) for any general matrix in \\(\mathbb{R}^{n}\\). 

Remark: We know that, \\(S(n)\\) forms a subspace under the vector space \\(M(n)\\). Thus, we can calculate
the dimension of this subspace explicitly. We know that to uniquely determine a symmetric matrix,
it suffices to only list the entries in the upper triangle part of the matrix as well as the 
diagonal. Thus, to uniquely determine an element in \\(S(n)\\), we need:
\\[ \frac{n^{2}}{2} + n = \frac{(n)(n+1)}{2} \\]
elements. Thus, \\(S(n)\\) is of dimension \\(\mathbb{R}^{k}\\) where \\(k=\frac{(n)(n+1)}{2}\\).

This proof that \\(O(n)\\) is a manifold under \\(M(n)=\mathbb{R}^{n^{2}}\\) is a very clear
application of the pre-image theorem so we state it first but before, we state that, we need to have
a notion of a regular value. So we state these two things now before attempting to prove anything:

What is a regular value?

Let \\(f: X\to Y\\) be a smooth map between manifolds. Then \\(y\\) is a regular value of \\(f\\) if
and only if every for all \\(x\in f^{-1}(y) \\), \\(df_{x}: T_{x}(X) \to T_{y}(Y)\\) is surjective
where \\(y = f(x)\\).

What is the pre-image theorem?

If \\(y\\) is a regular value of \\(f: X\to Y\\), then the preimage \\(f^{-1}(y)\\) is a
submanifold of \\(X\\), with dim \\(f^{-1}(y) =\\) dim \\(X\\) - dim \\(Y\\).

Thus, for our purposes, let \\(f: M(n) \to S(n)\\) via \\(A \mapsto AA^{T}\\). Since for any orthogonal
matrix \\(Q\\), \\(QQ^{T} = I\\), it follows that we want to determine if the preimage \\(f^{-1}(I)\\)
is a submanifold of \\(M(n)\\). Thus, it leaves us to check that \\(I\\) is a regular value of \\(f\\)
or in other words, it leaves us to check that for any \\(A\in f^{-1}(I)\\) (so any orthogonal matrix),
\\(df_{A}: T_{A}(M(n)) \to T_{f(A)}(S(n))\\) is surjective. First, note that for any \\(B\in M(n)\\):

\begin{align}
        df_{A}(B) = \lim_{h\to 0} \frac{f(A+h)-f(A)}{h}
        = \lim_{h\to 0} BA^{T} + AB^{T} + hBB^{T}
        = BA^{T} + AB^{T}
\end{align}

So, we want to check that for any matrix \\(C\in S(n)\\), that, there exists \\(B\in M(n)\\) such
that \\(df_{A}(B) = BA^{T} + AB^{T} = C\\). Note that since \\(C\\) is symmetric, then
\\(\frac{1}{2}C + \frac{1}{2}C^{T} = C\\). Thus, if we suppose that \\(BA^{T} = \frac{1}{2}C\\), then:
\\[ BA^{T} = \frac{1}{2}C \implies B = \frac{1}{2}CA\\]
so,
\begin{align}
    BA^{T} + AB^{T} = (\frac{1}{2}CA)A^{T} + A(\frac{1}{2}CA)^{T} = \frac{1}{2}(C+C^{T}) = C
\end{align}

So, we see that \\(df_{A}: M(n) \to S(n)\\) is surjective for any \\(A\in O(n)\\), proving that
\\(f^{-1}(I)=O(n)\\) is a manifold under \\(M(n)\\).

In order, to show this is a lie group under the operation of matrix multiplication:
\\[ O(n) \times O(n) \to O(n) \\]
is a smooth operation, it suffices to show that if \\(A,B\in O(n)\\), then \\(AB\\) is an
orthogonal matrix. Note that:
\\[ (AB)^{T}(AB) = B^{T}A^{T}(AB) = B^{T}B = I\\]
so that \\(AB\\) is an orthogonal matrix. The inverse of this operation comes from the fact
that:
\\[ A^{T} = A^{-1} \\]
so this set also fulfills the definition of a group with the additional property that its
operation is smooth. Thus, \\(O(n)\\) is a lie group!
