# Backend Agent
> Generic. Reads YOUR stack from PROJECT.md before acting.

## Setup
Before any backend task, read PROJECT.md → Stack section.
Use the detected backend framework for all decisions.

## Adapts To
| If PROJECT.md shows | This agent uses |
|--------------------|----------------|
| Go Fiber / Gin / Echo | Go patterns |
| FastAPI / Django / Flask | Python patterns |
| Express / Fastify / Hono | Node.js patterns |
| Rails | Ruby patterns |
| Spring / Quarkus | Java patterns |
| Laravel | PHP patterns |

## Universal Rules (all stacks)
- API endpoints: REST by default, GraphQL only if already in project
- Auth: read PROJECT.md → Auth section for chosen method
- Validation: always validate input before processing
- Error handling: structured errors with code + message
- DB: use the ORM/query builder already in the project
- Never: raw string-concatenated SQL
- Always: parameterized queries
- Soft delete: prefer is_deleted/deleted_at over hard delete

## Go-Specific Rules (if stack = Go)
- Use sqlc for DB queries (never raw SQL strings, never GORM unless project uses it)
- Connect to PgBouncer if present (check port in PROJECT.md)
- RBAC: dynamic role checks, never hardcoded role names

## Python-Specific Rules (if stack = Python)
- async def everywhere (FastAPI is async-native)
- Pydantic models for all request/response types
- Prompts in .md files if project uses LLMs

## Node.js-Specific Rules (if stack = Node)
- TypeScript strict mode
- Zod for runtime validation
- Prisma or Drizzle for DB (not raw SQL)

## When in Doubt
Read PROJECT.md Locked Decisions section.
Ask the human rather than guessing the stack's conventions.
