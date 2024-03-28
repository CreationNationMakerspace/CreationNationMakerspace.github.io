---
layout: presentation
title: On Comparing Adaptive Kaczmarz Methods (ATC)
permalink: /slides/test
order: 1
---

## On Comparing Adaptive Kaczmarz Methods


Jacob Moorman




-vertical-

In collaboration with

*Denali Molitor* and *Deanna Needell* of UCLA

and *Robert Gower* of Telecom-Paristech




-vertical-

Jacob was funded by NSF grant DGE-1829071

(The MENTOR NRT)

\\(
\def\range{\mathrm{Range}}
\def\eqdef{\overset{\mathrm{def}}{=}}
\def\sigi{\sigma\_i}
\def\sigmin{\sigma\_\min}
\def\sigmax{\sigma\_\max}
\def\t{\top}
\def\R{\mathbb{R}}
\def\P{\mathbb{P}}
\def\E{\mathbb{E}}
\def\Earg#1{\E\left[#1\right]}
\def\Ephiarg#1{\E\_\phi\left[#1\right]}
\def\Ephihatarg#1{\E\_{\hat\phi}\left[#1\right]}
\def\r{\mathbf{r}}
\def\rnext{\r^{k+1}}
\def\rcurr{\r^{k}}
\def\rexact{\r^\star}
\def\y{\mathbf{y}}
\def\x{\mathbf{x}}
\def\xinit{\x^{0}}
\def\xnext{\x^{k+1}}
\def\xcurr{\x^{k}}
\def\xexact{\x^{\star}}
\def\e{\mathbf{e}}
\def\einit{\xinit - \xexact}
\def\enext{\xnext - \xexact}
\def\ecurr{\xcurr - \xexact}
\def\ik{ {i\_k} }
\def\D{\mathbf{D}}
\def\A{\mathbf{A}}
\def\Ai{\A\_i}
\def\Ao{\A\_1}
\def\Am{\A\_m}
\def\Aik{\A\_\ik}
\def\pmat{\mathbf{P}}
\def\pmatik{\pmat\_\ik}
\def\bmat{\mathbf{Q}}
\def\bmatik{\bmat\_\ik}
\def\N{\mathbf{N}}
\def\Nk{\N\_k}
\def\B{\mathbf{B}}
\def\Binv{\B^{-1}}
\def\S{\mathbf{S}}
\def\Si{\S\_i}
\def\Hi{\mathbf{H}\_i}
\def\Sk{\S\_k}
\def\I{\mathbf{I}}
\def\W{\mathbf{W}}
\def\Wk{\W\_k}
\def\Z{\mathbf{Z}}
\def\Zk{\Z\_k}
\def\b{\mathbf{b}}
\def\bi{\b\_i}
\def\bik{\b\_\ik}
\def\Pk{\P\_k}
\def\Pik{ \P(\ik=i \mid \xcurr) }
\def\Pok{ \P(\ik=1 \mid \xcurr) }
\def\Pmk{ \P(\ik=m \mid \xcurr) }
\def\PSk{ \P(\Sk=\S \mid \xcurr) }
\def\argmin#1{\underset{#1}{\arg\min}}
\def\argmax#1{\underset{#1}{\arg\max}}
\def\proj#1{\underset{#1}{\text{proj}}}
\def\diag{\text{diag}}
\def\bproj#1{\underset{#1}{\text{proj}_\B}}
\def\norm#1{\left\lVert#1\right\rVert}
\def\bnorm#1{\left\lVert#1\right\rVert_B}
\def\abs#1{\left|#1\right|}
\def\trace#1{\mathbf{Tr}\left(#1\right)}
\def\innerprod#1#2{\langle #1 , #2 \rangle}
\\)

\\(
\def\d{\mathbf{d}}
\def\di{\d\_i}
\def\dj{\d\_j}
\def\dk{\d^k}
\def\dki{\dk\_i}
\def\dkj{\dk\_j}
\def\dkik{\dk\_\ik}
\def\r{\mathbf{r}}
\def\ri{\r\_i}
\def\rj{\r\_j}
\def\barr{\bar{\r}^k}
\def\barri{\barr\_i}
\def\barrj{\barr\_j}
\def\barrik{\barr\_\ik}
\def\barb{\bar{\mathbf{b}}}
\def\barbi{\barb\_i}
\def\barbik{\barb\_\ik}
\def\barA{\bar{\A}}
\def\barAi{\barA\_i}
\def\barAik{\barA\_\ik}
\def\lelr{\leq\_{\text{wr}}}
\def\sigphihat{\kappa\_{\hat \phi}(\A)}
\def\sigphi{\kappa\_\phi(\A)}
\def\sigphisq{\kappa\_\phi^{-2}(\A)}
\def\sigphihatsq{\kappa\_{\hat \phi}^{-2}(\A)}
\\)




-horizontal-

## Problem

Given \\(\A \in \R^{m \times n}\\) and \\(\b \in \R^m\\),

solve for \\(\xexact\\) satisfying \\(\A\xexact=\b\\)

such that \\(\xexact\\) has minimal norm.




-vertical-

## Notation

We will use an overbar to denote normalization by the row norms of \\(\A\\) using \\(\D \eqdef \diag(\norm{\A\_1}, \ldots, \norm{\A\_m})\\)

\\[\barb \eqdef \D^{-1} \b\\]
\\[\barA \eqdef \D^{-1} \A\\]




-horizontal-

## Kaczmarz Methods

Make an initial guess \\(\xinit \in \range(\A^\t)\\)

1. Select a row index \\(\ik \in [m]\\) by some **selection rule**

2. Update \\(\xnext = \argmin{\x \in \R^n} \norm{\x - \xcurr}\\) s.t. \\(\Aik \x = \bik\\)

3. Repeat until convergence




-vertical-

## Static Selection Rules

Row index \\(\ik\\) sampled i.i.d. at each iteration.

* \\(\Pik = p\_i\\)

* \\(\Pik = \norm{\Ai}^2/\norm{\A}_F^2\\)

* \\(\Pik = 1/m\\)




-vertical-

## Motivation for Adaptive Rules

Then the expected error update is

\\[\begin{align}
\Earg{\norm{\enext}^2 \mid \xcurr} &= \norm{\ecurr}^2 - \Earg{\norm{\xnext - \xcurr}^2\mid \xcurr}\\\\
&=\norm{\ecurr}^2 - \Earg{\dkik\mid \xcurr}
\end{align}\\]

where \\(\dki = \norm{\xnext - \xcurr}^2\\) under the selection \\(\ik=i\\).




-vertical-

## Adaptive Selection Rules

Choice of row index \\(\ik\\) depends on \\(\xcurr\\)

* **Max distance (MD)**: \\(\ik = \argmax{i}(\dki)\\)

* **Sampling MD**: \\(\ik = \argmax{i\in \tau\_k}(\dki)\\)

* \\(\Pik = \tfrac{\dki}{\sum\_j \dkj}\\)




-horizontal-

## Selection Rule Parameterization

A general way to parameterize the selection rule is

\\[\Pik = \frac{\phi\left(\dki; i, \dk \right)}{\sum\_j\phi\left(\dkj; j, \dk \right)}\\]

for some weighting function \\(\phi\\).




-vertical-

## Example Parameterizations

| <span style="font-weight:normal">\\(\phi(\abs{\r\_i}^2; i, \r)\\)</span> ||| Selection Rule |
|:---:|||:---:|
| \\(1\\) ||| Uniform sampling |
| \\(\norm{\A\_i}^2\\) ||| \\(\Pik = \norm{\Ai}^2/\norm{\A}_F^2\\) |
| \\(\mathbb{1}(\dki=\norm{\dk}\_\infty)\\) ||| Max distance rule |
| \\(\norm{\A\_i}^2\\)\\(\mathbb{1}(\dki\geq\theta\norm{\dk}\_\infty)\\) ||| A rule I made up |




-horizontal-

## Convergence

Given a selection rule parameterization \\(\phi\\),

there exists a rate constant \\(\sigphi\\) such that

\\[\Ephiarg{\norm{\ecurr}^2} \le (1 - \sigphisq)^k \norm{\einit}^2.\\]




-vertical-

## Convergence

Recalling the expected error update

\\[\begin{align}
& \Ephiarg{\norm{\enext}^2 \mid \xcurr} \\\\
&=\norm{\ecurr}^2 - \Ephiarg{\dkik\mid \xcurr} \\\\
&=\left(1 - \frac{\Ephiarg{\dkik\mid \xcurr}}{\norm{\ecurr}^2}\right)\norm{\ecurr}^2
\end{align}\\]




-vertical-

## Convergence

Thus, the smallest such rate constant \\(\sigphi\\) is

\\[\begin{align}
\sigphisq &= \min\_{\xcurr \in \range(\A^\t)}\left(\frac{\Ephiarg{\dkik\mid \xcurr}}{\norm{\ecurr}^2}\right).
\end{align}\\]

Though not obvious, this does not depend on \\(\xexact\\) or \\(k\\).

It depends only on \\(\A\\).




-horizontal-

## Convergence Results

Many papers present a selection rule and

compute or bound \\(\sigphi\\) for that rule.




-vertical-

| Selection Rule \\(\phi\\) || <span style="font-weight:normal">\\(\sigphisq\\)</span> | Paper |
|:---:||:---:|:---:|
| \\(\norm{\Ai}^2\\) || \\(= \frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)}\\) |  [SV09] |
| \\(\dki\\) || \\(\geq 2\frac{\sigmin^2(\barA)}{\sum\_i \sigi^2(\barA)}\\) | Soon |
| \\(\dki\mathbb{1}(\dki\geq ...)\\) || \\(\overset{\gt}{\approx} \frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)}\\) |  [BW18] |
| \\(\mathbb{1}(\dki=\norm{\dk}\_\infty)\\) || \\(= \underset{\e \in \range(\A^\t)}{\min} \left(\frac{\norm{\barA\e}\_\infty^2}{\norm{\e}^2}\right)\\) |  [NSLSKV16] |
| Sampling max distance || \\(\geq \frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)}\\) | [DHN17] |




-horizontal-

## Main Result

Suppose \\(\phi\\) and \\(\hat \phi\\) satisfy \\(\hat \phi \lelr \phi:\\)

\\[\hat \phi(\dj;\, j, \d)\phi(\di;\, i, \r) \le \phi(\dj;\, j, \r)\hat \phi(\di;\, i, \r)\\]

for any \\(\d\\) and any \\(i, j\\) with \\(\di \le \dj\\).

Then \\(\sigphihatsq \le \sigphisq\\).




-vertical-

## <span style="font-weight:normal">\\(\hat \phi \lelr \phi\\)</span> Explained

If \\(\hat\phi\\) and \\(\phi\\) were positive, we could write \\(\hat \phi \lelr \phi\\):

\\[\frac{\hat \phi(\dj; j, \d)}{\hat \phi(\di; i, \d)} \le \frac{\phi(\dj; j, \d)}{\phi(\di; i, \d)}.\\]

This basically says \\(\phi\\) grows faster than \\(\hat \phi\\)

\\[\frac{\hat \phi(b; \ldots)}{\hat \phi(a; \ldots)} \le \frac{\phi(b; \ldots)}{\phi(a; \ldots)}.\\]




-vertical-

## Implications

* Given two selection rules, we can determine which has a faster rate constant \\(\sigphi\\) without evaluating it.

* Max Distance rule has the fastest rate constant \\(\sigphi\\) possible, since \\(\phi \lelr \phi\_\infty\\) for any \\(\phi\\).

* Any monotonically increasing \\(\phi\\) yields a faster rate constant \\(\sigphi\\) than static sampling.




-vertical-

## Limitations

* Can't compare \\(\Ephihatarg{\norm{\ecurr}^2}\\) to \\(\Ephiarg{\norm{\ecurr}^2}\\)

* Not all \\(\hat \phi\\) and \\(\phi\\) are comparable by \\(\lelr\\)

* Does not give any measure of \\(\sigphisq - \sigphihatsq\\)




-horizontal-

## Future Work

* Wrap up the writing
* What can we say when \\(\hat \phi\\) and \\(\phi\\) are not comparable?
* Compare \\(\Ephiarg{\norm{\ecurr}^2}\\) and \\(\Ephihatarg{\norm{\ecurr}^2}\\)
* Extend to the inconsistent case




-vertical-

## References

<ul style="font-size:24px !important;">
  <li>
**[SV09]** T. Strohmer and R. Vershynin: *"A randomized Kaczmarz algorithm with exponential convergence"*, Journal of Fourier Analysis and Applications, 15 (2009), pp. 262–278.
  </li>
  <li>
**[GR15]** R. Gower and P. Richtarik: *"Randomized Iterative Methods for Linear Systems"*, SIAM Journal on Matrix Analysis and Applications (2015).
  </li>
  <li>
**[NSLSKV16]** J. Nutini, B. Sepehry, I. Laradji, M. Schmidt, H. Koepke, and A. Virani: *"Convergence rates for greedy Kaczmarz algorithms, and faster randomized Kaczmarz rules using the orthogonality graph"*, Proceedings of the Thirty-Second Conference on Uncertainty in Artificial Intelligence, pages 547–556. AUAI Press, 2016.
  </li>
  <li>
**[DHN17]** J.A. De Loera, J. Haddock, D. Needell: *"A sampling Kaczmarz–Motzkin algorithm for linear feasibility"*, SIAM Journal on Scientific Computing, 39(5), S66–S87 (2017).
  </li>
  <li>
**[BW18]** Z.-Z. Bai and W.-T. Wu: *"On greedy randomized Kaczmarz method for solving large sparse linear systems"*, SIAM Journal on Scientific Computing, vol. 40, no. 1, pp. A592–A606, 2018.
  </li>
</ul>




-horizontal-

# Appendix




-vertical-

## \\(\sigphisq\\) has no \\(\xexact\\) dependence

\\[\begin{align}
\frac{\Ephiarg{\dkik\mid \xcurr}}{\norm{\ecurr}^2} &= \frac{\Ephiarg{\abs{\barAik \xcurr - \barbik}^2\mid \xcurr}}{\norm{\ecurr}^2} \\\\
&= \frac{\Ephiarg{\abs{\barAik \left(\ecurr\right)}^2\mid \ecurr}}{\norm{\ecurr}^2} \\\\
&= \frac{\Ephiarg{\abs{\barAik \e}^2\mid \e}}{\norm{\e}^2}
\end{align}\\]




-vertical-

## Proof Sketch

\\[\begin{align}
&\hat \phi \lelr \phi \quad \\\\
&\implies \P\_{\hat \phi} \leq\_{\text{lr}} \P\_{\phi} & \text{(MLRP)} \\\\
&\implies \P\_{\hat \phi}\left(\di \geq t\right) \leq \P\_{\phi}\left(\di \geq t\right) \quad \forall t & \text{(FOSD)}\\\\
&\implies \E\_{\hat \phi}\left[\di\right] \leq \E\_{\phi}\left[\di\right]
\end{align}\\]

* MLRP: Monotone Likelihood Ratio Property
* FOSD: First Order Stochastic Dominance




-vertical-

## Sketch-project methods

Fix \\(\B \in \R^{n \times n}\\), symmetric positive definite.

1. Select \\(\Sk \in \R^{m \times \tau_k}\\) according to some **selection rule**

2. Let \\(\xnext = \argmin{\x\in\R^n} \norm{\x - \xcurr}_B\\) s.t. \\(\Sk^\t \A \x = \Sk^\t\b\\)

3. Repeat until convergence




-vertical-

## Sketch-project Residuals

The main result holds on all sketch-project methods where the sketching matrices are sampled from a finite set. The role of \\(\abs{\barri}^2\\) must be changed to \\(\norm{\b - \A \xcurr}^2\_{\Hi}\\), where \\(\Hi = \Si (\Si^\t \A \B^\dagger \A^\t \Si)^{\dagger} \Si^\t\\). Then, the main result holds directly.

This includes coordinate descent, block kaczmarz, and other methods as special cases.




-vertical-

## Experimental Results

<img style="margin:0;"  src="example.png" width="70%">




-horizontal-

## Selection Rules explained




-vertical-

## The original Randomized Kaczmarz [SV09]

\\[\Pik = \norm{\Ai}^2/\norm{\A}_F^2\\]

\\[\sigphisq = \frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)}\\]




-vertical-

## Max Distance [NSLSKV16]

\\[\ik = \argmax{i}\norm{\xnext - \xcurr} = \argmin{i}\norm{\xnext - \xexact}\\]

\\[\sigphisq = \min\_{\e \in \range(\A^\t)} \left(\frac{\norm{\barA\e}\_\infty^2}{\norm{\e}^2}\right)\\]




-vertical-

## Sampling Max Distance [DHN17]

Sample some row indices \\(\tau\_k \subset [m]\\),

then let \\(\ik = \argmax{i\in \tau\_k}\norm{\xnext - \xcurr}\\).

\\[\sigphisq \geq \frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)}\\]




-vertical-

## Greedy Randomized Kaczmarz [BW18]

\\(\Pik \propto \abs{\barri}^2\\) for

\\(\abs{\barri}^2 \geq \theta \norm{\barr}\_\infty^2 + (1-\theta)\frac{1}{m}\norm{\barr}^2\\),

and \\(\Pik = 0\\) otherwise.




-vertical-

## Greedy Randomized Kaczmarz [BW18]

\\[\begin{align}
\sigphisq &\geq \frac{1}{2}\left(\frac{\norm{\A}\_F^2}{\norm{\A}\_F^2 - \min\_i \norm{\Ai}^2} + 1\right)\frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)} \\\\
&=  \frac{1}{2}\left(2 - O\(m^{-1})\right)\frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)} \\\\
&\approx\frac{\sigmin^2(\A)}{\sum\_i \sigi^2(\A)}
\end{align}\\]