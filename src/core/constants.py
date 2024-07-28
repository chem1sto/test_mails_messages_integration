class EmailConfig:
    """
    Настройки для модели Email.
    """
    SUBJECT_MAX_LENGTH = 255
    SUBJECT_VERBOSE_NAME = "Тема сообщения"
    DATE_OF_RECEIPT_VERBOSE_NAME = "Дата получения письма"
    DATE_OF_DISPATCH_VERBOSE_NAME = "Дата отправки письма"
    BODY_MAX_LENGTH = 5000
    BODY_VERBOSE_NAME = "Описание или текст письма"
    INCLUDED_FILES_VERBOSE_NAME = "Прикреплённые файлы"


class EmailAccountConfig:
    """
    Настройки для модели EmailAccount.
    """
    EMAIL = "email"
    EMAIL_VERBOSE_NAME = "Электронная почта"
    EMAIL_HELP_TEXT = "Введите адрес электронной почты"
    PASSWORD = "password"
    PASSWORD_MAX_LENGTH = 128
    PASSWORD_VERBOSE_NAME = "Пароль"
    PASSWORD_HELP_TEXT = "Введите пароль от электронной почты"
    UNIQUE_EMAIL_PASSWORD_NAME = "unique_email_password"
