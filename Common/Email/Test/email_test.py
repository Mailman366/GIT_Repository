from sys import exit
from time import sleep
from argparse import ArgumentParser
from Common.Email.Python.writer import EmailWriter

# Constants
FROM_SUBJECT = "Automation - DO_NOT_REPLY"
FROM_BODY = "I'm a bot :D"


def test_one(test_dict):
    """Writes a single email"""
    print("Starting Email Test #1..")
    email = EmailWriter(test_dict)
    email.write_email()
    return


def test_two(test_dict, num_emails=5, wait=10):
    """
    Description:
        Sends a total of num_emails waiting "wait" each time

    Args:
        num_emails (int)
        wait(int) - seconds
    """
    print("Starting Email Test #2..")
    to_send = num_emails
    sent = 1

    for i in range(num_emails):
        print("Sending email {} of {}..".format(sent, to_send))
        email = EmailWriter(test_dict)
        email.write_email()

        # Increment counters
        sent += 1

        # Sleep
        print("Sleeping {} seconds before trying again..".format(wait))
        sleep(wait)

    return


def test_runner(test_dict, test_number):
    tests = {1: test_one,
             2: test_two}

    return tests[test_number](test_dict)


def parse_args():
    p = ArgumentParser()
    p.add_argument("-tn", "--test_number", type=int, required=True, choices=(1, 2))
    p.add_argument("-ta", "--to_address", type=str, required=True)
    return p.parse_args()


def main():
    # Parse Arguments
    args = parse_args()

    # Run a test
    to_address = args.to_address
    test_dict = {
        "To": to_address,
        "Subject": FROM_SUBJECT,
        "Body": FROM_BODY
    }

    test_runner(test_dict, args.test_number)

    # Exit
    exit(0)


if __name__ == "__main__":
    main()
