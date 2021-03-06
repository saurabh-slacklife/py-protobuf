#!/bin/sh
  # Start Gunicorn processes
  echo "Starting Gunicorn."
  echo "Application log path: /var/log/proto/application.log"
  echo "Access log path: /var/log/proto/access.log"
  
  mkdir -p /var/log/proto
  touch /var/log/proto/access.log
  touch /var/log/proto/application.log
  
  exec gunicorn --bind "0.0.0.0:5000" app.io.slacklife:flask_app \
    --log-syslog \
    --capture-output \
    --log-file /var/log/proto/application.log \
    --access-logfile /var/log/proto/access.log \
    --log-level info