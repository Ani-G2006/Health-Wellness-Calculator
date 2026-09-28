# Health & Wellness Calculator

A command-line Python application that calculates common health metrics, keeps a record of every calculation, and lets you view or clear that history later.

Built as a semester project for **CSE1021 – Introduction to Problem Solving and Programming** at VIT Bhopal.

---

## Features

| Metric | What it tells you |
|---|---|
| **BMI** (Body Mass Index) | Your weight relative to your height, with a category (Underweight, Healthy, Overweight, Obesity class 1/2/3) |
| **BMR** (Basal Metabolic Rate) | Calories your body burns at complete rest |
| **Daily calorie requirement** | Calories needed per day, based on your BMR and activity level |
| **Ideal body weight** | Expected weight for your height and sex |
| **Daily water intake** | Minimum litres of water per day, based on weight and activity level |

Other highlights:

- Repeat any calculation as many times as you like in one session (for example, for several people)
- Every result is saved automatically to a plain-text file
- View saved history for any metric
- Delete saved history for any metric
- Menu-driven, so no commands to memorise

---

## Project Structure

```
.
├── track.py        # Entry point: main menu and program flow
├── calculator.py   # All five calculation functions and their in-memory records
└── store.py        # File handling: saving, viewing and deleting records
```

| File | Responsibility |
|---|---|
| `track.py` | Shows the menus, calls the right calculator, then asks `store.py` to save the new records |
| `calculator.py` | Takes user input, performs the calculation, prints the result and appends it to a list (`BMI`, `BMR`, `Weight`, `Calorie`, `Waterintake`) |
| `store.py` | Builds file paths relative to the script folder, appends new entries to files, reads files back and clears them |

After you finish a calculation, `track.py` writes only the **new** entries from that session to disk, using the list length before the calculation as the starting point.

---

## Requirements

- **Python 3.10 or newer** (the program uses `match / case`)
- No external libraries; only the standard library (`os`) is used

Check your version:

```bash
python --version
```

---

## How to Run

1. Put `track.py`, `calculator.py` and `store.py` in the same folder.
2. Open a terminal in that folder.
3. Run:

```bash
python track.py
```

---

## Using the Program

### Main menu

```
1 for calculate(BMI, BMR, Ideal Weight, Ideal Waterintake, Required Calorie)
2 for View History
3 for delete data
4 for exit
```

### 1. Calculate

Choose a metric:

```
1 for BMI
2 for daily minimum water intake
3 for calculate bmr
4 required calorie
5 for ideal weight
6 for exit
```

Each calculator asks for the date (once), then your name and the required measurements. After each result you can enter `1` to calculate again or `2` to stop.

| Calculator | Inputs asked |
|---|---|
| BMI | Height (inches), weight (kg) |
| BMR | Weight (kg), height (inches), age (years), sex |
| Ideal weight | Height (inches), sex |
| Calorie requirement | Your BMR, activity level (1–5) |
| Water intake | Weight (kg), activity level (1–3) |

> Tip: calculate your **BMR first**, then enter that value in the calorie calculator.

### 2. View History

Pick a metric to print every record saved for it.

### 3. Delete Data

Pick a metric to clear its saved records.

### 4. Exit

Ends the program.

---

## Formulas Used

**BMI**

```
BMI = weight (kg) / height (m)²        where height (m) = height (inches) / 39.3701
```

| BMI | Category |
|---|---|
| below 18.5 | Underweight |
| 18.5 to 24.9 | Healthy |
| 25 to 29.9 | Overweight |
| 30 to 34.9 | Obesity (class 1) |
| 35 to 39.9 | Obesity (class 2) |
| 40 and above | Obesity (class 3) |

**BMR** (Mifflin–St Jeor equation, height converted to cm)

```
Male:   BMR = (10 × weight) + (6.25 × height_cm) − (5 × age) + 5
Female: BMR = (10 × weight) + (6.25 × height_cm) − (5 × age) − 161
```

**Daily calorie requirement**

```
Calories = BMR × activity multiplier
```

| Activity level | Multiplier |
|---|---|
| Sedentary (no exercise) | 1.2 |
| Lightly active | 1.375 |
| Moderately active | 1.55 |
| Very active | 1.725 |
| Extra active | 1.9 |

**Ideal body weight** (Devine formula, height in inches)

```
Male:   50 + 2.3 × (height − 60)  kg
Female: 45.5 + 2.3 × (height − 60) kg
```

**Daily water intake**

```
Water (L) = weight (kg) × factor / 1000
```

| Activity level | Factor (ml per kg) |
|---|---|
| Sedentary | 30 |
| Moderate | 35 |
| Active | 40 |

---

## Data Storage

Records are stored as plain text, one entry per line, in the same folder as the scripts. Each line is a set of `key=value` pairs separated by `|`.

| Metric | File |
|---|---|
| BMI | `BMI_data.txt` |
| BMR | `BMR_data.txt` |
| Ideal weight | `Weight_data.txt` |
| Calorie requirement | `calorie_data.txt` |
| Water intake | `Waterintake_data.txt` |

Example line from `BMI_data.txt`:

```
Date=23/09/2026|Name=Asha|BMI=22.86|Nature=Healthy
```

Files are created automatically the first time a metric is calculated. New records are appended, so earlier records are kept until you delete them from the menu.

---

## Sample Session

```
Enter any one: 1
Enter any one: 1
Enter date(DD/MM/YYYY): 23/09/2026
Enter your name: Asha
enter your hight(inch): 65
enter your weight(Kg) : 62
your BMI is: 22.74...
Healthy
1 to calculate again
2 to stop
enter any one: 2
```

*(Exact numbers depend on the inputs you enter.)*

---

## Limitations

- Inputs are not validated. Entering text where a number is expected, or a negative value, will crash or give meaningless results.
- Height is entered in inches and weight in kilograms; other units are not supported.
- BMI, BMR and the other results are general estimates and are **not medical advice**. Consult a healthcare professional for personal health decisions.

---

## Possible Future Improvements

- Input validation and friendlier error messages
- Support for metric height (cm) as well as inches
- A web or graphical front end
- Charts of BMI or weight over time

---
