FROM python:3.12.0-bullseye

RUN apt-get update && apt-get install -y cron 

# Set the working directory
WORKDIR .

# Copy the current directory contents into the container
COPY . .

# Copy and set up the cron job
COPY cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob

# Create a log file to be able to run tail
RUN touch /var/log/cron.log

# Install any needed packages specified in requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV FLASK_APP=main

# Run the application
CMD ["python", "./main.py"]
