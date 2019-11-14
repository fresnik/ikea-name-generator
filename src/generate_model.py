from Markov import TransitionMatrix

# Trademark names retrieved from https://www.google.com/googlebooks/uspto-trademarks-recent-applications.html
# Ikea names retrieved from https://github.com/jleinonen/ikea-names
# Wikipedia article names retrieved from https://dumps.wikimedia.org/simplewiki/20191020/

file_names = ['data/ikea_names.txt']
matrix_filename = 'ikea_name_matrix'
matrix = TransitionMatrix(matrix_filename)
key_delimiter = '---'

if __name__ == '__main__':
	count = 0

	for file_name in file_names:
		with open(file_name, 'r') as f:
			title = f.readline().strip()
			while title:
				matrix.add_transition(key_delimiter, title[0])
				if len(title) > 1:
					matrix.add_transition(key_delimiter, title[0:2])

				for i in range(len(title) - 1):
					# Add transition from current letter to next letter
					matrix.add_transition(title[i], title[i+1])

					if i < len(title) - 2:
						# Add transition from current letter to next bigraph
						matrix.add_transition(title[i], title[i+1:i+3])

						# Add transition from current bigraph to next letter
						matrix.add_transition(title[i:i+2], title[i+2])

					if i < len(title) - 3:
						# Add transition from current bigraph to next bigraph
						matrix.add_transition(title[i:i+2], title[i+2:i+4])

						# Add transition from current letter to next trigraph
						matrix.add_transition(title[i], title[i+1:i+4])

						# Add transition from current trigraph to the next letter
						matrix.add_transition(title[i:i+3], title[i+3])

					if i < len(title) - 4:
						# Add transition from current bigraph to next trigraph
						matrix.add_transition(title[i:i+2], title[i+2:i+5])

						# Add transition from current trigraph to next bigraph
						matrix.add_transition(title[i:i+3], title[i+3:i+5])

					if i < len(title) - 5:
						# Add transition from current trigraph to next trigraph
						matrix.add_transition(title[i:i+3], title[i+3:i+6])

					if i == len(title) - 3:
						# Add transition from current trigraph to end
						matrix.add_transition(title[i:i+3], key_delimiter)

					if i == len(title) - 2:
						# Add transition from current bigraph to end
						matrix.add_transition(title[i:i+2], key_delimiter)

					if i == len(title) - 1:
						# Add transition from current letter to end
						matrix.add_transition(title[i], key_delimiter)

				title = f.readline().strip()

			count += 1

	matrix.save()

	print(f'Successfully saved matrix as {matrix_filename}.json and {matrix_filename}_norm.json')