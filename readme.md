# Window State Announcer (NVDA Add-on)

This NVDA add-on provides a simple command to announce the current state of the active window.

When triggered, it reports whether the foreground window is:
- Maximized
- Minimized
- In its normal state

The add-on works as a global plugin and does not announce anything automatically.

## Usage

- Press **NVDA + Windows + Space**
- NVDA will announce the state of the currently active window

The announcement is on-demand and does not interrupt ongoing speech.

## Notes

- The add-on uses standard Windows APIs to determine window state.
- If no valid foreground window is detected, NVDA will announce that no window is available.
- No settings or configuration are required.

## Compatibility

- Intended for use with modern NVDA versions on Windows.
- Tested as a global plugin only.

## License

This add-on is distributed under the GNU General Public License, version 2 or later.
See `COPYING.txt` for full license details.
