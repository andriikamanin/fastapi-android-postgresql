
# Open Source Android + PostgreSQL API App

## Overview
This is an open-source project consisting of an Android app and a backend built with FastAPI that connects to a PostgreSQL database. The backend and database are containerized with Docker, and the entire system can be deployed on an AWS EC2 instance.

## Features
- **Android App**: Allows users to create items in a PostgreSQL database via the API.
- **Backend API**: Built with FastAPI, it handles requests from the Android app and interacts with the PostgreSQL database.
- **Dockerized**: Both the backend and database are containerized using Docker, making deployment and management easier.

## Tech Stack
- **Frontend**: Android (Java, Retrofit)
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **DevOps**: Docker, AWS EC2, Docker Compose

## Getting Started

### 1. Setting Up the Backend on AWS

Follow the steps below to set up the server on an AWS EC2 instance.

#### Step 1: Create an EC2 Instance

1. **Launch an EC2 instance** on AWS with Ubuntu 20.04 or later.
2. **Open required ports**: 
   - HTTP (port 80)
   - HTTPS (port 443) (if needed)
   - PostgreSQL (port 5432, for database access)
   - Your API port (default: 8080)

#### Step 2: Install Docker and Docker Compose

On your EC2 instance, run the following commands to install Docker and Docker Compose:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
```

Log out and back in to apply the user group changes.

#### Step 3: Set Up PostgreSQL and FastAPI Backend Using Docker Compose

1. Clone the repository with the Docker setup and API:

    ```bash
    git clone https://github.com/your-repo-url.git
    cd your-repo
    ```

2. In the `docker-compose.yml` file, configure PostgreSQL and FastAPI containers. Ensure the PostgreSQL database settings match your environment, such as `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB`.

3. **Run Docker Compose** to start the containers:
   
    ```bash
    docker-compose up --build
    ```

   This will start both the PostgreSQL database and the FastAPI backend API in containers.

4. Your backend API will be available at `http://<YOUR-AWS-INSTANCE-IP>:8080/`. You can test it by sending HTTP requests using tools like Postman or cURL.

#### Step 4: Access PostgreSQL (Optional)

To access PostgreSQL inside the Docker container, use the following command:

```bash
docker exec -it postgres psql -U your_user -d your_database
```

You can use this to create tables or check data directly.

#### Step 5: Configure SSL (Optional)

If you want your API to be served over HTTPS, you can set up SSL using **Let's Encrypt** or any other SSL provider. For example, you can use **nginx** as a reverse proxy and configure SSL certificates for your API.

For a complete guide, refer to [this tutorial on setting up SSL with Nginx](https://nginx.org/en/docs/http/configuring_https_servers.html).

### 2. Setting Up the Android App

1. **Clone the repository** with the Android app:

    ```bash
    git clone https://github.com/your-repo-url.git
    cd your-repo/android
    ```

2. **Open the project** in Android Studio.

3. **Configure Retrofit** in your app to interact with the FastAPI backend. For detailed setup instructions, refer to the code in the [Android app directory](https://github.com/your-repo-url/android).

4. **Update the base URL** in your Retrofit configuration to point to your deployed API, like so:
   
   ```java
   Retrofit retrofit = new Retrofit.Builder()
       .baseUrl("http://<YOUR-AWS-INSTANCE-IP>:8080/")
       .addConverterFactory(GsonConverterFactory.create())
       .build();
   ```

5. Once everything is configured, you can run the Android app and it will communicate with the backend to create items in the PostgreSQL database.

### 3. Configuration for Production (Optional)

If you plan to deploy your application in a production environment, here are a few extra steps you should consider:

- **Environment Variables**: Store sensitive information such as database credentials, secret keys, etc., in environment variables or a `.env` file to keep them secure.
  
- **Scaling and Load Balancing**: If you need to handle more traffic, consider deploying your app using **AWS Elastic Beanstalk** or **Amazon ECS** to scale horizontally. You can also set up **AWS RDS** for managed PostgreSQL.

- **Monitoring**: Set up monitoring and logging using **AWS CloudWatch** or other third-party services like **Prometheus** or **Grafana**.

### 4. Accessing the Project Code

The source code for both the backend API and Android app can be found in the following directories:

- **Backend API (FastAPI + PostgreSQL)**: [Backend directory](https://github.com/your-repo-url/backend)
- **Android App**: [Android directory](https://github.com/your-repo-url/android)

Each directory contains detailed instructions and example code to help you get started with setting up and interacting with the API.

---

## License
This project is licensed under the MIT License.

---


