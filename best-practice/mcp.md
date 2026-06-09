# MCP Best Practice
> Source: shanraisshan/claude-code-best-practice claude-mcp.md

## AgencyOS MCP Server (FastMCP on :8002)
```python
# src/mcp/server.py
@mcp.tool()
async def scrapling_research(url: str) -> str: ...
@mcp.tool()
async def knowledge_retrieve(client_id: str, query: str) -> str: ...
@mcp.tool()
async def social_trend_research(keywords: list[str]) -> list[dict]: ...
```

## Connect in Claude Code
```json
{
  "agencyos-ai": {
    "command": "python",
    "args": ["-m", "src.mcp.server"],
    "cwd": "/path/to/agencyos-ai"
  }
}
```

## Rules
- MCP: for external callers and Claude Code
- Internal: direct Python function calls (faster)
- Rate limit: 100 MCP calls/hour per tenant
- All calls logged in a2a_tasks for audit

## Adding New Tool
```python
@mcp.tool()
async def new_tool(param: str) -> str:
    '''Description shown to MCP clients.'''
    return await your_function(param)
```
