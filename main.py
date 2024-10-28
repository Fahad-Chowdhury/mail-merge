import os


class MailMerge():

    def __init__(self):
        self.mail_text = None
        self.receipients = []
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self._get_starting_letter()
        self._get_receipients()

    def _read_file(self, filepath, readlines=False):
        """ It reads contents from a file. It reads the conents as a list of
        strings if readlines is set to True, else it reads the contents to
        a string. """
        file_content = ""
        abs_filepath = os.path.join(self.current_dir, filepath)
        with open(abs_filepath) as file:
            if readlines:
                file_content = file.readlines()
            else:
                file_content = file.read()
        return file_content

    def _write_file(self, filepath, text):
        """ It writes text to a file with 'filepath'. """
        abs_filepath = os.path.join(self.current_dir, filepath)
        with open(abs_filepath, "w") as file:
            file.write(text)

    def _get_starting_letter(self):
        """ Reads the starting letter from 'Input/Letters/starting_letter.txt'. """
        filepath = "Input/Letters/starting_letter.txt"
        self.mail_text = self._read_file(filepath)

    def _get_receipients(self):
        """ Read the receipients of the mail from 'Input/Names/invited_names.txt' """
        filepath = "Input/Names/invited_names.txt"
        receipients = self._read_file(filepath, readlines=True)
        self.receipients = [receipient.strip() for receipient in receipients]

    def generate_mails(self):
        """ It generates mails using the 'starting_letter.txt' file for each name in the
        'invited_names.txt' file by replacing the [name] placeholder with the actual name.
        The letters are saved in the folder 'ReadyToSend'. """
        for receipient in self.receipients:
            message = self.mail_text.replace("[name]", receipient)
            filepath = f"Output/ReadyToSend/letter_for_{receipient}.txt"
            print(f"Generating '{filepath}' file . . .")
            self._write_file(filepath, message)


def main():
    """ Main method for mail merge.  """
    mail = MailMerge()
    mail.generate_mails()


if __name__ == "__main__":
    main()
