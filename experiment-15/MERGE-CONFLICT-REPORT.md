# Experiment 15 - Working with Git Branches and Resolving Merge Conflicts

**Repository:** `tharuncoder676/Slot-A-SOFTWARE-ENGINEERING`
**Feature branch:** `feature/experiment-15`
**Base branch:** `main`

---

## Aim

To demonstrate the collaborative Git workflow: cloning a shared repository,
branching, committing, pushing, keeping a feature branch up to date with
`main`, and resolving merge conflicts that arise when two developers change
the same lines of the same files.

---

## Scenario

Two developers work on `experiment-15/calculator.py` at the same time:

| | Developer A (this feature branch) | Developer B (teammate, merged to `main`) |
|---|---|---|
| New function | `multiply(a, b)` | `power(a, b)` |
| Divide-by-zero fix | `raise ValueError(...)` | print a warning and `return None` |
| Module description | `"Calculator v2.0 - ... multiply support"` | `"Calculator v1.1 - ... safe division"` |

Because both developers edited the **same regions** of the same two files, Git
could not auto-merge and reported a conflict.

---

## Steps Performed

### 1. Clone the shared repository

```bash
git clone https://github.com/tharuncoder676/Slot-A-SOFTWARE-ENGINEERING.git
cd Slot-A-SOFTWARE-ENGINEERING
```

### 2. Create a new branch and switch to it

```bash
git checkout -b feature/experiment-15
```

`git branch` confirms the active branch:

```
* feature/experiment-15
  main
```

### 3. Make changes to the files

On the feature branch, `experiment-15/calculator.py` was edited to add a
`multiply()` function and to guard `divide()` against a zero divisor:

```python
def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

`experiment-15/README.md` was updated to describe the change.

### 4. Commit the changes

```bash
git add experiment-15
git commit -m "Add multiply() and guard divide() against zero divisor"
```

### 5. Push the branch to the remote

```bash
git push -u origin feature/experiment-15
```

### 6. Pull the latest changes from `main`

Meanwhile the teammate's work had landed on `main`, so before merging:

```bash
git checkout main
git pull origin main
```

### 7. Switch back to the feature branch

```bash
git checkout feature/experiment-15
```

### 8. Merge `main` into the feature branch

```bash
git merge main
```

Git reported the conflict:

```
Auto-merging experiment-15/README.md
CONFLICT (content): Merge conflict in experiment-15/README.md
Auto-merging experiment-15/calculator.py
CONFLICT (content): Merge conflict in experiment-15/calculator.py
Automatic merge failed; fix conflicts and then commit the result.
```

`git status --short` showed both files as unmerged (`UU`):

```
UU experiment-15/README.md
UU experiment-15/calculator.py
```

---

## Conflicts Encountered

Git inserted conflict markers into both files. Everything between `<<<<<<< HEAD`
and `=======` is the version on the current (feature) branch; everything between
`=======` and `>>>>>>> main` is the version coming from `main`.

**Five conflict hunks in total — four in `calculator.py`, one in `README.md`.**

### Conflict 1 — new function added in the same place

```python
<<<<<<< HEAD
def multiply(a, b):
    return a * b
=======
def power(a, b):
    return a ** b
>>>>>>> main
```

### Conflict 2 — two different divide-by-zero strategies

```python
def divide(a, b):
    if b == 0:
<<<<<<< HEAD
        raise ValueError("Cannot divide by zero")
=======
        print("Warning: division by zero, returning None")
        return None
>>>>>>> main
    return a / b
```

### Conflict 3 — the version string in `describe()`

```python
<<<<<<< HEAD
    return "Calculator v2.0 - arithmetic operations with multiply support"
=======
    return "Calculator v1.1 - basic arithmetic with safe division"
>>>>>>> main
```

### Conflict 4 — the demo block in `__main__`

```python
<<<<<<< HEAD
    print("6 * 5 =", multiply(6, 5))
=======
    print("2 ^ 5 =", power(2, 5))
>>>>>>> main
```

### Conflict 5 — the `## Status` section of `README.md`

```markdown
<<<<<<< HEAD
Feature branch `feature/experiment-15`: added a `multiply()` function and
made `divide()` raise a `ValueError` when the divisor is zero.
=======
Main branch: teammate added a `power()` function and made `divide()` print a
warning and return `None` when the divisor is zero.
>>>>>>> main
```

---

## How the Conflicts Were Resolved

Each file was opened in the editor and the conflict markers were removed by
hand, deciding case by case rather than blindly taking one side.

| # | Conflict | Resolution | Reasoning |
|---|---|---|---|
| 1 | `multiply()` vs `power()` | **Kept both** | The two functions are independent additions. They only conflicted because they were written at the same line position, not because they disagree. |
| 2 | `raise ValueError` vs `return None` | **Kept `raise ValueError`** | Returning `None` silently lets an invalid result flow into later calculations, where it fails far from the real cause. Raising fails loudly at the point of the error. |
| 3 | Version string | **Wrote a new combined line** — `"Calculator v2.0 - arithmetic with multiply, power and safe division"` | Neither side was correct after the merge, since the merged module now has *both* new functions. |
| 4 | Demo `print` lines | **Kept both** | Both functions exist after the merge, so both should be demonstrated. |
| 5 | `README.md` status | **Rewrote to describe the merged result** | The status must describe the combined state of the branch, not either side alone. |

Conflicts 1, 4 and 5 are the common "both sides are right" case. Conflict 2 was
a genuine design disagreement that required an actual decision. Conflict 3 shows
that a resolution is sometimes **neither** side — new text has to be written.

### 9. Mark the conflicts as resolved

After editing, the files were checked for leftover markers and staged. Staging
a conflicted file is what tells Git the conflict is resolved:

```bash
grep -rn "<<<<<<<\|>>>>>>>" experiment-15/   # confirm no markers remain
python experiment-15/calculator.py           # confirm the merged code runs
git add experiment-15/calculator.py experiment-15/README.md
```

`git status` then reported all conflicts fixed.

### 10. Commit the resolved merge

```bash
git commit -m "Merge main into feature/experiment-15 and resolve conflicts"
```

### 11. Push and open a pull request

```bash
git push origin feature/experiment-15
gh pr create --base main --head feature/experiment-15
```

---

## Verification

The merged module runs correctly with both contributions present:

```
Calculator v2.0 - arithmetic with multiply, power and safe division
2 + 3 = 5
7 - 4 = 3
6 * 5 = 30
2 ^ 5 = 32
8 / 2 = 4.0
```

---

## Useful Commands Reference

| Command | Purpose |
|---|---|
| `git clone <url>` | Copy a remote repository locally |
| `git checkout -b <branch>` | Create a branch and switch to it |
| `git branch` | List branches, `*` marks the current one |
| `git push -u origin <branch>` | Push a branch and set its upstream |
| `git pull origin main` | Fetch and merge the latest `main` |
| `git merge main` | Merge `main` into the current branch |
| `git status --short` | `UU` marks unmerged (conflicted) files |
| `git diff` | Show the conflicting hunks during a merge |
| `git add <file>` | Mark a conflicted file as resolved |
| `git merge --abort` | Cancel the merge and return to the pre-merge state |
| `git log --graph --oneline` | View the branch and merge history |

---

## Conclusion

Merge conflicts are not errors — they are Git refusing to guess when two people
change the same lines. Git can only report *where* the disagreement is; deciding
*what the code should be* is the developer's job. Keeping a feature branch merged
up to date with `main` frequently keeps each conflict small and easy to reason
about, which is why `git pull` before merging is part of the routine.
