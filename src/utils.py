from typing import List

def load_data(file_path: str) -> List[float]:
    with open(file_path, 'r') as file:
        data = [float(line.strip()) for line in file]
        return data

def save_data(data: List[float], file_path: str):
    with open(file_path, 'w') as file:
        for value in data:
            file.write(str(value) + '\n')