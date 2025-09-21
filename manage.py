#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # define o settings padrão se a variável DJANGO_SETTINGS_MODULE não estiver setada
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)