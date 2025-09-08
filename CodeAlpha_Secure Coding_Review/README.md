# CodeAlpha_Secure_Coding_Task 3

## Overview

This repository contains a review of the secure coding practices implemented in an open-source application chosen for an intern task at CodeAlpha. The task involved selecting an open-source application and conducting a manual security review process. The primary objective of this review is to identify security vulnerabilities within the codebase and offer recommendations for enhancing secure coding practices.

## Task Requirements

- Choose an open-source application to review.
- Conduct a thorough review of the codebase to identify security vulnerabilities.
- Provide detailed recommendations for implementing secure coding practices.
- Utilize manual code reviews to assess the codebase.

## Application Description

Bike Showroom Management
System, a web application developed using Django (Python framework) with a

MySQL database backend. The system allows users to browse available bikes,
register or log in, book vehicles, and manage basic operations of a bike showroom. 

## Security Review
The security review process involved a meticulous examination of the codebase
using manual code review techniques. Identified vulnerabilities were categorized,
documented, and analyzed to provide actionable recommendations for implementing
robust secure coding practices

## Recommendations

- * * Secure Configuration

• Always set DEBUG = False in production to prevent sensitive error messages
from being exposed.
• Configure ALLOWED_HOSTS explicitly with the domain name or server IP to
block host header attacks.
• Enforce HTTPS by enabling Django’s SecurityMiddleware and setting:
o SECURE_SSL_REDIRECT = True
o SESSION_COOKIE_SECURE = True

- * * Secrets Management
• Store sensitive information such as SECRET_KEY, database credentials, and
API keys in environment variables or a secure vault (e.g., python-decouple,
django-environ).
• Never commit secrets to version control (e.g., GitHub).

- * * Logging and Monitoring
• Enable structured logging of security events (failed logins, suspicious activity).
• Monitor application and server logs for anomalies.
• Use tools like fail2ban or intrusion detection systems to block repeated attack
attempts.

## Conclusion

The secure coding review of the Django Bike Showroom Management System
highlighted several important areas for improvement
, particularly in terms of
application configuration and dependency management. Critical issues such as
leaving DEBUG=True in production and hardcoding the SECRET_KEY were identified,
both of which could lead to sensitive data disclosure if left unaddressed. Additionally,
the absence of certain HTTP security headers (HSTS, CSP) and reliance on
outdated dependencies present risks that should be remediated promptly.t, particularly in terms of
application configuration and dependency management. Critical issues such as
leaving DEBUG=True in production and hardcoding the SECRET_KEY were identified,
both of which could lead to sensitive data disclosure if left unaddressed. Additionally,
the absence of certain HTTP security headers (HSTS, CSP) and reliance on
outdated dependencies present risks that should be remediated promptly.

By implementing the recommended fixes and following secure coding best practices,
the Bike Showroom system can significantly enhance its security posture. 

## Resources

Django Documentation – Security Topics:
https://docs.djangoproject.com/en/stable/topics/security/
• Django Deployment Checklist:
https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
• OWASP Top Ten Web Application Security Risks: https://owasp.org/wwwproject-top-ten/
• Bandit – Python Security Linter: https://bandit.readthedocs.io
• pip-audit – Python Dependency Vulnerability Scanner:
https://pypi.org/project/pip-audit/
• NIST National Vulnerability Database (NVD): https://nvd.nist.gov/
• Mozilla Observatory – HTTP Security Headers Guide:
https://observatory.mozilla.org/