from sys import exit
from time import sleep
from argparse import ArgumentParser
from Common.Email.Python.writer import EmailWriter

# Constants
TO_ADDR = "nelsonb1212@gmail.com"
FROM_SUBJECT = "Automation - DO_NOT_REPLY"
FROM_BODY = "I'm a bot :D"
TEST_DICT = {
    "To": TO_ADDR,
    "Subject": FROM_SUBJECT,
    "Body": FROM_BODY
}


def test_one():
    """Writes a single email"""
    print("Starting Email Test #1..")
    email = EmailWriter(TEST_DICT)
    email.write_email()
    return


def test_two(num_emails=5, wait=10):
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
        email = EmailWriter(TEST_DICT)
        email.write_email()

        # Increment counters
        sent += 1

        # Sleep
        print("Sleeping {} seconds before trying again..".format(wait))
        sleep(wait)

    return


def test_runner(test_number):
    tests = {1: test_one,
             2: test_two}

    return tests[test_number]()


def parse_args():
    p = ArgumentParser()
    p.add_argument("-tn", "--test_number", type=int, required=True, choices=(1, 2))
    return p.parse_args()


def main():
    # Parse Arguments
    args = parse_args()

    # Run a test
    test_runner(args.test_number)

    # Exit
    exit(0)


if __name__ == "__main__":
    main()
