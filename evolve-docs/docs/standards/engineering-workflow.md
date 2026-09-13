# Evolve Engineering Workflow

## Purpose

Evolve needs a consistent way to plan, prioritise, deliver and improve work. The
workflow should provide enough discipline to make progress visible and
repeatable without introducing process that exists only to serve a team.

Evolve is a solo project. Practices that primarily coordinate multiple people
should therefore be treated as optional unless they provide a clear benefit to
planning, learning, quality or communication.

## Working Philosophies

The following philosophies were considered:

### Agile

Agile is an approach built around delivering valuable work in small increments,
responding to feedback and changing direction when new information becomes
available. Its principles favour working software, close feedback loops,
continuous improvement and collaboration over heavy up-front plans.

Agile is valuable for Evolve because it:

- makes progress visible through small, completed outcomes;
- allows priorities and plans to change as the project and its requirements
  become clearer;
- creates regular opportunities to inspect the work and improve the way of
  working;
- reduces the risk of spending a long time building the wrong thing; and
- supports learning as part of delivery rather than treating learning as a
  separate phase.

### Lean

Lean focuses on maximising value, reducing waste and improving flow, making it well suited to a solo project where finishing work before starting more work matters.

### Extreme Programming (XP)

XP focuses on engineering practices such as testing, simple design, continuous integration, refactoring and frequent releases, while collaboration practices have limited direct value for a solo project.

### Waterfall

Waterfall uses sequential phases and detailed up-front planning, making it a poor default for Evolve because the project is exploratory and requirements will change through learning and delivery.

## Selected Philosophy

Evolve will use **Agile** as its primary working philosophy

This is not an attempt to adopt every Agile practice. It is a commitment to
short feedback loops, incremental delivery, visible work, adaptation and
continuous improvement.

## Ways of Applying Agile

Agile can be applied through several different methods:

### Kanban

Kanban visualises work on a continuous-flow board, limits work in progress and
optimises the movement of issues from idea to completion. It has minimal
ceremony and is a strong fit for unplanned or continuously arriving work.

### Scrum

Scrum organises work into fixed-length sprints. A sprint provides a planning
point, a short delivery goal, a review of the result and a retrospective to
improve the next sprint. Scrum also gives work a predictable cadence without
requiring a detailed long-term plan.

### Scrumban

Scrumban combines Scrum's planning cadence with Kanban's flow visualisation and
work-in-progress limits. It can be useful when a team needs both regular
planning and flexibility during execution.

## Selected Method

Evolve will use **Scrumban**, adapted for a solo project.

The main reason is that sprints provide a clear and repeatable structure for
planning, delivering and reflecting. There is also a deliberately cheeky
secondary benefit: Scrumban gives the journey useful boundaries for public
communication. Sprint names and numbers make good LinkedIn post titles, and
retrospectives can be shared as a record of what was learned and improved.
This should not override engineering priorities, but it is a legitimate
motivation because communicating the journey encourages reflection and
accountability.

Evolve will not introduce roles, meetings or artefacts merely to imitate a
Scrum team. The process is a lightweight solo adaptation.

## Workflow

### 1. Plan

1. Capture work as a GitHub issue using Evolve's lightweight, outcome-driven
   issue format.
2. Assign every issue to a milestone. A milestone represents the larger goal
   that the issue contributes to, so no issue is disconnected from a project
   outcome.
3. Prioritise eligible issues before sprint planning.
4. At the start of a sprint, select a small set of issues that supports one
   clear sprint goal.
5. Add the selected issues to the sprint in GitHub Projects.

The sprint plan is a forecast, not a promise to complete an arbitrary volume of
work. Scope can be adjusted when new information makes the original plan
invalid.

### 2. Progress

Issues move through the GitHub Projects workflow:

`Backlog` -> `Ready` -> `In Progress` -> `Review` -> `Done`

- **Backlog**: identified work that is not yet ready or prioritised.
- **Ready**: prioritised work with a clear goal and acceptance conditions.
- **In Progress**: actively being implemented or investigated.
- **Review**: implementation is complete and is waiting for the review period.
- **Done**: reviewed, complete and ready to be considered delivered.

Work in progress should be kept small. Finish or review existing work before
starting additional work whenever practical.

### 3. Review

When implementation is complete, move the issue to **Review** and record any
relevant evidence, such as tests, screenshots or links.

Because Evolve is a one-person project, there must be a **minimum 24-hour
waiting period** between moving an issue into Review and reviewing it. This
creates distance from the implementation and gives the same person enough time
to look at the issue with a clearer perspective.

The review should check:

- the issue's goal and done conditions;
- the implementation and its surrounding behaviour;
- relevant tests and documentation; and
- whether the change introduces follow-up work.

If the issue does not meet the standard, return it to In Progress with the
remaining work recorded. If it meets the standard, move it to Done.

### 4. Complete

An issue is complete only after it has passed the review period and review. The
issue should remain linked to its milestone and sprint so that delivery can be
traced back to the larger goal and the sprint in which it was completed.

At the end of a sprint:

1. confirm which issues were completed;
2. move incomplete issues back to the backlog or into the next sprint based on
   their current priority;
3. review the sprint outcome against its goal; and
4. hold a short retrospective.

## Retrospectives and Continuous Improvement

Each sprint should end with a retrospective covering:

- what went well;
- what did not go well;
- what was learned; and
- one or two specific changes to try in the next sprint.

Retrospective notes can be recorded in the project journal and shared publicly
when useful. The workflow or standards themselves should be changed only when experience shows
that a change will improve delivery, quality or learning.

## GitHub Projects Configuration

GitHub Projects should support this workflow with:

- a board view containing `Backlog`, `Ready`, `In Progress`, `Review` and
  `Done` statuses;
- sprint iterations with a fixed, documented duration;
- fields for priority, milestone and sprint;
- issue links that preserve the relationship between project work and its
  larger goal; and
- views or filters for the current sprint, unassigned issues and issues
  waiting for review.

Every issue must have a milestone before it is considered Ready. The board is
the source of truth for current work status, while the issue remains the source
of truth for context, scope and completion conditions.