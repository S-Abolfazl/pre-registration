from rest_framework import serializers

class PersianModelserializer(serializers.ModelSerializer):
    deafult_error_messages = default_error_messages = {
        'required': 'این فیلد اجباری است.',
        'invalid': 'مقدار وارد شده نامعتبر است',
        'null': 'این فیلد نمی‌تواند خالی باشد.',
        'blank': 'این فیلد نمی‌تواند خالی باشد.',
        'max_length': 'طول این فیلد نمی‌تواند بیش از {max_length} کاراکتر باشد.',
        'min_length': 'طول این فیلد نمی‌تواند کمتر از {min_length} کاراکتر باشد.',
        'max_value': 'بیشترین مقدار مجاز برای این فیلد {max_value} است.',
        'min_value': 'کمترین مقدار مجاز برای این فیلد {min_value} است.',
        'invalid_type': 'نوع درس وارد شده نامعتبر است. گزینه‌های معتبر: {valid_types}',
        'invalid_choice': "مقدار وارد شده نامعتبر است"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update default error messages for all fields
        for field_name, field in self.fields.items():
            for error_key, error_message in self.default_error_messages.items():
                if error_key in field.error_messages:
                    field.error_messages[error_key] = error_message
        