#!/usr/bin/env python
"""
Load Django fixture data with foreign key constraints disabled.
This avoids the '__old' table issues during migration from MySQL to SQLite.
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, '/Users/michele.pasin/dev2/research_portal_2019/researcher/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from django.core.management import call_command
from django.db import connection

print("Disabling foreign key constraints...")
with connection.cursor() as cursor:
    cursor.execute('PRAGMA foreign_keys = OFF;')

print("Loading fixture data...")
try:
    call_command('loaddata', '/Users/michele.pasin/dev2/research_portal_2019/researcher/mysql_data_backup.json', verbosity=2)
    print("\nData loaded successfully!")
except Exception as e:
    print(f"\nError loading data: {e}")
    sys.exit(1)

print("Re-enabling foreign key constraints...")
with connection.cursor() as cursor:
    cursor.execute('PRAGMA foreign_keys = ON;')

print("Done!")
