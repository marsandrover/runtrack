import argparse
from datetime import datetime
from database import insert_run, get_all_runs, update_run_date

def list_runs():
    runs = get_all_runs()
    if runs:
        print("List of Runs:")
        for run in runs:
            print(f"ID: {run[0]}, Distance: {run[1]}, Duration: {run[2]}, Date: {run[3]}")
    else:
        print("No runs found.")

def add_run(distance, duration, date):
    insert_run(distance, duration, date)
    print("Run added successfully.")

def update_date(run_id, new_date):
    update_run_date(run_id, new_date)
    print(f"Date updated successfully for run ID {run_id}.")

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Running Tracker')

    # Define the subcommands
    subparsers = parser.add_subparsers(dest='command')

    # Define the 'list' subcommand
    parser_list = subparsers.add_parser('list', help='List all run records')

    # Define the 'add' subcommand
    parser_add = subparsers.add_parser('add', help='Add a new run record')
    parser_add.add_argument('distance', help='Distance of the run')
    parser_add.add_argument('duration', help='Duration of the run')
    parser_add.add_argument('date', help='Date of the run (format: dd/mm/yyyy)')

    # Define the 'update' subcommand
    parser_update = subparsers.add_parser('update', help='Update the date for a run record')
    parser_update.add_argument('run_id', help='ID of the run to update')
    parser_update.add_argument('new_date', help='New date for the run (format: dd/mm/yyyy)')

    # Parse the command-line arguments
    args = parser.parse_args()

    if args.command == 'list':
        list_runs()
    elif args.command == 'add':
        add_run(args.distance, args.duration, datetime.strptime(args.date, '%d/%m/%Y').date())
    elif args.command == 'update':
        update_date(int(args.run_id), datetime.strptime(args.new_date, '%d/%m/%Y').date())
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
