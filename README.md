# TrustNoOne – Zero Trust Architecture Mini Project

This mini project demonstrates Zero Trust security principles where
no user or device is trusted by default.

## Features
- User authentication using hashed passwords (SHA-256)
- Device validation per user
- Role-based access control (Admin, Developer, Intern)
- Access logging for auditing

## Access Flow
1. User enters credentials
2. Device ID is validated
3. Action is checked against role policies
4. Access is granted or denied and logged

## Technologies Used
- Python
- Hashlib (SHA-256)
- Zero Trust Architecture concepts
