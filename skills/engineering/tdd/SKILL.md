# Test-Driven Development
> Source: mattpocock/skills (119K★) + addyosmani/agent-skills (48K★)

## WHEN TO USE
When implementing any new function, endpoint, component, or expert.
Write the test first. Implementation second. Always.

## STEPS
1. Write the failing test that describes the behaviour
2. Run test → confirm it fails
3. Implement minimum code to make test pass
4. Run test → confirm it passes
5. Refactor if needed, tests still pass

## SUCCESS CRITERIA
- Test exists before implementation
- Test fails before implementation
- Test passes after implementation
- No implementation code changes the test

## PATTERNS
- Unit: test one function in isolation
- Integration: test module with real DB (use test container)
- E2E: test full user flow (Playwright / Maestro for mobile)
