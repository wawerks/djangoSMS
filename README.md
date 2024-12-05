# DjangoSMS

DjangoSMS is a Django-based application for sending and managing SMS messages efficiently. It provides a simple interface to integrate SMS functionality into your Django projects.

## Features

- Send SMS messages via supported gateways.
- Manage SMS templates for consistent communication.
- Track SMS logs for monitoring sent messages.
- Supports multiple SMS providers with easy configuration.

## Requirements

- Python 3.8+
- Django 3.2+

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/wawerks/djangoSMS.git
   cd djangoSMS
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Configuration

1. **Add the app to your Django project**:
   Add `djangoSMS` to the `INSTALLED_APPS` list in your `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'djangoSMS',
   ]
   ```

2. **Configure SMS Gateway**:
   Add your SMS provider settings to the `scores/models.py` file. Example for a generic gateway:
   ```python
            # Your Auth Token from twilio.com/console
            account_sid = "ACc7e5f9c7b69dc3219b0c973c8b17aa6f"
            auth_token  = "007efaaa8be27c0dd907720791683f0a"
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=f"(Your Message Here)",
                from_="Twilio Trial Number",
                to="Your registred number in twilio",
            )
   ```

## Usage

1. **Send an SMS**:
   Use the provided function to send SMS messages:
   ```python
   from djangoSMS.utils import send_sms

   send_sms(
       phone_number="+1234567890",
       message="Hello, this is a test message!"
   )
   ```

2. **Manage Templates**:
   Create and use predefined SMS templates in the admin panel for consistency.

3. **View SMS Logs**:
   Monitor sent messages and their statuses through the built-in logging feature.

## Testing

Run the test suite to ensure the application is functioning as expected:
```bash
python manage.py test
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [Your Name](mailto:youremail@example.com) or visit the [repository](https://github.com/wawerks/djangoSMS).
