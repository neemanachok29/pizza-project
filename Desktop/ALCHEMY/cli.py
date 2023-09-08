import click
from utils import create_database
from models import User, Event, Base
from sqlalchemy import create_engine
from datetime import datetime


@click.group()
def cli():
    pass

@click.command()
@click.option('--db-uri', default='sqlite:///database.py', help='Database URI')
def initdb(db_uri):
    """Create a new database."""
    create_database(db_uri)
    click.echo('Initialized the database.')

@click.command()
@click.option('--db-uri', default='sqlite:///database.py', help='Database URI')
def dropdb(db_uri):
    """Drop the database."""
    engine = create_engine(db_uri)
    Base.metadata.drop_all(engine)
    click.echo('Dropped the database.')

@click.command()
@click.option('--db-uri', default='sqlite:///database.py', help='Database URI')
def create_tables(db_uri):
    """Create tables."""
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    click.echo('Created tables.')

@click.command()
@click.option('--db-uri', default='sqlite:///database.py', help='Database URI')
@click.option('--username', prompt='Enter username', help='Username for the new user')
def add_user(db_uri, username):
    """Add a new user."""
    session = create_database(db_uri)
    user = User(username=username)
    session.add(user)
    session.commit()
    click.echo(f'User "{username}" added successfully.')

@click.command()
@click.option('--db-uri', default='sqlite:///database.py', help='Database URI')
@click.option('--title', prompt='Enter title', help='Title of the event')
@click.option('--description', prompt='Enter description', help='Description of the event')
@click.option('--start-date', prompt='Enter start date (YYYY-MM-DD)', help='Start date of the event (YYYY-MM-DD)')
@click.option('--end-date', prompt='Enter end date (YYYY-MM-DD)', help='End date of the event (YYYY-MM-DD)')
@click.option('--user-id', prompt='Enter user ID', type=int, help='User ID associated with the event')
def add_event(db_uri, title, description, start_date, end_date, user_id):
    """Add a new event."""
    session = create_database(db_uri)

    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

    event = Event(title=title, description=description, start_date=start_date, end_date=end_date, user_id=user_id)
    session.add(event)
    session.commit()
    click.echo(f'Event "{title}" added successfully.')

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(create_tables)
cli.add_command(add_user)
cli.add_command(add_event)

if __name__ == '__main__':
    cli()
