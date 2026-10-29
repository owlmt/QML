# Contributing

Thank you for considering a contribution to `owlmt/QML`. This document states the legal terms under
which contributions are accepted and the practical rules a contribution must follow. The licensing
structure it refers to is described in `LICENSING.md`; ownership is described in `COPYRIGHT.md`.

## 1. You keep your copyright

You retain the copyright in everything you contribute. Contributing to this repository does **not**
transfer or assign your copyright to the repository owner or to anyone else, and no contributor
licence agreement (CLA) is required.

## 2. Inbound licence: the same terms as the category

By submitting a contribution (a pull request, a patch, an issue attachment or any other form) you
license it to the repository owner and to every recipient of the repository under the licence that
`LICENSING.md` assigns to the category the contribution belongs to:

| Your contribution | Inbound licence | SPDX identifier |
|---|---|---|
| source code (scripts, `tools/`, notebook **code cells**) | GNU AGPL-3.0-only | `AGPL-3.0-only` |
| educational content (notebook **markdown cells**, documentation, original figures, exercises) | CC BY-NC-SA 4.0 | `CC-BY-NC-SA-4.0` |
| catalogue contributions (new or corrected rows in `manifest.csv`, `paper_index.csv`, the atlas CSVs) | CC BY 4.0 | `CC-BY-4.0` |

"Inbound = outbound": you grant exactly the licence under which the material is redistributed, no
more and no less. A contribution submitted under a different licence is not accepted unless its
licence is compatible and the pull request states it explicitly, in which case the file keeps the
contributor's notice and licence.

## 3. Developer Certificate of Origin (sign-off)

Every commit must carry a sign-off line certifying the Developer Certificate of Origin 1.1:

```
Signed-off-by: Your Name <your@email.example>
```

`git commit -s` adds the line. By signing off you certify the following:

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.
```

For this repository, "the open source license indicated in the file" means the licence that
`LICENSING.md` assigns to the contribution's category (section 2 above), including the Creative
Commons licences for non-code material.

## 4. Third-party rights are preserved

- Do not contribute code, text, figures or data that you do not have the right to license under the
  terms of section 2. Copying from a paper, from an authors' repository that has no licence or a
  restrictive one, or from a dataset's documentation is not acceptable unless the rights holder's
  terms allow it; say so in the pull request and keep the upstream notice.
- Third-party code that is included under a compatible licence (for example Apache-2.0, MIT,
  BSD-3-Clause or GPL-3.0 for code; CC BY 4.0 for text) must keep its original copyright notice and
  licence text, and the pull request must name the source and the licence. `LICENSING.md`,
  section 5.3, is updated to record it.
- Never commit paper PDFs, datasets, archives, credentials, tokens, checkpoints or large outputs;
  `.gitignore` excludes them and `tools/verify_notebook.py` rejects token-like strings. Notebooks
  download their data at run time and record the dataset's own licence.
- Never remove, weaken or relabel a third-party attribution or licence notice that a notebook
  carries.

## 5. Commercial licensing and your contribution

The repository owner reserves the right to offer separate commercial licences for the material he
owns (`LICENSING.md`, section 8). Because you keep the copyright in your contribution, that right
does **not** automatically extend to your contribution: the owner may commercially license your
contribution only if you agree to it separately. If you are willing to allow that, you may say so
in the pull request or in a separate written statement; if you say nothing, your contribution is
available only under the public licences of section 2. Future commercial licensing options
therefore remain open, subject always to who owns what.

## 6. Practical rules for notebooks and data

The scientific conventions are in `CLAUDE.md` and `tools/AGENT_BRIEF.md`. In short:

- one notebook per paper, filed in the paper's existing topic folder, named
  `<Method>_<Task>_<FirstAuthorYear>.ipynb`; never create new topic folders;
- every notebook downloads its own public data, fits every transform on the training split only,
  trains a classical baseline on identical inputs, ends with a claim-by-claim comparison with the
  paper, and contains the two mandatory sections "Dataset Exploration and Visualisation" and
  "Quantum Circuit Architecture" with executed outputs;
- the paper's `manifest.csv` row is updated in the same commit as the notebook
  (`tools/publish_notebook.py` does this and verifies the push);
- do not change executed outputs, metrics or reproduction statuses of existing notebooks except to
  correct an error, and explain the correction in the pull request and in `REPRODUCTION_LOG.md`.

## 7. How to submit

1. Fork the repository and create a branch.
2. Make your change; run `tools/verify_notebook.py` on any notebook you add or edit.
3. Commit with `git commit -s` (sign-off, section 3).
4. Open a pull request that states: what the change is, which category of `LICENSING.md` it falls
   under, and any third-party material it includes or depends on, with that material's licence.

Pull requests without a sign-off, or that include third-party material without its licence and
notice, are returned for correction.
