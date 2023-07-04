import subprocess
import sys
# Function made to check if Docker compose is installed or not and if not it will install
def check_docker():
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Docker is installed.")
    except FileNotFoundError:
        print("Docker is not installed.")

def create_wordpress_site(site_name):
    try:
        subprocess.run(["docker", "run", "-d", "--name", site_name, "-p", "80:80", "wordpress:latest"])
        print("WordPress site created successfully!")
        print(f"Access your site at http://localhost/{site_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating the WordPress site: {e}")

def stop_wordpress_site(site_name):
    try:
        subprocess.run(["docker", "stop", site_name])
        print("WordPress site stopped successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping the WordPress site: {e}")

def start_wordpress_site(site_name):
    try:
        subprocess.run(["docker", "start", site_name])
        print("WordPress site started successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error starting the WordPress site: {e}")


def main():
    print("Checking Docker installation...")
    check_docker()
    if len(sys.argv) < 2:
        print("Please provide the site name as a command-line argument.")
        print("Usage: python3 create_wordpress.py <site_name>")
        sys.exit(1)

    subcommand = sys.argv[1]
    site_name = sys.argv[2]
    
    if subcommand == "create":
        create_wordpress_site(site_name)
    elif subcommand == "stop":
        stop_wordpress_site(site_name)
    elif subcommand == "start":
        start_wordpress_site(site_name)
    else:
        print("Invalid subcommand.")
        print("Available subcommands: create, stop, start")

if __name__ == "__main__":
    main()
