MailboxValidator API
====================

EmailValidation(api_key)
------------------------

Creates a new instance of the MailboxValidator object with the API key.

validate_email(email_address)
-----------------------------

Performs email validation on the supplied email address.

Return Fields
~~~~~~~~~~~~~

+---------------------------------+------------------------------------+
| Field Name                      | Description                        |
+=================================+====================================+
| email_address                   | The input email address.           |
+---------------------------------+------------------------------------+
| domain                          | The domain of the email address.   |
+---------------------------------+------------------------------------+
| is_free                         | Whether the email address is from  |
|                                 | a free email provider like Gmail   |
|                                 | or Hotmail. Return values: True,   |
|                                 | False                              |
+---------------------------------+------------------------------------+
| is_syntax                       | Whether the email address is       |
|                                 | syntactically correct. Return      |
|                                 | values: True, False                |
+---------------------------------+------------------------------------+
| is_domain                       | Whether the email address has a    |
|                                 | valid MX record in its DNS         |
|                                 | entries. Return values: True,      |
|                                 | False, -   (- means not            |
|                                 | applicable)                        |
+---------------------------------+------------------------------------+
| is_smtp                         | Whether the mail servers specified |
|                                 | in the MX records are responding   |
|                                 | to connections. Return values:     |
|                                 | True, False, -   (- means not      |
|                                 | applicable)                        |
+---------------------------------+------------------------------------+
| is_verified                     | Whether the mail server confirms   |
|                                 | that the email address actually    |
|                                 | exist. Return values: True, False, |
|                                 | -   (- means not applicable)       |
+---------------------------------+------------------------------------+
| is_server_down                  | Whether the mail server is         |
|                                 | currently down or unresponsive.    |
|                                 | Return values: True, False, -   (- |
|                                 | means not applicable)              |
+---------------------------------+------------------------------------+
| is_greylisted                   | Whether the mail server employs    |
|                                 | greylisting where an email has to  |
|                                 | be sent a second time at a later   |
|                                 | time. Return values: True, False,  |
|                                 | -   (- means not applicable)       |
+---------------------------------+------------------------------------+
| is_disposable                   | Whether the email address is a     |
|                                 | temporary one from a disposable    |
|                                 | email provider. Return values:     |
|                                 | True, False, -   (- means not      |
|                                 | applicable)                        |
+---------------------------------+------------------------------------+
| is_suppressed                   | Whether the email address is in    |
|                                 | our blacklist. Return values:      |
|                                 | True, False, -   (- means not      |
|                                 | applicable)                        |
+---------------------------------+------------------------------------+
| is_role                         | Whether the email address is a     |
|                                 | role-based email address like      |
|                                 | admin@example.net or               |
|                                 | webmaster@example.net. Return      |
|                                 | values: True, False, -   (- means  |
|                                 | not applicable)                    |
+---------------------------------+------------------------------------+
| is_high_risk                    | Whether the email address contains |
|                                 | high risk keywords. Return values: |
|                                 | True, False, -   (- means not      |
|                                 | applicable)                        |
+---------------------------------+------------------------------------+
| is_catchall                     | Whether the email address is a     |
|                                 | catch-all address. Return values:  |
|                                 | True, False, Unknown, -   (- means |
|                                 | not applicable)                    |
+---------------------------------+------------------------------------+
| mailboxvalidator_score          | Email address reputation score.    |
|                                 | Score > 0.70 means good; score >   |
|                                 | 0.40 means fair; score <= 0.40     |
|                                 | means poor.                        |
+---------------------------------+------------------------------------+
| time_taken                      | The time taken to get the results  |
|                                 | in seconds.                        |
+---------------------------------+------------------------------------+
| status                          | Whether our system think the email |
|                                 | address is valid based on all the  |
|                                 | previous fields. Return values:    |
|                                 | True, False                        |
+---------------------------------+------------------------------------+
| credits_available               | The number of credits left to      |
|                                 | perform validations.               |
+---------------------------------+------------------------------------+
| error_code                      | The error code if there is any     |
|                                 | error. See error table in the      |
|                                 | below section.                     |
+---------------------------------+------------------------------------+
| error_message                   | The error message if there is any  |
|                                 | error. See error table in the      |
|                                 | below section.                     |
+---------------------------------+------------------------------------+

is_disposable_email(email_address)
----------------------------------

Check if the supplied email address is from a disposable email provider.

.. _return-fields-1:

Return Fields
~~~~~~~~~~~~~

+---------------------------------+------------------------------------+
| Field Name                      | Description                        |
+=================================+====================================+
| email_address                   | The input email address.           |
+---------------------------------+------------------------------------+
| is_disposable                   | Whether the email address is a     |
|                                 | temporary one from a disposable    |
|                                 | email provider. Return values:     |
|                                 | True, False                        |
+---------------------------------+------------------------------------+
| credits_available               | The number of credits left to      |
|                                 | perform validations.               |
+---------------------------------+------------------------------------+
| error_code                      | The error code if there is any     |
|                                 | error. See error table in the      |
|                                 | below section.                     |
+---------------------------------+------------------------------------+
| error_message                   | The error message if there is any  |
|                                 | error. See error table in the      |
|                                 | below section.                     |
+---------------------------------+------------------------------------+

is_free_email(email_address)
----------------------------

Check if the supplied email address is from a free email provider.

.. _return-fields-2:

Return Fields
~~~~~~~~~~~~~

+---------------------------------+------------------------------------+
| Field Name                      | Description                        |
+=================================+====================================+
| email_address                   | The input email address.           |
+---------------------------------+------------------------------------+
| is_free                         | Whether the email address is from  |
|                                 | a free email provider like Gmail   |
|                                 | or Hotmail. Return values: True,   |
|                                 | False                              |
+---------------------------------+------------------------------------+
| credits_available               | The number of credits left to      |
|                                 | perform validations.               |
+---------------------------------+------------------------------------+
| error_code                      | The error code if there is any     |
|                                 | error. See error table in the      |
|                                 | below section.                     |
+---------------------------------+------------------------------------+
| error_message                   | The error message if there is any  |
|                                 | error. See error table below.      |
+---------------------------------+------------------------------------+
