FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

COPY records.py ${LAMBDA_TASK_ROOT}

COPY records.joblib ${LAMBDA_TASK_ROOT}

COPY model.joblib ${LAMBDA_TASK_ROOT}

COPY praw.ini ${LAMBDA_TASK_ROOT}


# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_function.lambda_handler" ]