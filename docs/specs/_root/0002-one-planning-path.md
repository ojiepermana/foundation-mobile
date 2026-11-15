# 0002. One planning path: a scope row first, then a spec

**Date**: 2026-11-15
**Status**: Accepted

## Summary

Planning a new capability now has one path. You add a row to the scope (`docs/scope/`, the list of what to build and its status), then you write a spec (`docs/specs/`, the design and decision record) before code. The old planning guide under `docs/plans/` is removed, and a spec replaces the ADR (architecture decision record) as the record the rules ask for. The change is documents plus one list in the validator script.

## Context

> ⚠️ Premise note: The easy way to fix two planning paths is to write a third document that explains both. That leaves three doors. This change has to remove more than it adds: one folder goes, one record kind stops growing, and no new rule file appears.

The repository names four homes for planning and decision records:

| Home | What it holds today | Who points at it |
| --- | --- | --- |
| `docs/plans/` | One guide (`README.md`) that asks for a PRD (product brief) and a plan per capability. No plan has been written. | `AGENTS.md`, `docs/rules/development-rules.md`, `docs/architecture/overview.md`, the validator |
| `docs/decisions/` | `ADR-0001-foundation.md` | `README.md`, the overview, the validator |
| `docs/scope/` | The live tracker: an index, three workspaces, twelve rows | Nothing outside the folder |
| `docs/specs/` | Spec `0001` | Nothing outside the folder |

The forces at play:

- **Practice and rules disagree.** Every piece of planning since the foundation commit went into the scope and a spec. The rules still send a reader to `docs/plans/`.
- **Agents act on what `AGENTS.md` links.** An agent asked to plan the next capability follows the link, finds the guide, and writes a PRD in a folder nobody reads.
- **Two record kinds hold the same content.** An ADR and a spec both carry context, options, a decision and consequences. Each new decision would first need a call on which kind it is.
- **Deferred work is listed twice.** The guide and the scope index name the same areas in different words (authentication and accounts, transport clients and backend clients, flag engines and remote flags). Two lists drift.
- **The validator guards the wrong file.** `check-architecture.py` requires `docs/plans/README.md` and does not know the scope index exists.
- **One maintainer.** Anything a machine does not check rests on one person, so the path has to be short enough to hold in the head.
- **The scope files are kept by a command.** `/scope` rewrites them, so wording placed there can change without a review of the rule.

Without a decision, the first product feature would be planned in whichever place its author found first.

## Options considered

### Option 1: Scope row first, then a spec, in one change

The scope is where a capability is planned and tracked. A spec is the design and the decision record. `docs/plans/` is deleted, ADR 0001 stays as the founding record, and every pointer moves in the same change.

**Pros**:
- Matches what already happens, so nothing has to be learned.
- One record kind going forward. No call on ADR or spec.
- Removes a folder and a list. Adds no rule file.

**Cons**:
- The usual way to write both files is a pair of commands (`/scope`, `/architect`) that live outside this repository.
- Four links and one validator entry change at once. A missed link is a dead link.

### Option 2: The plans folder is the path

`docs/plans/` stays the place to plan, with a PRD and a plan per capability. The scope shrinks to a status tracker that links to each plan.

**Pros**:
- No pointer changes. The rules are already written this way.
- A plan file per capability is a familiar habit.

**Cons**:
- Nothing writes to `docs/plans/`. Every plan would be written by hand while the scope and specs are kept by commands.
- A plan and a spec would describe the same capability twice.

### Option 3: Keep every home, with a written split

The scope says what to build, a plan says how, an ADR records architecture decisions and a spec records feature designs.

**Pros**:
- Nothing is deleted. Each habit keeps its folder.

**Cons**:
- Four borders to explain and keep in step, for one maintainer and one greeting.
- Every new document starts with the question of which folder it belongs in.

## Decision

**Chosen option**: Option 1: Scope row first, then a spec, in one change.

A new capability is planned as a row in `docs/scope/`, designed in a spec under `docs/specs/` before code, and `docs/plans/` and new ADRs are retired in a single change.

## Rationale

Practice already chose. Six shared rows, both app workspaces and spec `0001` were written on this path, and no plan was ever written under `docs/plans/`. Moving the rules to match costs a handful of sentence edits. Moving practice to match the rules (Option 2) would mean hand writing files that no command keeps current, which one maintainer will not sustain.

The same reasoning settles the record kind. A spec carries everything an ADR does, plus the design. Keeping both (Option 3) adds a sorting step to every decision and a second folder to check, with no reader who needs the difference.

The calls made inside the chosen option, each confirmed with the engineer unless marked as a recommendation:

- **Delete the guide, do not leave a pointer.** A pointer file is still a second door, and the validator would keep requiring it.
- **The rule lives in `docs/rules/development-rules.md`.** That file already owns the sentence about plans and ADRs. The scope index was the runner up, and it lost because `/scope` rewrites it.
- **Files first, commands noted.** The rule names folders and what each file holds, then says which commands usually write them. A contributor without those commands can still follow the path.
- **Triggers stay with their owners.** The service rules, the dependency rules and the quality checks each keep their own trigger sentence. Only the word for the record changes. Gathering them into one list would create the second copy that spec `0001` forbids.
- **Decide first, always.** A new capability or a trigger change has a spec before code reaches `main`. Building first on an assumed decision is not used here.
- **The scope is the brief.** The user outcome and the done when line in a row (or a new workspace for a large area) are the product brief. No PRD file exists to drift from it.
- **ADR 0001 is not reworded.** An accepted record keeps its text. Only its status line changes, and only if a later spec replaces it.
- **Results go where they already live.** Progress sits in the scope row, what ran sits in `docs/quality/verification.md`.
- **No backfill.** Shipped capabilities get a spec only when a later change to them is a new capability or hits a trigger.
- **Recommendation: relabel the ownership matrix row** from `Architecture, ADRs and agent workflow` to `Architecture, decision records, scope and agent workflow`. Leaving it was the runner up, and it would keep the one word that sends a reader looking for ADR files.
- **Recommendation: spec `0001` is brought in step in the same change.** Its own premise note says a rule file changes first and the matching row follows in the same change. Waiting for a later pass was the runner up, and it would leave an accepted spec quoting a rule that no longer exists.
- **Recommendation: name no folder before it has a file.** `docs/reviews/` and similar are added to the repository structure when their first file lands, in line with real caller first.

## Standard definition

**Canonical pattern**:

```text
A new capability
  1. docs/scope/<workspace>/NNN - Name.md     add a row. It states the user outcome
                                              and a done when line. This is the brief.
                                              Usual way: /scope
  2. docs/specs/<workspace>/NNNN-title.md     write the spec before code.
                                              Usual way: /architect
  3. build one slice through its real caller
  4. progress  -> the scope row (status and open boxes)
     what ran  -> docs/quality/verification.md

A smaller change inside an existing capability
  needs a spec only when it changes ownership, a contract or a dependency.
  The trigger wording stays in its owner file:
    docs/rules/service-rules.md               a new crate or a moved ownership boundary
    docs/architecture/dependency-rules.md     a new dependency edge
    docs/quality/architecture-compliance.md   a new dependency or a material change
    docs/contracts/ffi-conventions.md         a breaking contract (the Compatibility row)
    docs/decisions/ADR-0001-foundation.md     Revisit when (a changed dependency direction,
                                              an async call across the bridge, clients
                                              versioned apart, a new shared crate or service)
  Everything else goes straight to code.

Deferred product work
  listed once, in the Deferred section of docs/scope/index.md
```

What a spec for a new capability covers (moved from the old guide, unchanged in meaning): the user outcome, scope, acceptance criteria, existing owner, public contract, dependency direction, platform specific work and a verification matrix. It names existing behavior or assets to reuse and justifies each proposed crate, service or framework.

Record keeping:

| Question | Answer |
| --- | --- |
| Where specs live | `docs/specs/<workspace>/`, where the workspace mirrors the scope (`_root`, `ios`, `android`) |
| How specs are named | `NNNN-kebab-title.md`, numbered per folder from `0001` |
| How scope rows are named | As the legend in `docs/scope/index.md` says. That file owns the wording. |
| Is a spec the record the rules ask for | Yes. Wherever a rule asked for an ADR or a plan, it now asks for a spec. |
| How a spec is replaced | The new spec is written, and the old one gets `**Status**: Superseded by [NNNN](NNNN-title.md)` |
| How ADR 0001 is replaced | Only its status line changes, to `Superseded by` with a link to the spec. Its text stays. |
| When an accepted record may be edited in place | Only a spec that mirrors rule files, which today is spec `0001`. It is amended in the same change as the rule, as its own premise note says. Every other accepted record is superseded, never reworded. |
| Who sets a spec's status | `/architect` writes `Proposed`. `/develop` moves it to `In Progress` and then `Accepted` as the scope row moves. |
| Do new specs or rows join the validator list | No. Only `docs/scope/index.md` is required. |
| Who approves a spec | The maintainer, as in spec `0001` |
| Follow-up lists inside a spec | Notes on that spec. Work that becomes real gets a scope row. |

**Replaces**:

- A PRD or a plan file under `docs/plans/`
- A new ADR file under `docs/decisions/`
- A list of deferred product work anywhere but `docs/scope/index.md`
- Code for a new capability, or a trigger change, that lands before its spec
- The words `plan` and `ADR` in a rule as the name of the record to write

**Enforcement**:

- `tooling/validation/check-architecture.py`, run by `scripts/test.sh` and the `foundation` job. In `REQUIRED_DOCS`, remove the entry `"plans": ["README"]` and add `"scope": ["index"]`. The script then fails with `Missing or empty document: docs/scope/index.md` when the landing page is gone. The entry `"decisions": ["ADR-0001-foundation"]` stays.
- The validator still fails on a new workspace crate or Cargo dependency until the policy changes, which forces the trigger case into view (unchanged from spec `0001`, rule R10).
- Everything else rests on review: whether a new capability has a row and a spec, whether the spec came before the code, and whether the spec covers the checklist. A machine cannot judge those.

**Rollout**:

One change, applied in this order so the checks never point at a missing file. Each replacement text is given in full.

1. `docs/rules/development-rules.md`. Replace the last paragraph (`Use a [plan]... consequences.`) with:

   ```markdown
   Plan a new capability in the [scope](../scope/index.md). Add a row to the owning workspace and treat it as the brief: it states the user outcome and a done when line. Then write a spec under `docs/specs/` before code. A smaller change needs a spec only when it changes ownership, a contract or a dependency. The [service rules](service-rules.md), the [dependency rules](../architecture/dependency-rules.md), the [FFI conventions](../contracts/ffi-conventions.md), the [quality checks](../quality/architecture-compliance.md) and the Revisit when list in the [foundation decision](../decisions/ADR-0001-foundation.md) name those triggers. `/scope` and `/architect` are the usual way to write both files.

   A spec for a new capability covers the user outcome, scope, acceptance criteria, existing owner, public contract, dependency direction, platform specific work and a verification matrix. It names existing behavior or assets to reuse and justifies each proposed crate, service or framework. Specs are numbered `NNNN-kebab-title.md` in the folder that mirrors the scope workspace. A spec that replaces an earlier record marks that record as superseded. The foundation decision is the founding record and stays in `docs/decisions/`.

   Record progress in the scope row and what ran in the [verification record](../quality/verification.md).
   ```

2. `AGENTS.md`, the fourth bullet under During implementation. Replace the sentence `Add a plan for a new capability and an ADR for a material ownership, contract or dependency decision.` with:

   ```markdown
   Plan a new capability in the [scope](docs/scope/index.md) and write its spec under `docs/specs/` before code. A material ownership, contract or dependency decision also needs a spec. The [development rules](docs/rules/development-rules.md) describe the path.
   ```

3. `docs/architecture/overview.md`. Replace `For a new capability, follow the [extension procedure](../plans/README.md).` with:

   ```markdown
   For a new capability, start in the [scope](../scope/index.md) and follow the [development rules](../rules/development-rules.md).
   ```

4. `docs/architecture/repository-structure.md`. Replace the `docs/` row with:

   ```markdown
   | `docs/` | Architecture, rules, design system, contracts and quality. `docs/scope/` lists what to build and its status. `docs/specs/` holds design and decision records. `docs/decisions/` holds the founding decision. |
   ```

5. `README.md`. In the same paragraph, directly after the sentence that ends `[foundation decision](docs/decisions/ADR-0001-foundation.md).` and before `Contributors should read`, add:

   ```markdown
   The [scope](docs/scope/index.md) lists what is built and what is next.
   ```

6. `docs/rules/service-rules.md`. Replace `record the trade-off in an ADR.` with ``record the trade-off in a spec under `docs/specs/`.``
7. `docs/quality/architecture-compliance.md`. Replace `needs an ADR and a corresponding policy update` with ``needs a spec under `docs/specs/` and a corresponding policy update``. The table row that says the script checks every planning and decision document stays as written (the scope index is the planning document, ADR 0001 the decision document).
8. `docs/architecture/ownership-matrix.md`. Relabel the last row to `Architecture, decision records, scope and agent workflow`. Owner and consumers stay.
9. `tooling/validation/check-architecture.py`. Change `REQUIRED_DOCS` as described under Enforcement.
10. Delete `docs/plans/README.md`. The folder goes with it.
11. `docs/scope/index.md`. In the last paragraph of Deferred, replace `need their own product brief and scope` with `each need their own scope before work starts`. This is the only rule wording that changes in the scope index. The list of areas stays, and it is now the only list.
12. `docs/scope/_root/007 - One planning path.md`. Replace the paragraph that starts `You can read the agent instructions` with the text below, and in the Done when line delete `[Planning guide](../../plans/README.md) · `.

    ```markdown
    You can read the agent instructions and land on one place to plan the next capability. Before this change the planning guide under `docs/plans/` asked for a product brief and a plan, while this scope tracked features under `docs/scope/`. The agent instructions, the development rules and the architecture overview all pointed to that guide, and nothing outside this folder pointed to the scope.
    ```

13. `docs/scope/_root/001 - Ownership and development rules.md`. Delete the closing paragraph (`The rules send a new capability to the planning guide and do not mention this scope yet. That gap is planned in [007](...)`). It is no longer true.
14. `docs/specs/_root/0001-ownership-development-rules.md`. Amend exactly these places and nothing else:
    - Row R10, the Rule cell only: `A new capability needs a scope row and a spec. A material ownership, contract or dependency decision needs a spec, with the affected architecture documents updated in the same change.` The Owner file and Enforced by cells stay.
    - The sentence `When R10 asks for an ADR.` becomes `When R10 asks for a spec.` The four bullets under it stay, including the one that names `ADR-0001` as a trigger owner.
    - Under Consequences, Neutral: `will trigger R10 and a new ADR` becomes `will trigger R10 and a new spec`.
    - Under Follow-up, the three items that start `R10 sends a new capability to`, `This spec opens` and `Record keeping that no file settles yet`: change `- [ ]` to `- [x]` and append ` Settled by [0002](0002-one-planning-path.md).`
15. Regenerate the knowledge graph after every edit above (usual way: `/graphify`) and commit the tracked outputs under `graphify-out/` in the same change. The graph still describes the old guide and the ADR rule, and agents read it first.

Files that do not change: `docs/decisions/ADR-0001-foundation.md`, and `docs/architecture/dependency-rules.md`. Its sentence `Update the policy check with the architecture decision when an edge changes` names the decision, not a kind of file, so it reads correctly as a spec.

Row `007` progress is not a rollout step. `/architect` links this spec and ticks the design box when the spec is accepted. `/develop` moves the row's status, and the counts in `docs/scope/_root/scope.md` and `docs/scope/index.md`, when the row is built and verified.

The change is complete when all of these hold. Run each from the repository root.

- `python3 tooling/validation/check-architecture.py` passes, and fails with `Missing or empty document: docs/scope/index.md` when that file is moved away for a moment.
- `scripts/test.sh` passes.
- `test ! -e docs/plans` succeeds.
- No link to the old guide is left outside the specs. This prints nothing:

  ```sh
  grep -rn "plans/README" AGENTS.md README.md docs tooling scripts --exclude-dir=specs
  ```

- No rule asks for an ADR. Every remaining mention is the file name of ADR 0001 inside a link, so this prints nothing:

  ```sh
  grep -rn "ADR" AGENTS.md README.md docs --exclude-dir=specs --exclude-dir=decisions | grep -v "ADR-0001-foundation.md"
  ```

- No rule asks for a plan or a PRD. This prints one line only, the history sentence in scope row `007`:

  ```sh
  grep -rniE "PRD|product brief|a plan( |\.|,)" AGENTS.md README.md docs --exclude-dir=specs --exclude-dir=decisions
  ```

- Deferred product work has one list. This prints `docs/scope/index.md` and nothing else:

  ```sh
  grep -rl "background transfers" AGENTS.md README.md docs --exclude-dir=specs
  ```

- `AGENTS.md` and `docs/architecture/repository-structure.md` both name the new homes. Each of these prints a count of 1 or more for both files:

  ```sh
  grep -c "docs/scope" AGENTS.md docs/architecture/repository-structure.md
  grep -c "docs/specs" AGENTS.md docs/architecture/repository-structure.md
  ```

- Every relative Markdown link resolves. This one off check (not added to the repository) prints `all links resolve`:

  ```sh
  python3 - <<'EOF'
  import pathlib, re, urllib.parse
  files = [*pathlib.Path("docs").rglob("*.md"), pathlib.Path("AGENTS.md"), pathlib.Path("README.md")]
  bad = []
  for f in files:
      text = re.sub(r"```.*?```", "", f.read_text(encoding="utf-8"), flags=re.S)
      text = re.sub(r"`[^`\n]*`", "", text)
      for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
          if "://" in target:
              continue
          if not (f.parent / urllib.parse.unquote(target)).exists():
              bad.append(f"{f}: {target}")
  print("\n".join(bad) or "all links resolve")
  EOF
  ```

- After step 15, `graphify-out/graph.json` has no node whose source file is `docs/plans/README.md`. The checks above leave `graphify-out/` out because it is derived.

**Exceptions**:

- `docs/decisions/ADR-0001-foundation.md` stays as written and stays required by the validator. It still says `feature plan`. Read that as a scope row and a spec.
- Specs may name `docs/plans/` and ADRs when they record history, as this one and spec `0001` do.
- A change that is not a new capability and hits no trigger needs neither a row nor a spec.
- Capabilities that shipped before this change need no spec until a later change to them is a new capability or hits a trigger.

## Consequences

**Positive**:

- A reader or agent goes from `AGENTS.md` to the scope index in one step, and from there to any row or spec.
- One record kind. A decision is always a spec, so nobody has to choose a folder.
- Deferred product work has one list, so it cannot drift.
- The validator guards the landing page that is in use, and no longer requires a guide nobody followed.
- Net result is one folder fewer and no new rule file.

**Negative / tradeoffs**:

- The usual tools for the path (`/scope`, `/architect`) are not part of this repository. A contributor without them writes both files by hand, with only the checklist in the development rules as a guide to their shape.
- The scope files are rewritten by a command. The landing page can change shape without a rule change, and the validator checks only that it exists and is not empty.
- Whether a capability has a row and a spec, and whether the spec came first, rests on review by one person. Nothing fails if code lands first.
- `/develop` can still offer to build first on an assumed decision. This repository says no, and nothing mechanical stops a yes.
- `docs/decisions/` stays as a folder with one file that will never get a sibling. A new reader may look for ADR 0002.
- Outside links to `docs/plans/README.md` (a bookmark, an old commit message) stop working.

**Neutral**:

- The first product feature that needs a record, a typed error or an async call across the bridge now produces a spec where spec `0001` expected an ADR.
- Spec status follows the scope row: `Proposed` when written, `In Progress` while built, `Accepted` when the row is done.

## Follow-up

- [ ] Nothing checks that the files linked from `docs/scope/index.md` exist. A link check in `check-architecture.py` becomes worth adding when a broken tracker link first costs time.
- [ ] Record where `/scope` and `/architect` come from when a second contributor joins, so the usual way is open to them. Spec `0001` already plans named reviewers for that moment.
- [ ] `/scope` rewrites `docs/scope/index.md`. A later run could bring back the `product brief` wording or a second deferred list. Check the Deferred paragraph after each `/scope` run until a link or wording check exists.
- [ ] `docs/decisions/` will hold one file. If a reader goes looking for ADR 0002, the development rules already say where decisions go. Revisit only if that proves not to be enough.
- [ ] The knowledge graph under `graphify-out/` is a derived copy of these rules and nothing checks that it is current. Regenerate it in any change that moves or deletes a governing document.
- [ ] Add `docs/reviews/` (and any other new record folder) to `docs/architecture/repository-structure.md` when its first file lands.
- [ ] If the checks are ever required before a change reaches `main` (open in spec `0001`), consider whether a new capability without a spec can be caught there.
