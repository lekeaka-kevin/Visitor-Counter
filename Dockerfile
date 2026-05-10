# Start from AWS's official Lambda Python image
FROM public.ecr.aws/lambda/python:3.12

# Copy your requirements file into the container
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the Python packages
RUN pip install -r requirements.txt

# Copy your actual code into the container
COPY app.py ${LAMBDA_TASK_ROOT}

# Tell Lambda which function to run
CMD [ "app.lambda_handler" ]
