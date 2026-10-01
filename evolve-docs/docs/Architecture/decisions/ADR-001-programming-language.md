# ADR-001: Programming Language

## Status

Accepted

## Context

Evolve requires programming languages for both frontend and backend development.

The purpose of Evolve is not to focus on learning a particular language, but to develop broader software engineering skills through designing, building, testing, deploying, securing and continuously improving a real application.

The initial languages should therefore allow development to begin quickly while remaining widely used in industry. Other languages can be introduced as Evolve grows.

## Options Considered

### Python

Already familiar, widely used in industry and well suited to backend development. Allows the focus to remain on software engineering rather than learning a new language.

### JavaScript

Widely used for web development, with some previous experience already gained through React and JSX.

### TypeScript

Adds static typing to JavaScript but introduces additional complexity that is not currently necessary for Evolve.

### Java

Widely used for backend and enterprise software engineering, but would require learning a new language and ecosystem.

### Go

Highly relevant to cloud-native and platform engineering, but would also require learning a new language before development begins.

## Decision

Evolve will initially use:

**Frontend: JavaScript with React**

**Backend: Python**

These are starting technologies, not permanent restrictions. Other languages can be introduced as Evolve develops.

## Rationale

The focus of Evolve is developing software engineering skills rather than learning programming languages.

Python allows backend development to begin with an already familiar language, while JavaScript and React provide a practical and industry-relevant frontend stack.

This allows more time to focus on areas such as architecture, APIs, databases, testing, security and application design.

## Consequences

Development can begin using mostly familiar technologies.

Evolve will initially not benefit from TypeScript's static typing.

Other languages such as Go, Java or TypeScript can be introduced later where there is a clear technical or learning reason.

Future changes to these choices should be recorded through new ADRs rather than rewriting this decision.