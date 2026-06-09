# PRP: Weekly Analytics Report
> Example PRP — E9 generates Monday morning reports
> Status: READY TO EXECUTE

## Goal
Every Monday at 9am BD time, E9 generates a performance report
for each active client and queues it in HITL for agency review.

## Success Criteria
- [ ] Temporal ScheduledWorkflow fires every Monday 9am Asia/Dhaka
- [ ] E9 generates report with top 5 posts + engagement summary
- [ ] HITL queue shows report under "Weekly Report" label with client name
- [ ] Approved reports sent to agency email via Postal
- [ ] Report archived in reports table with generated_at timestamp

## Files In Scope
- go/db/migrations/005_reports.sql
- go/db/queries/reports.sql
- go/internal/modules/reports/service.go
- go/internal/modules/reports/handlers.go
- src/experts/e9_analytics.py
- src/prompts/e9_analytics.md
- src/temporal/workflows/weekly_report.py
- agencyos-web/src/routes/(app)/reports/+page.svelte

## Files NOT In Scope
- billing module
- social scheduling module
- E1 content expert

## DECISIONS.md Compliance
- [ ] Temporal Cloud for scheduled workflow (not cron job)
- [ ] is_deleted on reports table
- [ ] RLS on reports table
- [ ] Valkey pub/sub for HITL notification when report ready

## Implementation Order
1. Migration 005_reports.sql
2. sqlc generate
3. Go reports module
4. E9 expert + prompt
5. Temporal WeeklyReportWorkflow (cron: 0 9 * * 1, tz: Asia/Dhaka)
6. Svelte reports route
7. Email delivery via Postal on approval

## Edge Cases
1. No posts this week: generate "slow week" summary, still queue in HITL
2. Client disconnected from social: note in report, skip their metrics
3. Approval expires (72h): auto-send or skip? → skip and log
