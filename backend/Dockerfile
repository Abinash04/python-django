FROM python:3.9-slim
RUN pip install --upgrade pip
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /code/
RUN python -m django --version
