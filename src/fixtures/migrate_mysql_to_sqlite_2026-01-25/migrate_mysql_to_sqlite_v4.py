#!/usr/bin/env python
"""
Direct migration from MySQL to SQLite using raw connections.

Backup version. Run on 2026-01-25 from project top level. 
"""
import os
import sys
import sqlite3

# Setup paths
sys.path.insert(0, '/Users/michele.pasin/dev2/research_portal_2019/researcher/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Configure both databases
from django.conf import settings
settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'researcher2021',
        'USER': 'root',
        'PASSWORD': 'mikele',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'mysql_source': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'researcher2021',
        'USER': 'root',
        'PASSWORD': 'mikele',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

import django
django.setup()

from django.db import connections

print("Starting direct migration from MySQL to SQLite...")
print("=" * 60)

# Get MySQL cursor
mysql_cursor = connections['mysql_source'].cursor()

# Get raw SQLite connection
sqlite_db_path = '/Users/michele.pasin/dev2/research_portal_2019/researcher/db.sqlite3'
sqlite_conn = sqlite3.connect(sqlite_db_path)
sqlite_cursor = sqlite_conn.cursor()

# Disable foreign key constraints in SQLite
print("\nDisabling SQLite foreign key constraints...")
sqlite_cursor.execute('PRAGMA foreign_keys = OFF;')

# Simple table copy function
def copy_table(table_name):
    print(f"   - Copying {table_name}...")

    # Get all data from MySQL
    mysql_cursor.execute(f"SELECT * FROM {table_name}")
    rows = mysql_cursor.fetchall()

    if not rows:
        print(f"     (no data)")
        return

    # Get column names
    columns = [desc[0] for desc in mysql_cursor.description]

    # Build INSERT statement for SQLite
    placeholders = ','.join(['?' for _ in columns])
    col_names = ','.join([f'`{c}`' for c in columns])
    insert_sql = f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"

    # Insert each row
    for row in rows:
        sqlite_cursor.execute(insert_sql, row)

    print(f"     ✓ {len(rows)} rows")

print("\n1. Copying auth tables...")
copy_table('auth_user')
copy_table('auth_user_groups')
copy_table('auth_user_user_permissions')

print("\n2. Copying authority lists...")
copy_table('researchapp_pubtypegroup')
copy_table('researchapp_pubtype')
copy_table('researchapp_generictype')
copy_table('researchapp_tag')
copy_table('researchapp_blogcategory')

print("\n3. Copying main objects...")
copy_table('researchapp_person')
copy_table('researchapp_project')
copy_table('researchapp_publication')
copy_table('researchapp_item')

print("\n4. Copying relationships...")
copy_table('researchapp_authorship')
copy_table('researchapp_publication_tags')
copy_table('researchapp_publication_categories')
copy_table('researchapp_project_tags')

# Re-enable foreign key constraints
print("\nRe-enabling SQLite foreign key constraints...")
sqlite_cursor.execute('PRAGMA foreign_keys = ON;')

# Commit and close
sqlite_conn.commit()
sqlite_conn.close()

print("\n" + "=" * 60)
print("✓ Migration completed successfully!")
print(f"\nSQLite database: {sqlite_db_path}")
print("\nVerifying data counts...")

# Reconnect to verify
from django.contrib.auth.models import User
from researchapp.models import (
    PubType, Tag, Person, Publication, Authorship, Project, Item
)

# Update settings to use SQLite
settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': sqlite_db_path,
    }
}

# Close all connections and reconnect
connections.close_all()

models_to_check = [
    ('Users', User),
    ('Publication Types', PubType),
    ('Tags', Tag),
    ('Persons', Person),
    ('Publications', Publication),
    ('Authorships', Authorship),
    ('Projects', Project),
    ('Items', Item),
]

for name, model in models_to_check:
    count = model.objects.count()
    print(f"   {name}: {count}")

print("\n✓ Migration verification complete!")
print("\nYou can now use the SQLite database in your application.")
