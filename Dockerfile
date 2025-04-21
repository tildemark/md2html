FROM python:3.9-slim-buster

WORKDIR /app

# Install necessary Python packages
COPY md2html/requirements.txt .
RUN pip install -r requirements.txt

# Copy your conversion script and webhook receiver
COPY md2html/convert_manuals.py .
COPY md2html/webhook_receiver.py .

# Copy your Gitea repository (mount as a volume in production for dynamic updates)
COPY md2html/manuals /app/manuals/

# Create the output HTML directory inside the container
RUN mkdir /app/html

# Expose the port for the webhook receiver (if applicable)
EXPOSE 5000

# Command to run the webhook receiver (or a scheduler)
CMD ["python3", "webhook_receiver.py"]