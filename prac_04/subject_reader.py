FILENAME = "subject_data.txt"

def main():
    """Load and display subject details from a file."""
    data = load_data(FILENAME)
    display_subject_details(data)

def load_data(filename):
    """Load subject data from file and return as a list of [code, lecturer, students]."""
    subject_data = []
    with open(filename) as file:
        for line in file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  
            subject_data.append(parts)
    return subject_data

def display_subject_details(data):
    """Print subject info in a formatted way."""
    for subject in data:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")

main()
