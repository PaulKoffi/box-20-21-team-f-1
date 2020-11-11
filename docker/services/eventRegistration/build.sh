echo "Building eventRegistration docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../services/eventRegistration/. resources
docker build -t djotiham/event_registration_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
