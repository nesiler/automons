import cli.cli_parser as cli
import cli.commands as commands


def main():
    # Parse the command-line arguments
    args = cli.parse_args()

    # Process the arguments and execute the corresponding command
    commands.process_arguments(args)


if __name__ == "__main__":
    main()
