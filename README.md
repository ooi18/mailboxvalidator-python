MailboxValidator Python Module
==============================

This Python module enables user to easily validate if an email address is valid, a type of disposable email or free email.

This module can be useful in many types of projects, for example

 - to validate an user's email during sign up
 - to clean your mailing list prior to email sending
 - to perform fraud check
 - and so on


Installation
============

To install this module type the following:

	pip install MailboxValidator


Dependencies
============

An API key is required for this module to function.

Go to https://www.mailboxvalidator.com/plans#api to sign up for FREE API plan and you'll be given an API key.


Online Documentation
=========
A comprehensive online documentation on the available functions can be found from https://ooi18-mailboxvalidator-python.readthedocs.io/en/latest/.


Quickstart
============

## Validate email

```python
import MailboxValidator
	
	mbv = MailboxValidator.EmailValidation('PASTE_API_KEY_HERE')
	results = mbv.validate_email('example@example.com')
	
	if results is None:
		print("Error connecting to API.\n")
	elif results['error_code'] == '':
		print('email_address = ' + results['email_address'] + "\n")
		print('domain = ' + results['domain'] + "\n")
		print('is_free = ' + results['is_free'] + "\n")
		print('is_syntax = ' + results['is_syntax'] + "\n")
		print('is_domain = ' + results['is_domain'] + "\n")
		print('is_smtp = ' + results['is_smtp'] + "\n")
		print('is_verified = ' + results['is_verified'] + "\n")
		print('is_server_down = ' + results['is_server_down'] + "\n")
		print('is_greylisted = ' + results['is_greylisted'] + "\n")
		print('is_disposable = ' + results['is_disposable'] + "\n")
		print('is_suppressed = ' + results['is_suppressed'] + "\n")
		print('is_role = ' + results['is_role'] + "\n")
		print('is_high_risk = ' + results['is_high_risk'] + "\n")
		print('is_catchall = ' + results['is_catchall'] + "\n")
		print('mailboxvalidator_score = ' + str(results['mailboxvalidator_score']) + "\n")
		print('time_taken = ' + str(results['time_taken']) + "\n")
		print('status = ' + results['status'] + "\n")
		print('credits_available = ' + str(results['credits_available']) + "\n")
	else:
		print('error_code = ' + results['error_code'] + "\n")
		print('error_message = ' + results['error_message'] + "\n")
```


## Check if an email is from a disposable email provider

```python
import MailboxValidator
	
	mbv = MailboxValidator.EmailValidation('PASTE_API_KEY_HERE')
	results = mbv.is_disposable_email('example@example.com')
	
	if results is None:
		print("Error connecting to API.\n")
	elif results['error_code'] == '':
		print('email_address = ' + results['email_address'] + "\n")
		print('is_disposable = ' + results['is_disposable'] + "\n")
		print('credits_available = ' + str(results['credits_available']) + "\n")
	else:
		print('error_code = ' + results['error_code'] + "\n")
		print('error_message = ' + results['error_message'] + "\n")
```

## Check if an email is from a free email provider

```python
import MailboxValidator
	
	mbv = MailboxValidator.EmailValidation('PASTE_API_KEY_HERE')
	results = mbv.is_free_email('example@example.com')
	
	if results is None:
		print("Error connecting to API.\n")
	elif results['error_code'] == '':
		print('email_address = ' + results['email_address'] + "\n")
		print('is_free = ' + results['is_free'] + "\n")
		print('credits_available = ' + str(results['credits_available']) + "\n")
	else:
		print('error_code = ' + results['error_code'] + "\n")
		print('error_message = ' + results['error_message'] + "\n")
```

Errors
======

| error_code | error_message |
| ---------- | ------------- |
| 100 | Missing parameter. |
| 101 | API key not found. |
| 102 | API key disabled. |
| 103 | API key expired. |
| 104 | Insufficient credits. |
| 105 | Unknown error. |

Copyright
=========

Copyright (C) 2018-2021 by MailboxValidator.com, support@mailboxvalidator.com
