import sys
import os # Essential for file and directory operations

# Define a default filename for user data storage
FILE_NAME = "user_data.txt" 

class EunoiaverseShell:
    """
    A simple interactive console shell user named 'eunoiaverse'.
    """
    def __init__(self, username="eunoiaverse"):
        self.username = username
        self.is_running = True
        self.history = []
        
        # A simple dictionary for handling basic, predefined commands
        self.commands = {
            'help': self._cmd_help,
            'exit': self._cmd_exit,
            'quit': self._cmd_exit,
            'greet': self._cmd_greet,
            'history': self._cmd_history,
            'add': self._cmd_add,
            # --- NEW COMMANDS ADDED BELOW ---
            'mkdir': self._cmd_mkdir,
            'touch': self._cmd_touch,
            'rm': self._cmd_rm,
            'connect': self._cmd_connect,
            'cli': self._cmd_cli,
        }

    def _get_prompt(self):
        """Generates the shell prompt."""
        # Display the current working directory in the prompt
        return f"[{os.getcwd()}] {self.username}> "

    def _parse_input(self, command_line):
        """Parses the input string into command and arguments."""
        # Use shlex for robust parsing that handles quoted arguments, like file paths with spaces
        import shlex
        try:
            parts = shlex.split(command_line.strip())
        except ValueError:
            print("Error: Invalid command format (e.g., unmatched quotes).")
            return None, []
        
        if not parts:
            return None, []
            
        command = parts[0].lower()
        args = parts[1:]
        return command, args

    def _execute_command(self, command, args):
        """Executes the command if it exists."""
        # Add to history before execution, in case it fails
        self.history.append((command, args)) 
        
        if command in self.commands:
            self.commands[command](args)
        else:
            print(f"Error: Unknown command '{command}'. Type 'help' for a list of commands.")

    # --- Core Command Handlers ---
    
    def _cmd_help(self, args):
        """Displays available commands."""
        print("\nAvailable Commands:")
        print("  **help** : Display this help message.")
        print("  **exit/quit** : Exit the eunoiaverse shell.")
        print("  **greet** : Receive a friendly greeting.")
        print("  **history** : Show the history of executed commands.")
        print("  **add** <server> <user> <email> <pass> : Add a new login record.")
        print("--- File & Directory Management ---")
        print("  **mkdir** <dirname> : Create a new directory (folder).")
        print("  **touch** <filename> : Create an empty file.")
        print("  **rm** <path> : Delete a file or an empty directory.")
        print("--- Simulation Tools ---")
        print("  **connect** <host> : Simulate connecting to a server.")
        print("  **cli** <tool_name> : Simulate creating a command-line tool script.")
        print("---")

    def _cmd_exit(self, args):
        """Sets the flag to stop the shell loop."""
        print("Goodbye! Exiting eunoiaverse shell.")
        self.is_running = False

    def _cmd_greet(self, args):
        """Prints a welcome message."""
        print(f"Hello, {self.username}! Welcome to your custom Python console.")

    def _cmd_history(self, args):
        """Prints the command history."""
        if not self.history:
            print("No commands executed yet.")
            return

        print("\nCommand History:")
        for i, (cmd, arg) in enumerate(self.history, 1):
            args_str = ' '.join(arg)
            print(f"  {i}: {cmd} {args_str}")
        print("---")
        
    def _cmd_add(self, args):
        """Adds new server/user login data to the specified file."""
        if len(args) < 4:
            print("Usage Error: **add** requires <server> <username> <email> <password>.")
            print("Example: add ubuntu user1 user1@server.com s3cr3tp4ss")
            return

        server, username, email, password = args[0], args[1], args[2], args[3]
        data_line = f"SERVER: {server} | USERNAME: {username} | EMAIL: {email} | PASSWORD: {password}\n"
        
        try:
            with open(FILE_NAME, 'a') as f:
                f.write(data_line)
                
            print(f"✅ Added login for **{username}** on **{server}** to **{FILE_NAME}**.")
            
        except IOError as e:
            print(f"File Error: Could not write to **{FILE_NAME}**. Details: {e}")

    # --- NEW TOOL COMMAND HANDLERS ---
    
    def _cmd_mkdir(self, args):
        """Creates a new directory."""
        if not args:
            print("Usage Error: **mkdir** requires a directory name. Example: mkdir my_project")
            return
            
        dir_name = args[0]
        try:
            # os.makedirs creates directories recursively if needed
            os.makedirs(dir_name, exist_ok=True) 
            print(f"📁 Directory **{dir_name}** created successfully.")
        except OSError as e:
            print(f"Error creating directory: {e}")

    def _cmd_touch(self, args):
        """Creates a new, empty file."""
        if not args:
            print("Usage Error: **touch** requires a file name. Example: touch README.md")
            return

        file_path = args[0]
        try:
            # 'a' mode creates the file if it doesn't exist, without truncating
            with open(file_path, 'a'): 
                os.utime(file_path, None) # Update the file timestamp
            print(f"📄 File **{file_path}** created/updated successfully.")
        except IOError as e:
            print(f"Error creating file: {e}")

    def _cmd_rm(self, args):
        """Deletes a file or empty directory."""
        if not args:
            print("Usage Error: **rm** requires a file or directory path. Example: rm temp.txt")
            return
            
        path_to_delete = args[0]
        
        if not os.path.exists(path_to_delete):
            print(f"Error: Path **{path_to_delete}** does not exist.")
            return

        if os.path.isfile(path_to_delete):
            try:
                os.remove(path_to_delete)
                print(f"❌ File **{path_to_delete}** deleted successfully.")
            except OSError as e:
                print(f"Error deleting file: {e}")
        elif os.path.isdir(path_to_delete):
            try:
                # This only removes an EMPTY directory
                os.rmdir(path_to_delete) 
                print(f"❌ Empty directory **{path_to_delete}** deleted successfully.")
            except OSError as e:
                print(f"Error: Directory **{path_to_delete}** is not empty or permission denied. Use system tools for recursive delete.")
        else:
            print(f"Error: **{path_to_delete}** is not a file or directory.")

    def _cmd_connect(self, args):
        """Simulates connecting to a server."""
        if not args:
            print("Usage Error: **connect** requires a host/IP. Example: connect 192.168.1.1")
            return
            
        host = args[0]
        print(f"Attempting to establish connection with **{host}**...")
        # Simulate network delay/check
        import time; time.sleep(1) 
        
        if host.lower() in ["localhost", "127.0.0.1"]:
            print("🌐 Connected successfully to **Localhost**.")
        elif host.startswith("192.") or host.startswith("10."):
            print(f"✅ Connection secured to private network host **{host}**.")
        else:
            print(f"⚠️ Connection attempt to **{host}** timed out or refused.")

    def _cmd_cli(self, args):
        """Simulates creating a basic command-line tool script."""
        if not args:
            print("Usage Error: **cli** requires a tool name. Example: cli my_tool")
            return
            
        tool_name = args[0]
        file_path = f"{tool_name}.py"
        
        # A simple Python script template for a CLI tool
        cli_template = f"""#!/usr/bin/env python
# Script generated by Eunoiaverse Shell

import sys

def main():
    if len(sys.argv) > 1:
        print(f"Executing tool: {{sys.argv[0]}}")
        print(f"Arguments provided: {{' '.join(sys.argv[1:])}}")
    else:
        print("Usage: python {tool_name}.py <argument>...")

if __name__ == "__main__":
    main()
"""
        try:
            with open(file_path, 'w') as f:
                f.write(cli_template)
            
            # Simulate making the script executable (on Unix-like systems)
            # os.chmod(file_path, 0o755) 
            
            print(f"🛠️ CLI tool script **{file_path}** created.")
            print("Hint: Run it with 'python **{file_path}** hello world'.")
            
        except IOError as e:
            print(f"Error creating CLI script: {e}")

    # --- Main Loop ---

    def run(self):
        """The main loop for the interactive shell."""
        print(f"--- Welcome to the {self.username} Python Shell Console ---")
        print("Type 'help' for available commands or 'exit' to quit.")
        
        while self.is_running:
            try:
                # Read user input
                command_line = input(self._get_prompt()).strip()
                
                if not command_line:
                    continue # Skip empty lines

                command, args = self._parse_input(command_line)
                
                if command:
                    self._execute_command(command, args)

            except EOFError:
                # Handle Ctrl-D (End of File)
                print("\nReceived EOF. Exiting...")
                self.is_running = False
            except KeyboardInterrupt:
                # Handle Ctrl-C (Interrupt)
                print("\n[Ctrl+C] Shell interrupted. Type 'exit' to quit.")
                
# --- Execution ---
if __name__ == "__main__":
    # Instantiate and run the shell
    shell = EunoiaverseShell()
    shell.run()
