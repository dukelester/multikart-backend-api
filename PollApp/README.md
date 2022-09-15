# Launching the app

Before launching the app we need to build the image first. From the root of your project run `docker build -t poll-app .`

Now we can launch the container: `docker run -it -p 80:80 -v "$(pwd)"/app:/app poll-app.`
This will also mount our app directory so we don't have to recreate it each time we edit the files