docker build -t flask_app "$( cd "$(dirname "$0")" ; pwd -P )"
docker run --network host -v "$( cd "$(dirname "$0")" ; pwd -P )"/config:/app/config flask_app
