import subprocess

def execute_command(command):
    try:
        # Execute the command
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Print the output of the command
        print("Command output:")
        print(result.stdout)
        
        # Print the error (if any)
        if result.stderr:
            print("Command error:")
            print(result.stderr)
        
        # Return the exit code
        return result.returncode
    
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print(f"Command failed with exit code {e.returncode}")
        print(f"Error output: {e.stderr}")
        return e.returncode

if __name__ == "__main__":
    # Example command to execute
    command = "python main.py && python response_parser.py && python location_plotter.py"
    
    # Execute the command
    exit_code = execute_command(command)
    
    # Print the exit code
    print(f"Command exited with code: {exit_code}")
