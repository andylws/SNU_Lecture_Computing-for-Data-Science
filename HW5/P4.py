"""
**Instruction**
Write P4 function that reads a file and creates another file with different delimeter.
- Assume the input file is delimited with blank(' ').
- Output file has comma(',') as a delimeter
- Assume there is no consecutive blanks in input file. i.e. '  ', '   ', '    ',...  does not appear in the input file.
- Filenames of input and ouput file are entered as input of P4 function
- there is no return value of P4 function
For example, if the input file has below lines, 

beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.327
radium 88 226

output file should look like this.
beryllium,4,9.012
magnesium,12,24.305
calcium,20,20.078
strontium,38,87.62
barium,56,137.327
radium,88,226
"""


def P4(input_filename: str, out_filename: str):
    ##### Write your Code Here #####
    with open(input_filename, 'r') as input_file, open(out_filename, 'w') as output_file:
        lines = input_file.readlines()
        split = []
        linesMade = []

        for line in lines:
            split.append(line.strip('\n').split())

        for line in split:
            linesMade.append(','.join(line))

        result = '\n'.join(linesMade)

        output_file.write(result)

    return
    ##### End of your code #####
