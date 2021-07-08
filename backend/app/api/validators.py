from rest_framework import serializers


def school_class_label_validator(class_label):
    if not class_label.isalpha():
        raise serializers.ValidationError('class_label must be letter from alphabet')
    return class_label.upper()
