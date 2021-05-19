def P1_ans(filename: str) -> list:
    out_list = []
    with open(filename, 'r') as input_file:
        # For each line in input_file
        for line in input_file.readlines():
            # Remove any blank or new line at the end of the line character,then split by ' '
            line_strip = line.strip().split(' ')
            '''
            # This is not required... for grading purpose.
            for element in line_strip:
                if isinstance(element, numbers.Number):
                    element = float(element)
            '''
            out_list.append(line_strip)
    return out_list


def P2_ans(filename: str) -> list:
    with open(filename, 'r') as input_file:
        # Get input lines as list
        fromLast = input_file.readlines()
        # Reverse the order of the list
        fromLast.reverse()
    return fromLast


def P3_ans(filename: str) -> list:
    out = []
    with open(filename, 'r') as input_file:
        for line in input_file.readlines():
            # Skip any lines starting with '// or '#'
            if line.startswith('//') or line.startswith('#'):
                continue
            # Split by #, then retrieve only the first elemnet of the resulting list
            line_rmcmt = line.strip().split('#')
            out.append(line_rmcmt[0].strip())
    return out


def P4_ans(input_filename: str, out_filename: str):
    with open(input_filename, 'r') as input_file:
        with open(out_filename, 'w') as output_file:
            for line in input_file.readlines():
                # For each line of input file, split by ' '
                # Then, join them with ',' ['A','B','C'] -> 'A,B,C'
                new_line = ','.join(line.strip().split(' '))
                # Attach new line charater at the end of the line.
                new_line += '\n'
                # Write on the output file
                output_file.write(new_line)


def P5_ans(input_filename: str, out_filename):
    with open(input_filename, 'r') as input_file:
        with open(out_filename, 'w') as output_file:
            for line in input_file.readlines():
                # Skip any lines starting with '//'
                if line.startswith('//'):
                    continue
                line = line.strip()
                # If starting with '#', retrieve from second elements
                # '#abcde' -> 'abcde'
                if line.startswith('#'):
                    line = line[1:]
                # For any comment mark, split by '#' and write each element as one line.
                line_rmcmt = line.split('#')
                for item in line_rmcmt:
                    output_file.write(item + '\n')
