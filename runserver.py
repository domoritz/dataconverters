#!/usr/bin/env python


from raven import app, configure


def main():
    configure()
    app.run()


if __name__ == '__main__':
    main()
