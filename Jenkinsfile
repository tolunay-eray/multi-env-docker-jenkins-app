pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'test', 'prod'],
            description: 'Choose the environment to deploy'
        )
    }

    environment {
        ENV_FILE = ".env.${params.ENV}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/tolunay-eray/multi-env-docker-jenkins-app.git'
            }
        }

        stage('Clean Previous Containers') {
            steps {
                sh 'docker compose down || true'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh """
                docker compose --env-file ${ENV_FILE} up -d --build
                """
            }
        }
    }
}