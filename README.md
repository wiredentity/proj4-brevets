# ACP Brevet Time Calculator
**Author**: Willow Sack **Email**: willow0@uoregon.edu

This project is a Flask application that calculates the opening and closing times for controls during an ACP brevet. It uses AJAX to update the times automatically when a user enters a control distance.

The calculator is based on the [RUSA brevet time calculator](https://rusa.org/octime_acp.html).

## How to Use

1. Select the brevet distance (200, 300, 400, 600, or 1000 km).
2. Enter the start date and time.
3. Enter the distance of a control in either miles or kilometers.
4. The opening and closing times will automatically appear.

Changing the start date, time, or brevet distance will also update any control times that have already been calculated.

## How the Times are Calculated

The opening and closing times are calculated using the ACP rules. Opening times use the maximum allowed speeds, while closing times use the minimum speeds.

The speeds change depending on how far into the brevet the control is. To calculate the time, the program goes through each distance segment and divides the distance traveled in that segment by its speed. It adds these times together, rounds to the nearest minute, and adds the result to the brevet start time.

### Opening Times

| Distance (km) | Speed (km/h) |
|---|---|
| 0–200 | 34 |
| 200–400 | 32 |
| 400–600 | 30 |
| 600–1000 | 28 |
| 1000–1300 | 26 |

### Closing Times

| Distance (km) | Speed (km/h) |
|---|---|
| 0–200 | 15 |
| 200–400 | 15 |
| 400–600 | 15 |
| 600–1000 | 11.428 |
| 1000–1300 | 13.333 |

#### Special Cases

- The starting control (0 km) opens at the start time and closes one hour later.
- Controls under 60 km use the formula `(distance / 20) + 1` hours for their closing time.
- The finish control uses the official maximum time for that brevet distance.
- If a control is farther than the brevet distance, the program uses the brevet distance instead.

### Finish Times

| Brevet Distance | Maximum Time |
|---|---|
| 200 km | 13 hours 30 minutes |
| 300 km | 20 hours |
| 400 km | 27 hours |
| 600 km | 40 hours |
| 1000 km | 75 hours |

The calculated times are returned as ISO 8601 date/time strings using the same timezone as the start time.

## Running the Project

The application runs using Docker.

Build the image:

```bash
docker build -t brevet-calculator .
```

Run the container:

```bash
docker run --rm -it -p 5000:5000 brevet-calculator
```

Then open `http://localhost:5000` in a browser.

## Testing

The tests are in `test_acp_times.py`. They check different control distances, finish times, and some of the special cases in the ACP rules.

From the `brevets` directory, run:

```bash
nosetests
```
