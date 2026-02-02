import hashlib
import time

# Sample user database (username: [password_hash, role])
user_db = {
    "admin": [hashlib.sha256("admin123".encode()).hexdigest(), "Administrator"],
    "john": [hashlib.sha256("john456".encode()).hexdigest(), "Developer"],
    "emma": [hashlib.sha256("emma789".encode()).hexdigest(), "Intern"]
}

# Approved devices per user
approved_devices = {
    "admin": ["Laptop-01", "Secure-VM"],
    "john": ["Dev-Laptop-17"],
    "emma": ["Intern-PC-3"]
}

# Simulated security policies (Role-based access)
access_policies = {
    "Administrator": ["read", "write", "delete", "config"],
    "Developer": ["read", "write"],
    "Intern": ["read"]
}

# Logger
def log_access(username, device, action, status):
    with open("access_log.txt", "a") as log:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {username} - {device} - {action} - {status}\n")

# Authentication Function
def authenticate(username, password):
    if username in user_db:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return password_hash == user_db[username][0]
    return False

# Device Validation Function
def validate_device(username, device_id):
    return device_id in approved_devices.get(username, [])

# Access Control Function
def authorize(username, action):
    role = user_db[username][1]
    return action in access_policies.get(role, [])

# Main Program
if __name__ == "__main__":
    print("Zero Trust Access System")
    username = input("Username: ")
    password = input("Password: ")

    if authenticate(username, password):
        device_id = input("Enter Device ID: ")
        if validate_device(username, device_id):
            action = input("Requested action (read/write/delete/config): ").lower()
            if authorize(username, action):
                print("Access granted for", action)
                log_access(username, device_id, action, "GRANTED")
            else:
                print("Access denied: Insufficient privileges.")
                log_access(username, device_id, action, "DENIED - ROLE")
        else:
            print("Access denied: Unrecognized device.")
            log_access(username, "UNKNOWN", "N/A", "DENIED - DEVICE")
    else:
        print("Authentication failed.")
        log_access("UNKNOWN", "UNKNOWN", "N/A", "DENIED - AUTH")
