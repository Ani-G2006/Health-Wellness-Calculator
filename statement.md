# Project Statement

## Problem Statement

People frequently want quick estimates of common health metrics — BMI, BMR, daily
calorie needs, ideal body weight, and daily water intake — but usually turn to
scattered online calculators that don't save any history. Each visit starts from
zero: there's no record of past results, no way to compare a new calculation
against an earlier one, and no single place that covers all five metrics together.
This project addresses that by providing one command-line tool that performs all
five calculations and automatically keeps a running record of every result for
later reference.

## Scope of the Project

**In scope:**
- Five health metric calculators: BMI, BMR, ideal body weight, daily calorie
  requirement, and daily water intake
- A menu-driven command-line interface requiring no prior setup beyond Python
- Persistent storage of every calculation, per metric, in plain text files
- Viewing saved history for any metric
- Deleting saved history for any metric

**Out of scope:**
- A graphical or web-based interface
- Unit systems other than inches/kilograms
- Medical diagnosis or personalized health advice — results are general
  estimates only
- Multi-user accounts or login

## Target Users

- Individuals who want fast, repeatable estimates of common health metrics
  without relying on ad-hoc web calculators
- Anyone tracking these metrics for themselves or a small group (each record
  is tagged with a name and date, so one session can cover several people)
- Students and instructors reviewing this project as a demonstration of
  Python fundamentals — functions, modules, file handling, and persistent
  data storage

## High-Level Features

- Calculate BMI, BMR, ideal body weight, daily calorie requirement, and
  daily water intake
- Repeat any calculation as many times as needed in a single session
- Every result is saved automatically, with no extra steps required
- View previously saved history for any individual metric
- Delete previously saved history for any individual metric
- Simple numbered menus throughout — no commands to memorize
