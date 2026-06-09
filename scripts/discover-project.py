#!/usr/bin/env python3
"""
Discover project stack and generate PROJECT.md.
Used by /setup command.
Usage: python3 scripts/discover-project.py [path-to-project]
"""
import sys, json
from pathlib import Path

def detect_stack(root: Path) -> dict:
    stack = {
        "frontend": None, "backend": None, "database": None,
        "mobile": None, "ai": None, "hosting": None, "auth": None,
        "dep_files": [], "dirs": []
    }

    # ── dependency file detection ──────────────────────
    pkg = root / "package.json"
    if pkg.exists():
        try:
            data = json.loads(pkg.read_text())
            deps = {**data.get("dependencies",{}), **data.get("devDependencies",{})}
            stack["dep_files"].append("package.json")

            # Frontend frameworks
            if "@sveltejs/kit" in deps: stack["frontend"] = "SvelteKit"
            elif "next" in deps: stack["frontend"] = "Next.js"
            elif "nuxt" in deps: stack["frontend"] = "Nuxt"
            elif "astro" in deps: stack["frontend"] = "Astro"
            elif "remix" in deps: stack["frontend"] = "Remix"
            elif "react" in deps: stack["frontend"] = "React"
            elif "vue" in deps: stack["frontend"] = "Vue 3"

            # Mobile
            if "react-native" in deps: stack["mobile"] = "React Native"
            if "expo" in deps: stack["mobile"] = "Expo + React Native"

            # Backend (Node)
            if "hono" in deps: stack["backend"] = "Hono"
            elif "fastify" in deps: stack["backend"] = "Fastify"
            elif "express" in deps: stack["backend"] = "Express"
            elif "elysia" in deps: stack["backend"] = "Elysia (Bun)"

            # AI
            if "ai" in deps or "@ai-sdk" in str(deps): stack["ai"] = "Vercel AI SDK"

            # Auth
            if "better-auth" in deps: stack["auth"] = "better-auth"
            elif "next-auth" in deps: stack["auth"] = "NextAuth"
            elif "lucia" in deps: stack["auth"] = "Lucia"

        except: pass

    go_mod = root / "go.mod"
    if go_mod.exists():
        content = go_mod.read_text()
        stack["dep_files"].append("go.mod")
        if "gofiber/fiber" in content: stack["backend"] = "Go Fiber"
        elif "gin-gonic/gin" in content: stack["backend"] = "Gin"
        elif "labstack/echo" in content: stack["backend"] = "Echo"
        elif "go-chi/chi" in content: stack["backend"] = "Chi"
        else: stack["backend"] = "Go (standard library)"

    for py_file in ["pyproject.toml", "requirements.txt"]:
        pf = root / py_file
        if pf.exists():
            content = pf.read_text().lower()
            stack["dep_files"].append(py_file)
            if "fastapi" in content: stack["backend"] = stack["backend"] or "FastAPI"
            if "django" in content: stack["backend"] = stack["backend"] or "Django"
            if "flask" in content: stack["backend"] = stack["backend"] or "Flask"
            if "langchain" in content: stack["ai"] = (stack["ai"] or "") + " LangChain"
            if "pydantic-ai" in content: stack["ai"] = (stack["ai"] or "") + " PydanticAI"
            if "langgraph" in content: stack["ai"] = (stack["ai"] or "") + " LangGraph"
            if "openai" in content or "anthropic" in content:
                stack["ai"] = stack["ai"] or "LLM SDK"

    if (root / "Podfile").exists():
        stack["mobile"] = stack["mobile"] or "iOS (native Swift)"
        stack["dep_files"].append("Podfile")

    if (root / "build.gradle").exists() or (root / "build.gradle.kts").exists():
        stack["mobile"] = stack["mobile"] or "Android (Kotlin)"
        stack["dep_files"].append("build.gradle")

    if (root / "pubspec.yaml").exists():
        stack["mobile"] = "Flutter"
        stack["dep_files"].append("pubspec.yaml")

    if (root / "Cargo.toml").exists():
        stack["backend"] = stack["backend"] or "Rust"
        stack["dep_files"].append("Cargo.toml")

    # ── directory scan ─────────────────────────────────
    ignore = {".git","node_modules","dist","build",".next","__pycache__",".venv","venv"}
    for d in sorted(root.iterdir()):
        if d.is_dir() and d.name not in ignore and not d.name.startswith("."):
            stack["dirs"].append(d.name)

    # ── DB detection from common patterns ──────────────
    all_text = ""
    for f in ["docker-compose.yml","docker-compose.yaml",".env.example"]:
        fp = root / f
        if fp.exists():
            all_text += fp.read_text().lower()

    if "postgres" in all_text: stack["database"] = "PostgreSQL"
    elif "mysql" in all_text: stack["database"] = "MySQL"
    elif "sqlite" in all_text: stack["database"] = "SQLite"
    elif "mongodb" in all_text: stack["database"] = "MongoDB"
    elif "redis" in all_text or "valkey" in all_text:
        stack["cache"] = "Redis/Valkey"

    # Hosting hints
    if (root / "vercel.json").exists(): stack["hosting"] = "Vercel"
    elif (root / "netlify.toml").exists(): stack["hosting"] = "Netlify"
    elif (root / "fly.toml").exists(): stack["hosting"] = "Fly.io"
    elif (root / "railway.toml").exists(): stack["hosting"] = "Railway"
    elif (root / "wrangler.toml").exists(): stack["hosting"] = "Cloudflare"
    elif (root / "coolify.yml").exists() or (root / "docker-compose.yml").exists():
        stack["hosting"] = "Self-hosted (Docker)"

    return stack


def generate_project_md(root: Path, stack: dict) -> str:
    # Try to get description from README
    desc = "{Describe your project here}"
    readme = root / "README.md"
    if readme.exists():
        lines = readme.read_text().splitlines()
        for line in lines:
            if line.strip() and not line.startswith("#"):
                desc = line.strip()[:200]
                break

    lines = [
        "# PROJECT.md",
        f"> Auto-generated by ll-vibekit scripts/discover-project.py",
        f"> Root: {root}",
        "",
        "## What This Project Is",
        desc,
        "",
        "## Stack (auto-detected)",
        "| Layer | Technology | Notes |",
        "|-------|-----------|-------|",
    ]

    for layer, tech in [
        ("Frontend", stack.get("frontend")),
        ("Backend",  stack.get("backend")),
        ("Database", stack.get("database")),
        ("Cache",    stack.get("cache")),
        ("Mobile",   stack.get("mobile")),
        ("AI/ML",    stack.get("ai")),
        ("Auth",     stack.get("auth")),
        ("Hosting",  stack.get("hosting")),
    ]:
        if tech:
            lines.append(f"| {layer} | {tech} | |")
        else:
            lines.append(f"| {layer} | (not detected) | fill manually |")

    lines += [
        "",
        "## Dependency Files Found",
        "
".join(f"- {f}" for f in stack["dep_files"]) or "- (none found)",
        "",
        "## Key Directories",
        "```",
        "
".join(f"{d}/" for d in stack["dirs"][:12]),
        "```",
        "",
        "## Current Features / Modules",
        "| Module | Status | Notes |",
        "|--------|--------|-------|",
        "| (fill after /setup discover) | | |",
        "",
        "## Locked Decisions",
        "- (fill with your architectural constraints)",
        "",
        "## Active Sprint",
        "(what are you building right now?)",
        "",
        "## Human TODO",
        "- [ ] (tasks only humans can do — API registrations, payment setup, etc.)",
        "",
        "## Commands",
        "```bash",
        "(fill with your build/test/deploy commands)",
        "```",
        "",
        "## Notes for AI Agents",
        "(anything the agent must know — constraints, conventions, pitfalls)",
    ]

    return "
".join(lines)


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    print(f"Scanning: {root}")
    print()

    stack = detect_stack(root)

    print("Detected stack:")
    for k, v in stack.items():
        if k not in ("dep_files", "dirs") and v:
            print(f"  {k:<12} {v}")

    print("
Dependency files found:")
    for f in stack["dep_files"]:
        print(f"  {f}")

    print("
Directories:")
    print("  " + "  ".join(stack["dirs"][:10]))

    md = generate_project_md(root, stack)
    out = root / "PROJECT.md"
    out.write_text(md)
    print(f"
Generated: {out}")
    print("Review and edit PROJECT.md, then run /route in Claude Code.")


if __name__ == "__main__":
    main()
