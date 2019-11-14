from Markov import TransitionMatrix
import os

matrix = TransitionMatrix()


def initialize():
    data_filename = os.getenv('NAME_DATA_FILE', 'ikea_name_matrix_norm.json')

    if not os.path.isfile(data_filename):
        raise ValueError(f'Unknown data file "{data_filename}". Set the environment variable NAME_DATA_FILE to an '
                         'existing file.')

    matrix.load_data(data_filename)
    matrix.initialize_chain()


def reset():
    matrix.curr_state = '---'


def generate_name(count: int = 1, max_length: int = 20) -> list:
    if matrix.curr_state is None:
        initialize()

    names = []

    i = 0
    while i < count:
        reset()

        result = []
        next_symbol = matrix.get_next_outcome()
        while next_symbol != '---':
            result.append(next_symbol)
            next_symbol = matrix.get_next_outcome()

        result = ''.join(result)

        if len(result) > max_length:
            continue

        names.append(result)
        i += 1

    return names


if __name__ == '__main__':
    # os.environ['SCM_NAME_DATA_FILE'] = 'data/scm_name_matrix_norm.json'
    print(generate_name())
