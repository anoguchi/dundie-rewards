import argparse


def load(filepath):
    """Load the file at the given filepath to the database."""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found: {e}")


def main():

    parser = argparse.ArgumentParser(
        description="Dundie Mifflin Rewards CLI", epilog="Enjoy and use with caution."
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="Subcommand to execute",
        choices=("load", "show", "send"),
        default="help",
    )
    parser.add_argument(
        "filepath", type=str, help="Path to the file to load", default="none"
    )
    args = parser.parse_args()

    globals()[args.subcommand](args.filepath)


if __name__ == "__main__":
    main()
