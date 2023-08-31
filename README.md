# Raspberry Pi Clock Display

This project displays a clock in dark mode on the HDMI output of a Raspberry Pi. The time is displayed in the Oslo timezone.

## Requirements

- Raspberry Pi running Raspberry Pi OS
- Python 3
- Pygame library for Python

## Installation

1. Clone this repository to your Raspberry Pi.
2. Install the required Python libraries with `pip3 install pygame`.

## Usage

To run the clock display, use the following command:

```bash
python3 /home/pi/btv-clock/clock.py
```

The clock display will show the current time in white text on a black background.

## Auto-start on Boot

To automatically start the clock display on boot, add the following lines to your crontab:

```bash
@reboot xrandr -display :0.0 --output HDMI-1 --mode 1920x1080i --rate 50
@reboot python3 /home/pi/btv-clock/clock.py
```

With these changes, the clock display will automatically start every time your Raspberry Pi boots up.

## License

This project is licensed under the terms of the MIT license.