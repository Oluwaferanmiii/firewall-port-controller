# Firewall Port Controller

This Python script allows you to open and close a firewall port using an IP address. It restricts access to the website unless an IP address has been explicitly permitted.

## Features
- Open a specific port on a remote firewall using a browser command.
- Close the firewall port and restrict access based on the IP address.
- Simple control using browser URLs with the `open` and `close` actions.

## Prerequisites
- Python 3.x installed on the remote desktop/server.
- Proper firewall configurations in place that allow Python scripts to interact with firewall settings.

## How to Run the Script

1. **Command Line Execution**:
   - Run the script in the command prompt using:
     ```
     python C:/path/to/script/firewall_control.py
     ```

2. **Control the Firewall Port via Browser**:
   - Open your web browser and navigate to:
     ```
     http://<remote-desktop-ip>:8080/?action=open
     ```
     This will open the firewall port.
   
   - To close the firewall port, use:
     ```
     http://<remote-desktop-ip>:8080/?action=close
     ```

## Example

1. Run the script:

2. To open the port:
- Open a browser and navigate to:
  ```
  http://192.168.0.1:8080/?action=open
  ```

3. To close the port:
- Open a browser and navigate to:
  ```
  http://192.168.0.1:8080/?action=close
  ```

## Script Details

- **IP Address Control**: The script checks the provided IP address and determines whether to grant or restrict access to the website.
- **Firewall Port**: By default, the script interacts with port 8080, but this can be changed in the script as needed.
- **Actions**: The `open` and `close` actions are used to manage the firewall status.

## Future Enhancements

- Add a logging mechanism to keep track of access attempts and actions performed.
- Implement more granular control for IP-based access, such as whitelisting specific IP addresses.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

