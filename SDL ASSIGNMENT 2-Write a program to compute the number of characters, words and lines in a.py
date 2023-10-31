class TextFileAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.num_of_words = 0
        self.num_of_lines = 0
        self.num_of_char = 0
        self.num_of_spaces = 0

    def analyze(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    self.num_of_lines += 1
                    word = 'Y'
                    for letter in line:
                        if letter != ' ' and word == 'Y':
                            self.num_of_words += 1
                            word = 'N'
                        elif letter == ' ':
                            self.num_of_spaces += 1
                            word = 'Y'
                        for i in letter:
                            if i != ' ' and i != '\n':
                                self.num_of_char += 1

            print("Number of words in text file:", self.num_of_words)
            print("Number of lines in text file:", self.num_of_lines)
            print('Number of characters in text file:', self.num_of_char)
            print('Number of spaces in text file:', self.num_of_spaces)
        except FileNotFoundError:
            print('File not found')

# Driver Code:
if __name__ == '__main__':
    filename = 'File1.txt'
    analyzer = TextFileAnalyzer(filename)
    analyzer.analyze()
