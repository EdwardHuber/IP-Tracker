# 📍 IP Tracker

> A simple Python tool to track detailed information about any public IP address using a geolocation API.

## Description

This script queries a public API to retrieve information like location, ISP, timezone, and organization data about any IP address. You can use it to analyze your own IP or investigate a suspicious one.

## Features

- Tracks:
  - City, Region, Country
  - Latitude and Longitude
  - Timezone
  - ISP and Organization
- Accepts manual IP input or uses your public IP by default
- Clean terminal output

## Requirements

```bash
pip install requests
