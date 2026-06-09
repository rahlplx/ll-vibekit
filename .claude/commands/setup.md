# /setup — Project Discovery & Configuration

The most important command in ll-vibekit.
Run once when installing into a new OR existing project.
Generates PROJECT.md which all agents read.

---

## Usage

```
/setup new        → starting a brand-new project
/setup discover   → already have code, need to understand it
/setup refresh    → re-scan after major changes
```

---

## /setup new

For greenfield projects with no code yet.

### Steps
1. Ask the human:
   - "What are you building? Describe it in 2-3 sentences."
   - "What tech stack? (or say 'suggest one' for recommendations)"
   - "Web app, mobile app, API, or something else?"
   - "Solo or team? Any constraints (budget, hosting, timeline)?"

2. Based on answers, generate PROJECT.md with:
   - Project description
   - Recommended stack (or confirmed stack)
   - Empty modules table
   - Relevant HUMAN-TODO items for that stack

3. Suggest first skill to use based on stack:
   - SaaS web → skills/saas/add-module/SKILL.md
   - Mobile → skills/mobile/react-native-expo/SKILL.md
   - API only → skills/engineering/api-design/SKILL.md

---

## /setup discover

For existing projects. Auto-detects stack from files.

### Step 1: Scan for dependency files
```
package.json     → Node.js / JS framework
go.mod           → Go
pyproject.toml   → Python
requirements.txt → Python
pom.xml          → Java / Kotlin
build.gradle     → Android / Kotlin
Podfile          → iOS / Swift
Cargo.toml       → Rust
composer.json    → PHP
Gemfile          → Ruby
pubspec.yaml     → Flutter / Dart
```

### Step 2: Detect framework from deps
```javascript
// package.json detection
"@sveltejs/kit"     → SvelteKit
"next"              → Next.js
"react-native"      → React Native
"expo"              → Expo
"hono"              → Hono
"express"           → Express
"fastify"           → Fastify

// go.mod detection
"github.com/gofiber/fiber"  → Go Fiber
"github.com/gin-gonic/gin"  → Gin
"github.com/labstack/echo"  → Echo

// pyproject.toml / requirements.txt
"fastapi"    → FastAPI
"django"     → Django
"flask"      → Flask
"langchain"  → LangChain stack
"pydantic-ai"→ PydanticAI agents
```

### Step 3: Scan directory structure
```
src/          → frontend source
app/          → Next.js / Expo Router pages
cmd/          → Go entrypoints
internal/     → Go modules
migrations/   → database migrations
agents/       → AI agent files
```

### Step 4: Read existing docs if present
```
README.md     → project description
DECISIONS.md  → locked decisions
CLAUDE.md     → existing rules (merge with ll-vibekit rules)
```

### Step 5: Generate PROJECT.md
Fill every section based on discovered data.
Ask clarifying questions only for sections that cannot be inferred.

### Step 6: Confirm with human
Show: "Here's what I found — does this look right?"
Allow corrections before saving.

---

## /setup refresh

Re-run discovery after the project has changed significantly.
Diffs against existing PROJECT.md and asks about changes.
Useful after: adding a new language, major refactor, new team member.

---

## Output

After any /setup variant, PROJECT.md is created/updated.
Print: "PROJECT.md generated. Run /route to start building."

Token budget: /setup is the ONE expensive session. After that, PROJECT.md
keeps every session cheap by pre-answering all context questions.
