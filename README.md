# Cursor Cloud Agent weather POC

This repo is a small proof of concept: fetch the current temperature for ZIP 75024 (Plano, TX) and append one line to `temperature_log.txt` every hour.

`weather_poc.py` calls the Open-Meteo forecast API (no API key) and appends a timestamped reading. Run it locally with:

```
python weather_poc.py
```

Two hourly runners can do the same job. Either one is enough; both can stay enabled.

## Cursor Cloud Agent (scheduled automation)

A Cursor Automation on an hourly schedule checks out this GitHub repo, runs `weather_poc.py`, appends a line to `temperature_log.txt`, and commits the log if the cloud workspace allows writes.

Enable it in Cursor: **Automations** (or the [Cloud Agents dashboard](https://cursor.com/dashboard?tab=cloud-agents)). Confirm the repo is `lakshmaiah-narisetty/CursorAgentPOC` on `main`, the schedule is every hour, and Cloud compute is on. Save and turn the automation on.

## GitHub Action (repo-side hourly runner)

`.github/workflows/hourly-weather.yml` runs on the hour (UTC) and also supports **Run workflow** from the Actions tab.

1. Open the repo on GitHub → **Actions** and enable workflows if prompted.
2. Because the job commits `temperature_log.txt`, give the workflow write permission: **Settings → Actions → General → Workflow permissions → Read and write permissions**.
3. Use **Actions → Hourly weather log → Run workflow** once to confirm a new line appears.

## What success looks like

Every hour, `temperature_log.txt` gains a line like:

```
2026-09-03 17:17:13 | Temperature: 91.7°F
```
