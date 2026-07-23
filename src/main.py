from ruff import lint
import sys

def main():
    try:
        lint.run(sys.argv[1:])
    except SystemExit as e:
        sys.exit(e.code)

if __name__ == '__main__':
    main()