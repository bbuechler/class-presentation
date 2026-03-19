import os

# invalid_variable = f"Good Job - {os.getenv('USER', 'unknown')}!"

print(f"This should fail checks - {invalid_variable}")
