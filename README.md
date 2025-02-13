# New Boilerplate Repo

##  Running the App with Docker

1. **Build the Docker image**  
   ```bash
   docker build -t boilerplate_app .
   ```

2. **Run the Docker container**  
   ```bash
   docker run -p 8000:8000 boilerplate_app
   ```


## Publishing the Docker Image

1. **Log in to Docker Hub**  
   ```bash
   docker login
   ```

2. **Tag the Docker image**  
   ```bash
   docker tag boilerplate_app agutierrez4/boilerplate_app:latest
   ```

3. **Push the Docker image to Docker Hub**  
   ```bash
   docker push agutierrez4/boilerplate_app:latest
   ```
