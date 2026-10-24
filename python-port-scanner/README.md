## Python Port Scanner
A TCP port scanner built from scratch in Python using the built-in socket library.

### Features
- Customizable starting and ending ports
- Configurable connection timeouts
- Quick and robust scan modes
- Live status output for open, closed, and timed-out ports
- Input validation and hostname resolution

### Requirements
- Python 3

### Usage
Run the program: python port_scanner.py
Follow the prompts to enter an IP address, select a scan mode, and specify a port range.

### How It Works
The scanner attempts TCP connections to ports in the selected range. Successful connections are reported as open, connection refusals as closed, and timeouts separately. A timeout does not necessarily mean a port is filtered.

### Responsible Use
Use this tool only on systems you own or have explicit permission to test.

### Future Improvements
- Common service identification
- Scan duration and performance statistics
- CSV report export
- Automated tests
- Concurrent scanning
