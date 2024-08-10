import os
import shutil
import paramiko
from scp import SCPClient

# Configuration
PROJECT_NAME = "TouchDesignerProject"
BUILD_DIR = "dist"  # Directory where the build output is stored
DEPLOY_DIR = "/path/to/deploy/directory"  # Path to the deployment directory on the server or local machine

# Remote server configuration (if deploying to a remote server)
REMOTE_SERVER = "your.server.com"
REMOTE_USER = "username"
REMOTE_PASSWORD = "password"
REMOTE_PATH = "/path/on/remote/server"

# SSH Key configuration (optional)
USE_SSH_KEY = False
SSH_KEY_PATH = "/path/to/your/private/key"

# Function to deploy locally
def deploy_locally(build_dir, deploy_dir):
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    shutil.copytree(build_dir, deploy_dir)
    print(f"Project deployed locally to {deploy_dir}")

# Function to deploy to a remote server using SCP
def deploy_to_remote(build_dir, remote_path, server, user, password, use_ssh_key=False, ssh_key_path=None):
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        if use_ssh_key:
            ssh.connect(server, username=user, key_filename=ssh_key_path)
        else:
            ssh.connect(server, username=user, password=password)

        # Create an SCP client
        with SCPClient(ssh.get_transport()) as scp:
            # Copy files to the remote server
            scp.put(build_dir, remote_path, recursive=True)
        
        print(f"Project deployed to remote server {server}:{remote_path}")
    except Exception as e:
        print(f"Failed to deploy to remote server: {e}")
    finally:
        ssh.close()

# Main deployment function
def deploy(build_dir, deploy_dir, remote=False):
    if remote:
        deploy_to_remote(build_dir, REMOTE_PATH, REMOTE_SERVER, REMOTE_USER, REMOTE_PASSWORD, USE_SSH_KEY, SSH_KEY_PATH)
    else:
        deploy_locally(build_dir, deploy_dir)

# Run deployment
deploy(BUILD_DIR, DEPLOY_DIR, remote=True)  # Set `remote=True` to deploy to a remote server