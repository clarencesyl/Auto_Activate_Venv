import os

# Edit path to venv folder accordingly.
venv_path = "D:/Github_Projects/venv/Scripts"

# Comment out and/or make changes accordingly depending on where venv folder is located.
# Quotations must be single followed by double. e.g. ' " " '.
os.system('start cmd /k "cd {} & activate"'.format(venv_path))  # Venv folder in C: drive.
os.system('start cmd /k "echo ok & {} & cd {} & activate"'.format("d:", venv_path))  # Venv folder in other drive e.g. D: drive.


# Written by: Clarence Seah
