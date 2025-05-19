FROM python:3.11.12-slim

# Upgrade pip
RUN pip install --upgrade pip

# Set working directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install Pillow

# Copy project files
COPY ./src /code/src

# Optional: copy model if not inside `src/`
COPY ./src/pred/models/Trafic_signs_model.keras /code/Trafic_signs_model.keras

# Launch app
CMD ["python", "src/main.py"]