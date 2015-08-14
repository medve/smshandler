*SMSHandler* - Base Handler class.

Every handler must have send method implementation;

Every handler must have SMS centre address.

If login or password is None then send request to sms centre without this parameters.

### Settings:

`SMS_GATES = {`

    `"<handler_name>":{`

        `"address":"<address>",`

    `},`

    `"<handler_name>":{`

        `"address":"<address>",`

        `"login":"<login>",`

        `"password":"<password>",`

    `},`

    `"<handler_name>":{`

        `"address":"<address>",`

        `"login":"<login>",`

        `"password":"<password>",`

        `"field_names":{`

            `"login_field_name":"<login_field_name>",`

            `"password_field_name":"<password_field_name>",`

             `...`

        `}`

    `},`

`}`

*get_handler_by_name(handler_name)* - Use it for getting handlers that was defined in settings.SMS_GATES

*get_handler(address, login = None, password = None, **kwargs)* - Use it for creating your handlers right in code.
