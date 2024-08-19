# Lumen Ala Performance

[![Latest Version](https://img.shields.io/github/v/release/not-empty/ala-performance-locust?style=flat-square)](https://github.com/not-empty/lumen-ala-performance/releases)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Python code using locust to get domain performance

### Installation

Requires [Python](https://www.python.org/) 3.7.

The recommended way to install is through [Pip](https://pypi.org/project/pip/).

```sh
pip install -r requirements.txt
```

```sh
cp .env.example .env
```

Put values in **CONTEXT**, **SECRET** and **TOKEN** environment because the script need to authenticate and verify all CRUD routes (Get this [config](https://github.com/not-empty/ala-microframework-php/blob/master/config/token.php) in Lumen-Ala project).

### Run Cli interface

Run the file domainperformance.py using [Locust](https://locust.io/)

```sh
locust -f domainperformance.py
```

And access [Localhost dashboard](http://localhost:8089/) to start the Locust

### Run in background

This example run with 1000 users and spawned 10 per second for 1 minute.

```sh
locust -f domainperformance.py -H {Your Host and Port Here} -u 1000 -r 10 -t 1m --headless --csv report
``` 

After running this command, you can consulting 3 files *report_failures.csv*, *report_stats.csv* and *report_stats_history.csv* to validate the performance test.

### Development

Want to contribute? Great!

The project using a simple code.
Make a change in your file and be careful with your updates!

**Not Empty Foundation - Free codes, full minds**
